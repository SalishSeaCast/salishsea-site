## Copyright 2013-2017 The Salish Sea MEOPAR Contributors
## and The University of British Columbia
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##    http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
<%inherit file="../site.mako"/>

<%block name="title">${data_date} Spring Diatom Bloom Forecast</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>${data_date} Spring Diatom Bloom Forecast</h1>

      <p>
        The current best estimate of the first spring diatom bloom in the Strait of Georgia is
        ${bloom_dates[prediction['median']]}.
        That estimate is based on a run of the
        <a href="https://www.eoas.ubc.ca/~sallen/SOG-docs/">SOG biophysical model for deep estuaries</a>
        <a href="#footnote1" id="footnote1-back-link" title="Link to citation">[1]</a>
        with the following parameters:
      </p>
      <ol>
        <li>
          Run start date/time: ${run_start_date}
        </li>
        <li>
          Actual wind,
          meteorological,
          and river flow forcing data to ${data_date},
          and historical data from ${prediction['median']} thereafter

        </li>
      </ol>
      <p>
        ${prediction['median']} has the median bloom date in an ensemble of SOG runs that use historical wind,
        meteorological,
        and river flow data from 1980 through 2010 as future forcing data after ${data_date}.
      </p>
      <p>
        Best estimate bounds on the bloom date are:
      </p>
      <ul>
        <li>
          No earlier than ${bloom_dates[prediction['early']]} based on using actual forcing data to ${data_date},
          and data from ${prediction['early'] - 1}/${prediction['early']} thereafter.
          ${prediction['early']} has the 5th centile bloom date in the ensemble of SOG runs.
        </li>
        <li>
          No later than ${bloom_dates[prediction['late']]} based on using actual forcing data to ${data_date},
          and data from ${prediction['late'] - 1}/${prediction['late']} thereafter.
          ${prediction['late']} has the 95th centile bloom date in the ensemble of SOG runs.
        </li>
      </ul>
      <p>
        <a id="footnote1" href="#footnote1-back-link" title="Link to reference">[1]</a>
        Allen, S. E. and M. A. Wolfe. (2013).
        Hindcast of the Timing of the Spring Phytoplankton Bloom in the Strait of Georgia, 1968-2010.
        Progress in Oceanography, volume 115, pp 6-13.
        <a href="http://dx.doi.org/10.1016/j.pocean.2013.05.026" title="Link to paper via DOI">
          http://dx.doi.org/10.1016/j.pocean.2013.05.026
        </a>
      </p>

      <h2>Data Sources</h2>
      <p>
        The forcing data used to drive the SOG model is obtained from several sources:
      </p>
      <ul>
        <li>
          Hourly wind velocities at 
          <a href="http://www.lighthousefriends.com/light.asp?ID=1178">Sand Heads Lightstation</a>
          from the historical data web service at
          <a href="http://climate.weather.gc.ca/">climate.weather.gc.ca/</a>
        </li>
          Hourly air temperature,
          relative humidity,
          and weather description
          (from which cloud fraction is calculated)
          at Vancouver International Airport
          (YVR)
          from the historical data web service at
          <a href="http://climate.weather.gc.ca/">climate.weather.gc.ca/</a>
        <li>
          Average daily river discharge rates for the
          <a href="http://www.aquatic.uoguelph.ca/rivers/fraser.htm">Fraser River</a>,
          and the <a href="http://en.wikipedia.org/wiki/Englishman_River">Englishman River</a>
          (as a proxy for the fresh water sources other than the Fraser)
          from <a href="http://wateroffice.ec.gc.ca/">wateroffice.ec.gc.ca</a>
        </li>
      </ul>

      <h2>Disclaimer</h2>
      <p>
        This site presents output from a research project.
        Results are not expected to be a robust prediction of the timing of the spring bloom.
        At this point,
        we believe such a prediction is not possible before mid-February using any model and this model is not yet tested.
      </p>

      <h2>Time Series</h2>
      <img class="img-responsive"
        src="${request.static_url(str(plots_path/ts_plot_files['nitrate_diatoms']))}"
        alt="Profiles from Median Prediction">
      <img class="img-responsive"
        src="${request.static_url(str(plots_path/ts_plot_files['temperature_salinity']))}"
        alt="Profiles from Median Prediction">
      <img class="img-responsive"
        src="${request.static_url(str(plots_path/ts_plot_files['mld_wind']))}"
        alt="Profiles from Median Prediction">

      <h2>Profiles at ${data_date} 12:00 from Median Prediction</h2>
      <img class="img-responsive"
        src="${request.static_url(str(plots_path/profiles_plot_file))}"
        alt="Profiles from Median Prediction">

      <h2>Bloom Date Evolution</h2>
      <table class="table table-striped">
        <thead>
          <tr>
            <th class="transition-date" rowspan="2">
              Actual to Ensemble Forcing Transition Date</th>
            <th class="centre-span2" colspan="2">Median</th>
            <th class="centre-span2" colspan="2">5th Centile Early Bound</th>
            <th class="centre-span2" colspan="2">95th Centile Late Bound</th>
            <th class="centre-span2" colspan="2">Earliest Ensemble Result</th>
            <th class="centre-span2" colspan="2">Latest Ensemble Result</th>
          </tr>
          <tr>
            %for i in range(5):
              <th class="bloom-date">Bloom Date</th>
              <th class="ensemble-member">Ensemble Member</th>
            %endfor
          </tr>
        </thead>
        <tbody>
          %for row in bloom_date_log:
            <tr>
              %for value in row:
                <td>${value}</td>
              %endfor
              %for i in range(len(row) + 1, 12):
                <td>N/A</td>
              %endfor
            </tr>
          %endfor
        </tbody>
       </table>

    </div>
  </div>
</div>
