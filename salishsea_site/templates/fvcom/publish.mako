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

## SPDX-License-Identifier: Apache-2.0


<%inherit file="../site.mako"/>
<%namespace file="../salishseacast/figures_page_defs.mako" import="list_of_plots, figure_group, figure_row, figure_nav_links, init_image_loop_group, image_loop_group, show_figure"/>

<%block name="title">${results_date.format('dddd, D MMMM YYYY')} – VHFR FVCOM ${run_type_title}</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>${results_date.format('dddd, D MMMM YYYY')} – VHFR FVCOM ${run_type_title}</h1>
    </div>
  </div>


  <div class="row">
    <div class="col-md-12">
      <h2>Disclaimer</h2>
      <p>
        This page presents output from a research project.
        Results on this page have not been subject to statistical evaluation in comparison
        to validated instrument observations.
        Model modifications may change the way in which the results are calculated from
        day to day.
      </p>
    </div>
  </div>

  ${list_of_plots(figure_links)}

  %if available_figures["water levels"]:
    ${figure_group(water_level_figures, available_figures["water levels"], run_type, run_date, 'fvcom')}
    ${figure_nav_links('fvcom')}
  %endif

  %if available_figures["2nd narrows currents"]:
    ${figure_row(second_narrows_current_figure, run_type, run_date, 'fvcom')}
    ${figure_nav_links('fvcom')}
  %endif

  %if available_figures["image loops"]:
    ${image_loop_group(image_loops)}
    ${figure_nav_links()}
  %endif

  <%include file="../salishseacast/data_sources.mako"/>
</div>


<%block name="page_js">
  <script src="${request.static_path("salishsea_site:static/js/ImageLoop.js")}"></script>
  ${show_figure()}
  ${init_image_loop_group(image_loops, run_type, run_date, "fvcom")}
</%block>
