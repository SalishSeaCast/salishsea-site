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

<%inherit file="../site.mako"/>
<%namespace file="../salishseacast/results_index_page_defs.mako" import="month_heading"/>

<%block name="title">
  VHFR FVCOM Model Daily Results
</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>Vancouver Harbour/Fraser River FVCOM Model Daily Results</h1>
    </div>
  </div>

  <div class="row">
    <div class="col-md-9 col-md-offset-1">
      <table class="table table-striped">
        <tr>
          <td></td>
          %if last_month_cols != 0:
            ${month_heading(last_month_cols, first_date)}
          %endif
          ${month_heading(this_month_cols, last_date)}
        </tr>
        <tr>
          <th class="results-index">Water Levels, Currents &amp; Thalweg Transects</th>
        </tr>
        ${grid_row("X2 Nowcast", grid_dates['x2 nowcast water levels'], "nowcast-x2", "publish")}
        ${grid_row("R12 Nowcast", grid_dates['r12 nowcast water levels'], "nowcast-r12", "publish")}
        ${grid_row("X2 Forecast", grid_dates['x2 forecast water levels'], "forecast-x2", "publish")}
      </table>
    </div>
  </div>
</div>


<%def name="grid_row(title, dates, run_type, figs_type)">
  <tr>
    <td class="text-right">${title}</td>
    %for d in dates:
      <td class="text-center">
        %if d is None:
          &nbsp;
        %else:
          <a href=${request.route_url(
                      'fvcom.results.{run_type}.{figs_type}'.format(run_type=run_type, figs_type=figs_type),
                      results_date=d.format('DDMMMYY').lower())}>
            ${d.format("D")}
          </a>
        %endif
      </td>
    %endfor
  </tr>
</%def>
