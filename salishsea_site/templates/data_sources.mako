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
<%namespace file="header_link.mako" import="header_link"/>
<%
  from salishsea_site.mako_filters import slug
%>
<div class="row">
  <div class="col-md-12">
    <h2 id="${'Data Sources' | slug}">Data Sources ${header_link(slug('Data Sources'))}</h2>
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
