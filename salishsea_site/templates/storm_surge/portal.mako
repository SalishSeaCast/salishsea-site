## Copyright 2014-2019 The Salish Sea MEOPAR Contributors
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

<%block name="title">
  Storm Surge Information Portal
</%block>

<div class="container">
  <div class="row">
    <div class="col-md-10 col-md-offset-1">
      <h1>Storm Surge Information Portal</h1>

      <p>
        This is a collection of links to web resources that may help interested parties assess
        the risks and possible impacts of storm surge events in the Salish Sea region,
        with particular emphasis on the Southern Strait of Georgia.
      </p>

      <h2>UBC SalishSeaCast Storm Surge</h2>
      <div class="row">
        <div class="col-md-5">
          <a href=${request.route_url('storm_surge.forecast')}>
            <img class="img-responsive"
              src="${request.static_url('/results/nowcast-sys/figures/storm-surge/Website_thumbnail.png')}"
              title="UBC SalishSeaCast Storm Surge Forecast"
              alt="UBC SalishSeaCast Storm Surge Forecast Thumbnail Image">
          </a>
        </div>
        <div class="col-md-7">
          <p>
            <a href=${request.route_url('storm_surge.forecast')}>SalishSeaCast Forecast</a>
            gives our most recent forecast,
            usually for tomorrow.
            The summary figure to the left,
            shows green if maximum water levels are predicted to be below maximum tides for the year,
            orange if the maximum water levels are predicted to between maximum tides and extreme water,
            and red if the maximum water levels are predicted to be above extreme water.
            The vectors are winds averaged over the four hours previous to the predicted maximum water levels.
            The forecasting system is considered to be a research tool only and is to be used at your own risk.
            Details of the model system are at
            <a href=${request.route_url('salishseacast.about')}>SalishSeaCast NEMO Model</a>.
          </p>
        </div>
      </div>

      <h2>Storm Surge BC</h2>
      <div class="row">
        <div class="col-md-3">
          <a href="https://www.stormsurgebc.ca/">
            <img class="img-responsive"
              src="https://www.stormsurgebc.ca/files/images/alert.gif"
              title="Storm Surge BC Alert Map"
              alt="Storm Surge BC Alert Map">
          </a>
        </div>
        <div class="col-md-9">
          <p>
            <a href="https://stormsurgebc.ca/">Storm Surge BC</a>
            is the British Columbia Storm Surge Forecasting Program site.
            The program is a joint effort between the BC Ministry of Environment
            and the federal Department of Fisheries and Oceans.
            The objective of the program is to provide 6-day forecasts of storm surge
            and total water levels at several sites in the marine waters of southern British Columbia.
            A predictive numerical ocean model and real-time data monitoring are employed to generate
            <a href="https://stormsurgebc.ca/bulletins.html">bulletins</a>
            for Victoria, Vancouver and Campbell River.
            The site also provides a
            <a href="https://stormsurgebc.ca/almanac.html">seasonal almanac</a>
            and a <a href="https://stormsurgebc.ca/twitter.html">Twitter feed</a>.
            The forecasting system is considered to be a research tool only and is to be used at your own risk.
            <a href="https://stormsurgebc.ca/">Storm Surge BC</a>
            is maintained by
            <a href="https://stormsurgebc.ca/contact.html">Dr. Scott Tinis</a>.
          </p>
        </div>
      </div>

      <h2>Halibut Bank Weather Buoy</h2>
      <p>
        The
        <a href="https://weather.gc.ca/marine/weatherConditions-currentConditions_e.html?mapID=02&siteID=14305&stationID=46146">
          Halibut Bank Weather Buoy
        </a>
        is located at
        <a href="https://www.google.com/maps/place/49%C2%B020%2724.0%22N+123%C2%B043%2712.0%22W/@49.3077769,-123.7302997,11z/data=!4m2!3m1!1s0x0:0x0">
          49.34°N, 123.72°W
        </a>,
        west of Bowen Island and north-east of Nanaimo,
        in the open water of the south-central Georgia Strait.
        The buoy is equipped with automated weather and wave measuring sensors whose data are provided on an
        <a href="https://weather.gc.ca/marine/weatherConditions-currentConditions_e.html?mapID=02&siteID=14305&stationID=46146">
          Environment Canada web page
        </a>.
        Current conditions as well as those for the preceding 24 hours are available.
      </p>

      <h2>NOAA Storm Surge Forecast at Neah Bay, WA</h2>
      <p>
        The US National Oceanic and Atmospheric Administration (NOAA) maintains storm surge advisory pages
        for various locations on the Pacific Coast.
        The
        <a href="http://www.nws.noaa.gov/mdl/etsurge/index.php?page=stn&region=wc&datum=mllw&list=&map=0-48&type=both&stn=waneah">
          Neah Bay, Washington advisory page
        </a>
        provides measurements and model predictions of the sea surface height at the entrance to the Strait of Juan de Fuca.
        The forecast extends about 3 and a half days into the future.
        The water level at Neah Bay provides information about the effects of Pacific Ocean storms on the Salish Sea water levels.
        The same NOAA site also provides advisories for other locations on the Washington State coast of the Salish Sea,
        including,
        Port Angeles,
        Port Townsend,
        Friday Harbor,
        and Cherry Point.
      </p>

      <h2>Sea Level Rise and Storm Surges on the BC Coast</h2>
      <p>
        The BC provincial government maintains a
        <a href="http://www2.gov.bc.ca/gov/content/environment/climate-change/policy-legislation-programs/adaptation/sea-level-rise">
          web page about climate change adaptation
        </a>
        with information about sea level rise and storm surges.
        The storm surge information there elaborates on the
        <a href="https://stormsurgebc.ca/">Storm Surge BC</a>
        site.
      </p>

      <h2>SalishSeaCast NEMO Model</h2>
      <p>
        Work is presently under way to evaluate the
        <a href=${request.route_url('salishseacast.about')}>SalishSeaCast NEMO model's</a>
        calculations of tides and sea surface height by hindcasting storm surge events that occurred between 2002 and 2011.
        Once the model's hindcasting skill has been determined to be adequate,
        and atmospheric model products of sufficient resolution are available,
        the intent is to run the model to provide daily sea surface height forecasts that will be published to the web.
        When that objective is reached the Salish Sea NEMO model will augment the storm surge prediction
        and risk assessment resources listed above.
      </p>

      <h2>Feedback</h2>
      <p>
        If you have comments or questions on the information provided on this page,
        or suggestions of other resources that should be linked here,
        please contact <a href="mailto:sallen@eoas.ubc.ca">Susan Allen</a>.
      </p>
    </div>
  </div>
</div>
