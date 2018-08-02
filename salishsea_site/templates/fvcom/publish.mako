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

<%inherit file="../site.mako"/>
<%namespace file="../salishseacast/figures_page_defs.mako" import="list_of_plots, figure_group, figure_row, figure_nav_links"/>

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

  ${figure_group(water_level_figures, water_level_figures_available, run_type, run_date, 'fvcom')}
  ${figure_nav_links('fvcom')}

  %if currents_figure_available:
    ${figure_row(second_narrows_current_figure, run_type, run_date, 'fvcom')}
    ${figure_nav_links('fvcom')}
  %endif

  <%include file="../salishseacast/data_sources.mako"/>
</div>
