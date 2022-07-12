## Copyright 2014 – present by the Mesoscale Ocean and Atmospheric Dynamics (MOAD) group
## in the Department of Earth, Ocean, and Atmospheric Sciences
## at The University of British Columbia
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
<%namespace file="figures_page_defs.mako" import="header_link, list_of_plots, figure_row, init_image_loop_group, image_loop_group, figure_nav_links"/>

<%block name="title">Salish Sea Surface Current Tiles – ${results_date.format('DD-MMM-YYYY')}</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>Surface Currents</h1>

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

      <img src="${request.static_path("salishsea_site:static/img/surface_currents_tilemap.svg")}"
           usemap="#tileclickmap" width="500" height="600">
      <%include file="surface_current_tilemap.html"/>

    </div>
  </div>

  ## This placeholder link here gets set by regionMap()
  <a id="pdflink" download></a>

  ${image_loop_group(image_loops)}

  <%include file="data_sources.mako"/>
</div>


<%block name="page_js">
  <script src="${request.static_path("salishsea_site:static/js/ImageLoop.js")}"></script>
  ${init_image_loop_group(image_loops, run_type, run_date, 'surface currents')}

    ## This is the function called when a tile is clicked in the tilemap
  <script>
    ## tilemap click handler
    function regionMap(tilenumber) {
      if (tilenumber < 10) {
        var tilenumberstr = "0" + tilenumber.toString();
      } else {
        var tilenumberstr = tilenumber.toString();
      }
      ## Set the dropdown box
      document.getElementsByClassName("form-control")[0].selectedIndex = tilenumber - 1;
      ## Switch to the clicked tile map
      showImageLoop({target: {value: "Tile" + tilenumberstr}});
      ## Update the PDF link
      document.getElementById("pdflink").innerHTML = "Download PDF time series for tile " + tilenumberstr;
      document.getElementById("pdflink").href = "${tiles_pdf_url_stub}".replace("xx", tilenumberstr);
    }

    ## Set tile 01 at load time
    regionMap(1)
    document.getElementsByClassName("form-control")[0].onchange = function() {
      regionMap(document.getElementsByClassName("form-control")[0].selectedIndex + 1)
    }
  </script>
</%block>
