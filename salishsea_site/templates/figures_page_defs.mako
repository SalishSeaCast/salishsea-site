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


<%def name="header_link(title)">\
  <a class="header-link" href="#${title | slug}"
     title="Link to this heading">
    <span class="fa fa-link fa-flip-horizontal" aria-hidden="true"></span>
  </a>
</%def>


<%def name="list_of_plots(figures)">\
  <div class="row">
    <div class="col-md-12">
      <h2 id="${'List of Plots' | slug}">Plots ${header_link('List of Plots') | slug}</h2>
      <ul>
        %for figure in figures:
          <li><a href="#${figure.title | slug}">${figure.title}</a></li>
        %endfor
      </ul>
    </div>
  </div>
</%def>
