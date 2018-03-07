## Copyright 2014-2018 The Salish Sea MEOPAR Contributors
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


<%def name="figure_row(figure, run_type, run_date, model='nemo')">
  <div class="row">
    <div class="col-md-12">
      <h3 id="${figure.title | slug}"> ${figure.title} ${header_link(figure.title) | slug}</h3>
      <img class="img-responsive"
        src="${request.static_url(figure.path(run_type, run_date, model))}"
        alt="${figure.title} image">
    </div>
  </div>
</%def>


<%def name="figure_group(figure_group, figures_available, run_type, run_date, model='nemo')">
  <%doc>
    Render a figure group block.

    The image title and source are updated via onchange events on selector
    rendered above the image that provides a list of figure links.

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
    <div class="col-md-6">
      <select class="form-control" name="${figure_group.description | slug}"
              onchange="showFigure(event, '${figure_group.description | slug}-img')">
        %for i, (figure, available) in enumerate(zip(figure_group.figures, figures_available)):
          %if available:
            <option
              selected
                value="${figure.title}|${request.static_url(figure.path(run_type, run_date, model))}">
              ${figure.link_text}
            </option>
            <% break %>
          %endif
        %endfor
        %for figure, available in zip(figure_group.figures[i+1:], figures_available[i+1:]):
          %if available:
            <option
                value="${figure.title}|${request.static_url(figure.path(run_type, run_date, model))}">
              ${figure.link_text}
            </option>
          %endif
        %endfor
      </select>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <img id="${figure_group.description | slug}-img" class="img-responsive"
       src="${request.static_url(figure_group.figures[i].path(run_type, run_date, model))}"
       alt="${figure_group.figures[i].title} image">
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


<%def name="init_image_loop(img_loop, model_var, model='nemo')">
  ${show_image_loop()}
  <script>
    function init() {
      var imageList = [
        %for run_hr in img_loop.hrs:
          "${request.static_url(img_loop.path(run_type, run_date, run_hr, model))}",
        %endfor
      ];
      jsImageLoop = initImageLoop(imageList, "${model_var}");
    }
    // Set initially visible image loop
    showImageLoop({target: {value: "${model_var}"}})
  </script>
</%def>


<%def name="image_loop(image_loop, jsImageLoop, model_var, datetime_id, slider_id)">
  <%doc>
    Render an image loop block.

    Page templates that use this def must also include a page_js block like:

      <%block name="page_js">
        <script src="${request.static_path("salishsea_site:static/js/ImageLoop.js")}"></script>
        ${init_image_loop(nitrate_loop, "nitrate")}
      </%block>
  </%doc>
  <div id="${model_var}_image_loop_container" class="image-loop hidden">
    <div class="row">
      <div class="col-md-12">
        <button class="btn btn-default" onclick="${jsImageLoop}.start()" type="button" title="Begin animation">Play</button>
        <button class="btn btn-default" onclick="${jsImageLoop}.stop()" type="button" title="Stop animation">Stop</button>
        <button class="btn btn-default"
                type="button" title="Go to the first image" aria-label="Go to the first image"
                onclick="${jsImageLoop}.goto('beginning')" >
          <i class="fa fa-fast-backward" aria-hidden="true"></i>
        </button>
        <button class="btn btn-default"
                type="button" title="Go to the previous image" aria-label="Go to the previous image"
                onclick="${jsImageLoop}.goto('left')" >
          <i class="fa fa-backward" aria-hidden="true"></i>
        </button>
        <button class="btn btn-default"
                type="button" title="Go to the next image" aria-label="Go to the next image"
                onclick="${jsImageLoop}.goto('right')" >
          <i class="fa fa-forward" aria-hidden="true"></i>
        </button>
        <button class="btn btn-default"
                type="button" title="Go to the last image" aria-label="Go to the last image"
                onclick="${jsImageLoop}.goto('end')" >
          <i class="fa fa-fast-forward" aria-hidden="true"></i>
        </button>
        <span class="inline">Direction:
          <button class="btn btn-default" id="btnDirection"
                  type="button" title="Animation's current direction. Click to change."
                  aria-label="Animation's current direction. Click to change."
                  onclick="this.innerHTML=${jsImageLoop}.toggleDirection()">forward</button>
        </span>
        <span class="inline">Speed:
          <button class="btn btn-default" id="increaseSpeed"
                  type="button" title="Increase animation speed" aria-label="Increase animation speed"
                  onclick="${jsImageLoop}.changeSpeed(-100)" >
            <i class="fa fa-chevron-up" aria-hidden="true"></i>
          </button>
          <button class="btn btn-default"
                  type="button" title="Reduce animation speed" aria-label="Reduce animation speed"
                  onclick="${jsImageLoop}.changeSpeed(+100)">
            <i class="fa fa-chevron-down" aria-hidden="true"></i>
          </button>
        </span>
      </div>
    </div>

    <div class="row">
      <div class="col-md-4">
        <div id="${datetime_id}" title="Current image date/time"></div>
      </div>
      <div class="col-md-8">
        <div id="${slider_id}"></div>
      </div>
    </div>

    <div class="row">
      <div class="col-md-12">
        <div id="${model_var}_image_loop_canvas"></div>
      </div>
    </div>
  </div>
