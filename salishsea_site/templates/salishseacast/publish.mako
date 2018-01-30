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

<%inherit file="../site.mako"/>
<%namespace file="figures_page_defs.mako" import="header_link, list_of_plots, figure_row, figure_group, show_figure, figure_nav_links"/>

<%block name="title">${results_date.format('dddd, D MMMM YYYY')} – Salish Sea Storm Surge ${run_type_title}</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>${results_date.format('dddd, D MMMM YYYY')} – Salish Sea Storm Surge ${run_type_title}</h1>

      <h3 id="${figures[0].title | slug}"> ${figures[0].title} ${header_link(figures[0].title) | slug} </h3>
      <img class="img-responsive"
        src="${request.static_url(figures[0].path(run_type, run_date))}"
        alt="${figures[0].title} image">
    </div>
  </div>

  <div class="row">
    <div class="col-md-12">
      <h2>Disclaimer</h2>
      <p>
        This page presents output from a research project.
        Results are not expected to be a robust prediction of the storm surge.
      </p>
      <p>
        Model sea surface height has been evaluated through a series of hindcasts for significant surge events in 2006,
        2009, and 2012 <a id="#footnote1-back-link" href="#footnote1" title="Link to citation">[1]</a>.
      </p>

      <h3>Reference</h3>
      <p>
        <a id="footnote1" href="#footnote1-back-link" title="Link to reference">[1]</a>
        Soontiens, N., Allen, S., Latornell, D., Le Souef, K., Machuca, I., Paquin, J.-P., Lu, Y., Thompson, K., Korabel, V. (2015).
        Storm surges in the Strait of Georgia simulated with a regional model.
        Atmosphere-Ocean volume 54, issue 1.
        <a href="https://dx.doi.org/10.1080/07055900.2015.1108899" title="Link to paper via DOI">
          https://dx.doi.org/10.1080/07055900.2015.1108899
        </a>
      </p>
    </div>
  </div>

  ${list_of_plots(figure_links)}

  %for figure in figures[1:]:
    ${figure_row(figure, run_type, run_date)}
    ${figure_nav_links()}
  %endfor

  %if any(tides_max_ssh_figures_available):
    ${figure_group(tides_max_ssh_figures, tides_max_ssh_figures_available, run_type, run_date)}
    ${figure_nav_links()}
  %endif

  %if wind_figure_available:
    ${figure_row(sand_heads_wind_figure, run_type, run_date)}
    ${figure_nav_links()}
  %endif

  <%include file="data_sources.mako"/>
</div>


<%block name="page_js">
  <script>
    function init() { }
  </script>
  ${show_figure()}
</%block>
