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


<%!
  from salishsea_site.mako_filters import slug
%>

<%inherit file="../site.mako"/>
<%namespace file="figures_page_defs.mako" import="figure_nav_links, figure_row, init_image_loop_group, image_loop_group, list_of_plots"/>

<%block name="title">Salish Sea Model Biology – ${results_date.format('DD-MMM-YYYY')}</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>Salish Sea Model Biology</h1>

      <h2>Evaluation Results from Nowcast</h2>

      <h2>${results_date.format('dddd, D MMMM YYYY')}</h2>

      <h2>Disclaimer</h2>
      <p>
        This page presents output from a research project.
        Results on this page are either:
      </p>
        <ol>
          <li>not yet evaluated, or</li>
          <li>have been evaluated but do not agree well with observations.</li>
        </ol>
      <p>
        For the latter we are working on model modifications.
      </p>

      <h2>References</h2>
      <ul>
        <li>
          Soontiens, N., Allen, S., Latornell, D., Le Souef, K., Machuca, I., Paquin, J.-P., Lu, Y., Thompson, K., Korabel, V. (2015).
          Storm surges in the Strait of Georgia simulated with a regional model.
          Atmosphere-Ocean volume 54, issue 1, pp 1-21.
          <a href="https://dx.doi.org/10.1080/07055900.2015.1108899" title="Link to paper via DOI">
            https://dx.doi.org/10.1080/07055900.2015.1108899
          </a>
        </li>
        <li>
          Soontiens, N. and Allen, S.
          Modelling sensitivities to mixing and advection in a sill-basin estuarine system.
          Ocean Modelling, volume 112, pp 17-32.
          <a href="https://dx.doi.org/10.1016/j.ocemod.2017.02.008" title="Link to paper via DOI">
            https://dx.doi.org/10.1016/j.ocemod.2017.02.008
          </a>
        </li>
      </ul>
    </div>
  </div>

  ${list_of_plots(figure_links)}

  %if available_figures['biology loops']:
    ${image_loop_group(image_loops)}
    ${figure_nav_links()}
  %endif

  %if available_figures['baynes sound']:
    %for figure in baynes_sound_figures:
      ${figure_row(figure, 'nowcast-agrif', run_date)}
      ${figure_nav_links()}
    %endfor
  %endif

  <%include file="data_sources.mako"/>
</div>


<%block name="page_js">
  <script src="${request.static_path("salishsea_site:static/js/ImageLoop.js")}"></script>
  ${init_image_loop_group(image_loops, run_type, run_date)}
</%block>
