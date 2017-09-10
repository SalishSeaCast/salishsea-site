## Copyright 2013-2017 The Salish Sea MEOPAR Contributors
## and The University of British Columbia
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##    https://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
<%!
  from salishsea_site.mako_filters import slug
%>


<%def name="header_link(title)">
  <a class="header-link" href="#${title | slug}"
     title="Link to this heading">
    <span class="fa fa-link fa-flip-horizontal" aria-hidden="true"></span>
  </a>
</%def>


<%def name="list_of_plots(figure_links)">
  <div class="row">
    <div class="col-md-12">
      <h2 id="${'List of Plots' | slug}">Plots ${header_link('List of Plots') | slug}</h2>
      <ul>
        %for title in figure_links:
          <li><a href="#${title | slug}">${title}</a></li>
        %endfor
      </ul>
    </div>
  </div>
</%def>


<%def name="figure_row(figure, run_type, run_date)">
  <div class="row">
    <div class="col-md-12">
      <h3 id="${figure.title | slug}"> ${figure.title} ${header_link(figure.title) | slug}</h3>
      <img class="img-responsive"
        src="${request.static_url(figure.path(run_type, run_date))}"
        alt="${figure.title} image">
    </div>
  </div>
</%def>


<%def name="figure_group(figure_group, run_type, run_date)">
  <%doc>
    Render a figrue group block.

    The image title and source are updated via onclick events on a list of
    figure links that are rendered beside the image.

    Page templates that use this def must also call the show_figure() in their
    page_js block; e.g.

      <%block name="page_js">
        ${show_figure()}
      </%block>
  </%doc>
  <div class="row" id="${figure_group.description | slug}">
    <div class="col-md-12">
      <h3>${figure_group.description}: ${header_link(figure_group.description) | slug}</h3>
    </div>
  </div>
  <div class="row">
    <div class="col-md-4">
      <select class="form-control" name="${figure_group.description | slug}" onchange="showFigure(event, '${figure_group.description | slug}-img')">
        <option
          selected
            data-url="${request.static_url(figure_group.figures[0].path(run_type, run_date))}"
            value="${figure_group.figures[0].title}|${request.static_url(figure_group.figures[0].path(run_type, run_date))}">
          ${figure_group.figures[0].link_text}
        </option>
        %for figure in figure_group.figures[1:]:
          <option
              data-url="${request.static_url(figure.path(run_type, run_date))}"
              value="${figure.title}|${request.static_url(figure.path(run_type, run_date))}">
            ${figure.link_text}
          </option>
        %endfor
      </select>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <img id="${figure_group.description | slug}-img" class="img-responsive"
       src="${request.static_url(figure_group.figures[0].path(run_type, run_date))}"
       alt="${figure_group.figures[0].title} image">
    </div>
  </div>
</%def>


<%def name="show_figure()">
  <script>
    function showFigure(event, imgId) {
      var parts = event.target.value.split('|');
      document.getElementById(imgId).alt=parts[0];
      document.getElementById(imgId).src=parts[1];
    }
  </script>
</%def>


<%def name="figure_nav_links()">
  <div class="row">
    <div class="col-md-2 col-md-offset-3">
      <p class="text-center"><a href=${request.route_url('results.index')}>Results Index Page</a></p>
    </div>
    <div class="col-md-2">
      <p class="text-center"><a href="#top">Top of Page</a></p>
    </div>
    <div class="col-md-2">
      <p class="text-center"><a href="#${'List of Plots' | slug}">List of Plots</a></p>
    </div>
  </div>
</%def>
