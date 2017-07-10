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
<%namespace file="figures_page_defs.mako" import="header_link, list_of_plots, figure_row, figure_nav_links"/>

<%block name="title">Salish Sea Model Biology – ${results_date.format('DD-MMM-YYYY')}</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>Salish Sea Model Biology</h1>

      <h2>Evaluation Results from Nowcast</h2>

      <h2>${results_date.format('dddd, D MMMM YYYY')}</h2>

      <h2>Disclaimer</h2>
      <p>
        This page presents output from a research project.
        Results on this page are either:
      </p>
        <ol>
          <li>not yet evaluated, or</li>
          <li>have been evaluated but do not agree well with observations.</li>
        </ol>
      <p>
        For the latter we are working on model modifications.
      </p>

      <h2>References</h2>
      <ul>
        <li>
          Soontiens, N., Allen, S., Latornell, D., Le Souef, K., Machuca, I., Paquin, J.-P., Lu, Y., Thompson, K., Korabel, V. (2015).
          Storm surges in the Strait of Georgia simulated with a regional model.
          Atmosphere-Ocean volume 54, issue 1, pp 1-21.
          <a href="https://dx.doi.org/10.1080/07055900.2015.1108899" title="Link to paper via DOI">
            https://dx.doi.org/10.1080/07055900.2015.1108899
          </a>
        </li>
        <li>
          Soontiens, N. and Allen, S.
          Modelling sensitivities to mixing and advection in a sill-basin estuarine system. 
          Ocean Modelling, volume 112, pp 17-32.
          <a href="https://dx.doi.org/10.1016/j.ocemod.2017.02.008" title="Link to paper via DOI">
            https://dx.doi.org/10.1016/j.ocemod.2017.02.008
          </a>
        </li>
      </ul>
    </div>
  </div>

  <div class="image-loop">
    <div class="row">
      <div class="col-md-12">
        <h3 id="${image_loop.title | slug}"> ${image_loop.title} ${header_link(image_loop.title) | slug}</h3>

        <button class="btn btn-default" onclick="il.start()" type="button" title="Begin animation">Play</button>
        <button class="btn btn-default" onclick="il.stop()" type="button" title="Stop animation">Stop</button>
        <button class="btn btn-default"
                type="button" title="Go to the first image" aria-label="Go to the first image"
                onclick="il.goto('beginning')" >
          <i class="fa fa-fast-backward" aria-hidden="true"></i>
        </button>
        <button class="btn btn-default"
                type="button" title="Go to the previous image" aria-label="Go to the previous image"
                onclick="il.goto('left')" >
          <i class="fa fa-backward" aria-hidden="true"></i>
        </button>
        <button class="btn btn-default"
                type="button" title="Go to the next image" aria-label="Go to the next image"
                onclick="il.goto('right')" >
          <i class="fa fa-forward" aria-hidden="true"></i>
        </button>
        <button class="btn btn-default"
                type="button" title="Go to the last image" aria-label="Go to the last image"
                onclick="il.goto('end')" >
          <i class="fa fa-fast-forward" aria-hidden="true"></i>
        </button>
        <span class="inline">Direction:
          <button class="btn btn-default" id="btnDirection"
                  type="button" title="Animation's current direction. Click to change."
                  aria-label="Animation's current direction. Click to change."
                  onclick="this.innerHTML=il.toggleDirection()">forward</button>
        </span>
        <span class="inline">Speed:
          <button class="btn btn-default" id="increaseSpeed"
                  type="button" title="Increase animation speed" aria-label="Increase animation speed"
                  onclick="il.changeSpeed(-100)" >
            <i class="fa fa-chevron-up" aria-hidden="true"></i>
          </button>
          <button class="btn btn-default"
                  type="button" title="Reduce animation speed" aria-label="Reduce animation speed"
                  onclick="il.changeSpeed(+100)">
            <i class="fa fa-chevron-down" aria-hidden="true"></i>
          </button>
        </span>
        <!--We don't show these selectors, but ImageLoop.js uses them -->
        <select class="hidden" id="indexStart"><option></option></select>
        <select class="hidden" id="indexEnd"><option></option></select>
      </div>
    </div>

    <div class="row">
      <div class="col-md-4">
        <div id="datetime" title="Current image date/time"></div>
      </div>
      <div class="col-md-8">
        <div id="slider"></div>
      </div>
    </div>

    <div class="row">
      <div class="col-md-12">
        <div id="il"></div>
      </div>
    </div>
  </div>

  <%include file="data_sources.mako"/>
</div>


<%block name="page_js">
  <script src="${request.static_path("salishsea_site:static/js/ImageLoop.js")}"></script>
  <script>
    var datetime = null;
    var sl = null;
    var il = null;
    var imgType = "dateTimes";
    var images = [
        %for run_hr in image_loop_hrs:
          "${request.static_url(image_loop.path(run_type, run_date, run_hr))}",
        %endfor
    ];
  </script>
</%block>
