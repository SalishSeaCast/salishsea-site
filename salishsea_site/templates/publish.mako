## Copyright 2013-2016 The Salish Sea MEOPAR Contributors
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
<%inherit file="site.mako"/>
<%
  from salishsea_site.mako_filters import slug
%>

<%block name="title">${results_date.format('dddd, D MMMM YYYY')} – Salish Sea Storm Surge ${run_type_title}</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>${results_date.format('dddd, D MMMM YYYY')} – Salish Sea Storm Surge ${run_type_title}</h1>

      <h3 id="${figures[0].title | slug}"> ${figures[0].title} ${header_link(figures[0].title)} </h3>
      <img class="img-responsive"
        src="${request.static_url(
                '/results/nowcast-sys/figures/{run_type}/{run_dmy}/{svg_name}_{run_dmy}.svg'
                .format(run_type=run_type, svg_name=figures[0].svg_name, run_dmy=run_date.format('DDMMMYY').lower()))}"
        alt="${figures[0].title} image">
    </div>
  </div>

  <div class="row">
    <div class="col-md-12">
      <h2>Disclaimer</h2>
      <p>
        This page presents output from a research project.
        Results are not expected to be a robust prediction of the storm surge.
      </p>
      <p>
        Model sea surface height has been evaluated through a series of hindcasts for significant surge events in 2006,
        2009, and 2012 <a id="#footnote1-back-link" href="#footnote1" title="Link to citation">[1]</a>.
      </p>

      <h3>Reference</h3>
      <p>
        <a id="footnote1" href="#footnote1-back-link" title="Link to reference">[1]</a>
        Soontiens, N., Allen, S., Latornell, D., Le Souef, K., Machuca, I., Paquin, J.-P., Lu, Y., Thompson, K., Korabel, V. (2015).
        Storm surges in the Strait of Georgia simulated with a regional model.
        Atmosphere-Ocean volume 54, issue 1.
        <a href="https://dx.doi.org/10.1080/07055900.2015.1108899" title="Link to paper via DOI">
          https://dx.doi.org/10.1080/07055900.2015.1108899
        </a>
      </p>
    </div>
  </div>

  <div class="row">
    <div class="col-md-12">
      <h2 id="${'List of Plots' | slug}">Plots ${header_link('List of Plots')}</h2>
      <ul>
        %for figure in figures:
          <li><a href="#${figure.title | slug}">${figure.title}</a></li>
        %endfor
      </ul>
    </div>
  </div>

  %for figure in figures[1:]:
    <div class="row">
      <div class="col-md-12">
        <h3 id="${figure.title | slug}"> ${figure.title} ${header_link(figure.title)} </h3>
        <img class="img-responsive"
          src="${request.static_url(
                  '/results/nowcast-sys/figures/{run_type}/{run_dmy}/{svg_name}_{run_dmy}.svg'
                  .format(run_type=run_type, svg_name=figure.svg_name, run_dmy=run_date.format('DDMMMYY').lower()))}"
          alt="${figure.title} image">
      </div>
      <div class="row">
        <div class="col-md-2 col-md-offset-3">
          <p class="text-center"><a href="https://salishsea.eos.ubc.ca/nemo/results/">Index Page</a></p>
        </div>
        <div class="col-md-2">
          <p class="text-center"><a href="#top">Top of Page</a></p>
        </div>
        <div class="col-md-2">
          <p class="text-center"><a href="#${'List of Plots' | slug}">List of Plots</a></p>
        </div>
      </div>
    </div>
  %endfor

  <div class="row">
    <div class="col-md-12">
      <h2 id="${'Data Sources' | slug}">Data Sources ${header_link('Data Sources')}</h2>
      <p>The forcing data used to drive the Salish Sea model is obtained from several sources:</p>
      <dl>
        <dt>Winds and metorological conditions</dt>
        <dd>
          <ul>
            <li>
              <a href="https://weather.gc.ca/grib/grib2_HRDPS_HR_e.html">High Resolution Deterministic Prediction System</a>
              (HRDPS) from Environment Canada.
            </li>
          </ul>
        </dd>

        <dt>Open boundary conditions</dt>
        <dd>
          <ul>
            <li>
              <a href="http://www.nws.noaa.gov/mdl/etsurge/index.php?page=stn&region=wc&datum=msl&list=wc&map=0-48&type=both&stn=waneah">
              NOAA Storm Surge Forecast
              </a>
              at Neah Bay, WA.
            </li>
          </ul>
        </dd>

        <dt>Rivers</dt>
        <dd>
          <ul>
            <li>
              Fraser river: Real-time Environment Canada data at
              <a
                href="https://wateroffice.ec.gc.ca/report/report_e.html?mode=Table&type=realTime&stn=08MF005&dataType=Real-Time&startDate=2014-12-30&endDate=2015-01-06&prm1=47&prm2=-1">Hope</a>
            </li>
            <li>
              Other rivers:
              J. Morrison , M. G. G. Foreman and D. Masson, 2012.
              A method for estimating monthly freshwater discharge affecting British Columbia coastal waters.
              Atmosphere-Ocean volume 50, issue 1.
              <a href="http://dx.doi.org/10.1080/07055900.2011.637667">http://dx.doi.org/10.1080/07055900.2011.637667</a>
            </li>
          </ul>
        </dd>
        <dt>Tidal constituents</dt>
        <dd>
          <ul>
            <li>
              <p>Tidal predictions were generated using constituents from the Canadian Hydrographic Service.</p>
              <p>
                This product has been produced by the
                <strong>Department of Earth, Ocean and Atmospheric Sciences, University of British Columbia</strong>
                based on Canadian Hydrographic Charts and/or data,
                pursuant to CHS Direct User Licence No. 2015-0303-1260-S.
              </p>
              <p>
                The incorporation of data sourced from CHS in this product shall not be construed as constituting
                an endorsement by CHS of this product.
              </p>
              <p>
                This product does not meet the requirements of the
                <em>Charts and Nautical Publications Regulations, 1995</em>
                under the
                <em>Canada Shipping Act, 2001</em>.
                Official charts and publications,
                corrected and up-to-date,
                must be used to meet the requirements of those regulations.
              </p>
            </li>
          </ul>
        </dd>
      </dl>
      <p></p>
      <p></p>
      <p></p>
    </div>
  </div>
</div>


<%def name="header_link(title)">\
  <a class="header-link" href="#${title | slug}"
     title="Link to this heading">
    <span class="fa fa-link fa-flip-horizontal" aria-hidden="true"></span>
  </a>
</%def>