</%def>


<%def name="show_image_loop()">
  <script>
    function showImageLoop(event) {
      // Hide all of the div.image-loop elements
      var imageLoops = document.getElementsByClassName('image-loop');
      for (var i=0; i < imageLoops.length; i++) {
        imageLoops[i].classList.remove('show');
        imageLoops[i].classList.add('hidden')
      }
      // Show the selected div.image-loop element
      var imageLoopToShow = document.getElementById(event.target.value + "_image_loop_container");
      imageLoopToShow.classList.remove('hidden');
      imageLoopToShow.classList.add('show')
    }
  </script>
</%def>


<%def name="init_image_loop_group(image_loops, model='nemo')">
  ${show_image_loop()}
  <script>
    function init() {
      var imageLists = new Array();
      jsImageLoops = new Array();
      %for i, img_loop in enumerate(image_loops.loops):
        imageLists[${i}] = [
          %for run_hr in img_loop.hrs:
            "${request.static_url(img_loop.path(run_type, run_date, run_hr, model))}",
          %endfor
        ];
        jsImageLoops[${i}] = initImageLoop(imageLists[${i}], "${image_loops.loops[i].model_var}");
      %endfor
    }
    // Set initially visible image loop
    showImageLoop({target: {value: "${image_loops.loops[0].model_var}"}})
  </script>
</%def>


<%def name="image_loop_group(group)">
  <%doc>
    Render a image loop group block.

    The onchange event on the selector above the collection of image loop
    blocks sets the visibility of the desired image loop.

    Page templates that use this def must also call the show_image_loop()
    in their page_js block; e.g.

      <%block name="page_js">
        <script src="${request.static_path("salishsea_site:static/js/ImageLoop.js")}"></script>
        ${init_image_loop_group(image_loops)}
      </%block>
  </%doc>
  <div class="row" id="${group.description | slug}">
    <div class="col-md-12">
      <h3>${group.description}: ${header_link(group.description) | slug}</h3>
    </div>
  </div>
  <div class="row">
    <div class="col-md-6">
      <select class="form-control" name="${group.description | slug}"
              onchange="showImageLoop(event)">
        <option selected value="${group.loops[0].model_var}">${group.loops[0].link_text}</option>
        %for img_loop in group.loops[1:]:
          <option value="${img_loop.model_var}">${img_loop.link_text}</option>
        %endfor
      </select>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      %for i, img_loop in enumerate(group.loops):
        %if img_loop.hrs:
          ${image_loop(
              img_loop, f"jsImageLoops[{i}]", f"{img_loop.model_var}",
              f"{img_loop.model_var}_datetime_id", f"{img_loop.model_var}_slider_id")}
        %endif
      %endfor
    </div>
  </div>
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
