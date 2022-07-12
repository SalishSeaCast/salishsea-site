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
<%inherit file="site.mako"/>

<%block name="title">Salish Sea Oceanography</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>UBC Salish Sea Model Project</h1>
    </div>
  </div>

  <div class="row">
    <div class="col-md-4">
      <h3>About the Project</h3>
      <a href=${request.route_url('salishseacast.about')}>
        <img class="img-responsive index"
             src="${request.static_url('/results/nowcast-sys/figures/salishsea-site/static/img/index_page/about_project.svg')}"
             alt="Salish Sea Oceanography Model Products">
      </a>
      <p class="index">
        A three-dimensional physical-biological-chemical ocean model for the Strait of Georgia and Salish Sea.
      </p>
    </div>
    <div class="col-md-4">
      <h3>Storm Surge Forecast</h3>
      <a href=${request.route_url('storm_surge.forecast')}>
        <img class="img-responsive index"
             src="${request.static_url('/results/nowcast-sys/figures/salishsea-site/static/img/index_page/storm_surge_forecast.svg')}"
             alt="Salish Sea Oceanography Model Products">
      </a>
      <p class="index">
        Marine and atmospheric conditions: storm surge alerts, tidal predictions, surface height, and winds.
      </p>
    </div>
    <div class="col-md-4">
      <h3>Diatom Bloom Forecast</h3>
      <a href=${request.route_url('bloomcast.spring_diatoms')}>
        <img class="img-responsive index"
             src="${request.static_url('/results/nowcast-sys/figures/salishsea-site/static/img/index_page/diatom_bloom_forecast.svg')}"
             alt="Salish Sea Oceanography Model Products">
      </a>
      <p class="index">
        SOG biophysical model: best estimate of the first spring diatom bloom in the Straight of Georgia.
      </p>
    </div>
  </div>

  <div class="row">
    <div class="col-md-4">
      <h3>Storm Surge Nowcast</h3>
      <a href=${request.route_url('results.index')}>
        <img class="img-responsive index"
             src="${request.static_url('/results/nowcast-sys/figures/salishsea-site/static/img/index_page/storm_surge_nowcast.svg')}"
             alt="Salish Sea Oceanography Model Products">
      </a>
      <p class="index">
        Present marine and atmospheric conditions.
      </p>
    </div>
    <div class="col-md-4">
      <h3>Currents and Physics</h3>
      <a href=${request.route_url('results.index')}>
        <img class="img-responsive index"
             src="${request.static_url('/results/nowcast-sys/figures/salishsea-site/static/img/index_page/curents_and_physics.svg')}"
             alt="Salish Sea Oceanography Model Products">
      </a>
      <p class="index">
        Research results: salinity, temperature, and currents.
      </p>
    </div>
    <div class="col-md-4">
      <h3>Biology</h3>
      <a href=${request.route_url('results.index')}>
        <img class="img-responsive index"
             src="${request.static_url('/results/nowcast-sys/figures/salishsea-site/static/img/index_page/biology.svg')}"
             alt="Salish Sea Oceanography Model Products">
      </a>
      <p class="index">
        Research results: nitrate, diatoms, flagellates.
      </p>
    </div>
  </div>
</div>
