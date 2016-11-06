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

<%block name="navbar">
  <nav class="navbar navbar-inverse" role="navigation">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed"
                data-toggle="collapse" data-target="#bs-salissea-navbar-collapse"
                aria-expanded="false">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a href="https://salishsea.eos.ubc.ca/" class="navbar-brand">Salish Sea</a>
      </div>

      <div id="bs-salishsea-navbar-collapes" class="collapse navbar-collapse">
        <ul class="nav navbar-nav">
          <li class="dropdown">
            <a href="#" class="dropdown-toggle"
               data-toggle="dropdown" role="button"
               aria-haspopup="true" aria-expanded="false">
              Storm Surge <span class="caret"></span>
            </a>
            <ul class="dropdown-menu" role="menu">
              <li><a href="https://salishsea.eos.ubc.ca/storm-surge/index.html">Information Portal</a></li>
              <li><a href="https://salishsea.eos.ubc.ca/storm-surge/forecast.html"> SalishSeaCast Forecast</a></li>
              <li><a href="#"><span class="fa fa-rss" aria-hidden="true"></span> Feeds</a></li>
            </ul>
          </li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle"
               data-toggle="dropdown" role="button"
               aria-haspopup="true" aria-expanded="false">
              SalishSeaCast <span class="caret"></span>
            </a>
            <ul class="dropdown-menu" role="menu">
              <li><a href="https://salishsea.eos.ubc.ca/nemo/index.html">About</a></li>
              <li><a href=${request.route_url('results.index')}>Results</a></li>
              <li><a href="https://salishsea.eos.ubc.ca/erddap/">ERDDAP</a></li>
              <li><a href="#">Automation Monitoring</a></li>
            </ul>
          </li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle"
               data-toggle="dropdown" role="button"
               aria-haspopup="true" aria-expanded="false">
              Bloomcast <span class="caret"></span>
            </a>
            <ul class="dropdown-menu" role="menu">
              <li><a href="https://salishsea.eos.ubc.ca/bloomcast.html">About</a></li>
              <li><a href="https://salishsea.eos.ubc.ca/bloomcast/spring_diatoms.html">Spring Diatoms</a></li>
            </ul>
          </li>
          <li class="dropdown"><a href="#">SMELT</a></li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle"
               data-toggle="dropdown" role="button"
               aria-haspopup="true" aria-expanded="false">
              About <span class="caret"></span>
            </a>
            <ul class="dropdown-menu" role="menu">
              <li><a href=${request.route_url('about.contributors')}>Contributors</a></li>
              <li><a href="#">Publications</a></li>
              <li><a href="https://salishsea.eos.ubc.ca/license.html">License</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</%block>
