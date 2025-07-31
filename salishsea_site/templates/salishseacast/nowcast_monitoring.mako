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

<%block name="title">
  SalishSeaCast Automation Monitoring
</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>SalishSeaCast Automation Monitoring</h1>

      <p>
        This page presents monitoring information from the
        <a href=${request.route_url('salishseacast.about')}>SalishSeaCast NEMO model</a>
        daily nowcast and forecast runs.
        It is primarily intended for members of the Salish Sea NEMO modeling team.
        Public results of the preceding 21 days runs are linked from
        <a href=${request.route_url('results.index')}>${request.route_url('results.index')}</a>.
      </p>

      <p>
        On this page are:
        <ul>
           <li>
             A link to the
             <a href="#checklist">nowcast manager process's checklist</a>
             that shows the status of the system
           </li>
           <li>
             Links to the present and preceding 7 days'
             <a href="#log-files">log files</a>
           </li>
           <li>
             Plots produced from the
             <a href="#grib_to_netcdf-image">weather forcing dataset</a>
           </li>
           <li>
             Plot produced from the
            <a href="#get_NeahBay_ssh-image">sea surface height</a>
            observation and forecast datasets used to force the western boundary
            of the model at the mouth of the Juan de Fuca Strait
           </li>
         </ul>
      </p>

      <p>
        The public interface to access SalishSeaCast run results is the project
        ERDDAP server at
        <a href=${request.erddap_url}>${request.erddap_url}</a>.
      </p>

      <p>
        Team members with access to <kbd>skookum</kbd> can access the run results files
        at these locations:
      </p>
      <div class="row table-responsive">
        <div class="col-md-8 col-md-offset-2">
          <table class="table table-striped">
            <tbody>
              <tr>
                <td>nowcast, NEMO-3.6, physics only, since 15-Oct-2016</td>
                <td><kbd>/results/SalishSea/nowcast-blue/</kbd></td>
              </tr>
              <tr>
                <td>nowcast, NEMO-3.4, physics only, prior to 15-Oct-2016</td>
                <td><kbd>/results/SalishSea/nowcast/</kbd></td>
              </tr>
              <tr>
                <td>nowcast, NEMO-3.6, physics and biology</td>
                <td><kbd>/results/SalishSea/nowcast-green/</kbd></td>
              </tr>
              <tr>
                <td>forecast, NEMO-3.6, physics only, since 15-Oct-2016</td>
                <td><kbd>/results/SalishSea/forecast/</kbd></td>
              </tr>
              <tr>
                <td>forecast, NEMO-3.4 physics only, prior to since 15-Oct-2016</td>
                <td><kbd>/results/SalishSea/forecast-3.4/</kbd></td>
              </tr>
              <tr>
                <td>preliminary forecast, NEMO-3.6, physics only, since 15-Oct-2016</td>
                <td><kbd>/results/SalishSea/forecast2/</kbd></td>
              </tr>
              <tr>
                <td>preliminary forecast, NEMO-3.6, physics only, prior to 15-Oct-2016</td>
                <td><kbd>/results/SalishSea/forecast2-3.4/</kbd></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <p>
        Within those directories the results files are contained in directories
        named for the run date; e.g. <code>09feb15/</code>.
        Those directories contain the netCDF4 results files from the run,
        other NEMO output files,
        the configuration files used to produce the run,
        and metadata files that identify the Mercurial revisions of the code
        and forcing data repos used for the runs.
        Each day's results directory also contains a <code>figures/</code>
        subdirectory where SVG renderings of the day's results page(s) plots
        can be found.
      </p>

      <h2 id="checklist">Checklist</h2>
      <p>
        The
        <a href=${request.route_url('nowcast.logs', filename='nowcast_checklist.yaml', token='')}>nowcast checklist</a>
        is a YAML representation of the checklist dictionary that is maintained
        by the nowcast manager process.
        It reflects the present state of the nowcast system,
        showing the information returned to the manager from each of the workers.
        It is both (somewhat) human-readable,
        and machine-readable.
        The checklist is reset each morning after the forecast2 run results have been processed
        (see the discussion of log file rollovers below).
        That means that the checklist records only the results of the log file rotations
        for a period of time each morning.
        The
        <a href=${request.route_url('nowcast.logs', filename='checklist.log', token='')}>previous day's checklist</a>
        is also available.
        The checklist is stored in <kbd>/results/nowcast-sys/logs/nowcast/nowcast_checklist.yaml</kbd>
        on <kbd>skookum</kbd>.
      </p>

      <h2 id="log-files">Log Files</h2>
      <p>
        The log files contain messages from the nowcast automation workers and manager processes.
        Each day's nowcast processing is in a separate log file.
        When the day's processing is completed the log file is rolled over,
        as are the previous log files.
        The log for the current day's run
        (<a href="${request.route_url('nowcast.logs', filename='nowcast.log', token='')}">nowcast.log</a>
)
        is rolled over to
        <a href="${request.route_url('nowcast.logs', filename='nowcast.log.1', token='')}">nowcast.log.1</a>,
        and the previous
        <a href="${request.route_url('nowcast.logs', filename='nowcast.log.1', token='')}">nowcast.log.1</a>
        is rolled over to
        <a href="${request.route_url('nowcast.logs', filename='nowcast.log.2', token='')}">nowcast.log.2</a>,
        etc.
        A total of 7 day's log files are retained.
      </p>

      <p>
        There are 3 flavours of log files:
        <ul>
          <li>
            <a href="${request.route_url('nowcast.logs', filename='nowcast.log', token='')}">nowcast.log</a>
            which contains messages logged at the <kbd>info</kbd> level and above
            (<kbd>warning</kbd>, <kbd>error</kbd>, etc.).
            This is the most concise log file.
          </li>
          <li>
            <a href="${request.route_url('nowcast.logs', filename='nowcast.debug.log', token='')}">nowcast.debug.log</a>
            which contains messages logged at the <kbd>debug</kbd> level and above;
            i.e. all of the nitty-gritty details.
          </li>
          <li>
            <a href="${request.route_url('nowcast.logs', filename='checklist.log', token='')}">checklist.log</a>
            which contains a snapshot of the checklist file each morning before it is reset.
          </li>
        </ul>
      </p>

      <p>
        The log file rollovers happen each morning after the forecast2 run results
        have been processed to produce both a
        <a href=${request.route_url('results.index')}>results page</a>
        and the storm surge
        <a href=${request.route_url('storm_surge.forecast')}> forecast page</a>.
      </p>

      <div class="row table-responsive">
        <div class="col-md-12">
          <table class="table table-striped">
            <tbody>
              <tr>
                <td width="431px">
                  <a
                    href=${request.route_url('nowcast.logs', filename='nowcast.log', token='')}><kbd class="link">nowcast.log</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a
                    href=${request.route_url('nowcast.logs', filename='nowcast.debug.log', token='')}><kbd class="link">nowcast.debug.log</kbd></a>
                </td>
                <td>
                  Current log files.
                  Nearly empty after the preliminary forecast run
                  (forecast2) results have been processed and the current day's
                  run log files are rolled over to
                  <a
                    href=${request.route_url('nowcast.logs', filename='nowcast.log.1', token='')}><kbd class="link">nowcast.log.1</kbd></a>
                  and
                  <a
                    href=${request.route_url('nowcast.logs', filename='nowcast.debug.log.1', token='')}><kbd class="link">nowcast.debug.log.1</kbd></a>.
                </td>
              </tr>
              <tr>
                <td>
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.log.1', token='')}><kbd class="link">nowcast.log.1</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.debug.log.1', token='')}><kbd class="link">nowcast.debug.log.1</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='checklist.log.1', token='')}><kbd class="link">checklist.log.1</kbd></a>
                </td>
                <td>
                  Previous log files.
                  Roll over to
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.log.2', token='')}><kbd class="link">nowcast.log.2</kbd></a>,
                  <a href="${request.route_url('nowcast.logs', filename='nowcast.debug.log.2', token='')}"><kbd class="link">nowcast.debug.log.2</kbd></a>,
                  and <a href=${request.route_url('nowcast.logs', filename='checklist.log.2', token='')}><kbd class="link">checklist.log.2</kbd></a>
                  when <kbd>nowcast.log</kbd> rolls over to <kbd>nowcast.log.1</kbd>.
                </td>
              </tr>
              <tr>
                <td colspan="2">
                  Older log files:
                </td>
              </tr>
              <tr>
                <td colspan="2">
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.log.2', token='')}><kbd class="link">nowcast.log.2</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.debug.log.2', token='')}><kbd class="link">nowcast.debug.log.2</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='checklist.log.2', token='')}><kbd class="link">checklist.log.2</kbd></a>
                </td>
              </tr>
              <tr>
                <td colspan="2">
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.log.3', token='')}><kbd class="link">nowcast.log.3</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.debug.log.3', token='')}><kbd class="link">nowcast.debug.log.3</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='checklist.log.3', token='')}><kbd class="link">checklist.log.3</kbd></a>
                </td>
              </tr>
              <tr>
                <td colspan="2">
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.log.4', token='')}><kbd class="link">nowcast.log.4</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.debug.log.4', token='')}><kbd class="link">nowcast.debug.log.4</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='checklist.log.4', token='')}><kbd class="link">checklist.log.4</kbd></a>
                </td>
              </tr>
              <tr>
                <td colspan="2">
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.log.5', token='')}><kbd class="link">nowcast.log.5</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.debug.log.5', token='')}><kbd class="link">nowcast.debug.log.5</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='checklist.log.5', token='')}><kbd class="link">checklist.log.5</kbd></a>
                </td>
              </tr>
              <tr>
                <td colspan="2">
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.log.6', token='')}><kbd class="link">nowcast.log.6</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.debug.log.6', token='')}><kbd class="link">nowcast.debug.log.6</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='checklist.log.6', token='')}><kbd class="link">checklist.log.6</kbd></a>
                </td>
              </tr>
              <tr>
                <td colspan="2">
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.log.7', token='')}><kbd class="link">nowcast.log.7</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='nowcast.debug.log.7', token='')}><kbd class="link">nowcast.debug.log.7</kbd></a>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                  <a href=${request.route_url('nowcast.logs', filename='checklist.log.7', token='')}><kbd class="link">checklist.log.7</kbd></a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <h2 id="grib_to_netcdf-image">grib_to_netcdf Worker Monitoring Plots</h2>
      <img class="img-responsive"
        src="${request.static_url(grib_to_netcdf_png)}"
        alt="Weather forcing dataset monitoring plots">

      <h2 id="get_NeahBay_ssh-image">get_NeahBay_ssh Worker Monitoring Plots</h2>
      <img class="img-responsive"
        src="${request.static_url(get_NeahBay_ssh_png)}"
        alt="Juan de Fuca Strait sea surface height forcing dataset observations and forecast plot">
    </div>
  </div>
</div>
