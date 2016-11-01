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

<%block name="title">${results_date.format('dddd, D MMMM YYYY')} – Salish Sea Storm Surge ${run_type.title()}</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1 id="top">${results_date.format('dddd, D MMMM YYYY')} – Salish Sea Storm Surge ${run_type.title()}</h1>

      <h3 id="${plot_title | slug}"> ${plot_title} ${header_link(plot_title)} </h3>
      <img class="img-responsive"
        src="${request.static_url(
                '/results/nowcast-sys/figures/{run_type}/{run_dmy}/{svg_file}_{run_dmy}.svg'
                .format(run_type=run_type, svg_file=svg_file, run_dmy=run_date.format('DDMMMYY').lower()))}"
        alt="${plot_title} image">
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
</div>


<%def name="header_link(title)">\
  <a class="header-link" href="#${title | slug}"
     title="Link to this heading">
    <span class="fa fa-link fa-flip-horizontal" aria-hidden="true"></span>
  </a>
</%def>
