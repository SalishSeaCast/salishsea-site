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

<%block name="title">${results_date.format('dddd, D MMMM YYYY')} – Salish Sea Storm Surge ${run_type.title()}</%block>

<h1 id="top">${results_date.format('dddd, D MMMM YYYY')} – Salish Sea Storm Surge ${run_type.title()}</h1>

<h3 id="${plot_title.replace(' ', '-').lower()}">
  ${plot_title}
  <a class="headerlink" href="#${plot_title.replace(' ', '-').lower()}" title="Permalink to this headline">¶</a>
</h3>
<img class="img-responsive"
  src="${request.static_url(
          '/results/nowcast-sys/figures/{run_type}/{run_dmy}/{svg_file}_{run_dmy}.svg'
          .format(run_type=run_type, svg_file=svg_file, run_dmy=run_date.format('DDMMMYY').lower()))}"
  alt="${plot_title} image">
