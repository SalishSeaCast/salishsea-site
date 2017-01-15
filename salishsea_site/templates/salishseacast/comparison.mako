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
<%!
  from salishsea_site.mako_filters import slug
%>

<%inherit file="../site.mako"/>
<%namespace file="figures_page_defs.mako" import="header_link, list_of_plots, figure_row, figure_nav_links"/>

<%block name="title">
  Salish Sea Model and Observation Comparisons – ${results_date.format('DD-MMM-YYYY')}
</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>Salish Sea Model and Observation Comparisons from Nowcast</h1>

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
          Atmosphere-Ocean volume 54, issue 1.
          <a href="https://dx.doi.org/10.1080/07055900.2015.1108899" title="Link to paper via DOI">
            https://dx.doi.org/10.1080/07055900.2015.1108899
          </a>
        </li>
        <li>
          Soontiens, N. and Allen, S.
          Modelling sensitivities to mixing and advection in a sill-basin estuarine system.
          <em>Under revision for Ocean Modelling</em>.
        </li>
      </ul>
    </div>
  </div>

  ${list_of_plots(figures)}

  %for figure in figures:
    ${figure_row(figure, FIG_FILE_TMPL, run_type, run_date)}
    ${figure_nav_links()}
  %endfor

  <%include file="data_sources.mako"/>
</div>
