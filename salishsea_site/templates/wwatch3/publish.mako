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
<%namespace file="../salishseacast/figures_page_defs.mako" import="figure_group, show_figure"/>

<%block name="title">${results_date.format('dddd, D MMMM YYYY')} – VHFR FVCOM ${run_type_title}</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>${results_date.format('dddd, D MMMM YYYY')} – WaveWatch3™ ${run_type_title}</h1>
    </div>
  </div>

  ${figure_group(figures, figures_available, run_type, run_date, 'wwatch3')}

</div>


<%block name="page_js">
  <script>
    function init() { }
  </script>
  ${show_figure()}
</%block>
