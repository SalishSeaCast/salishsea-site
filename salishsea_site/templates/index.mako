## Copyright 2013-2017 The Salish Sea MEOPAR Contributors
## and The University of British Columbia
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
    <div class="col-md-8 col-md-offset-2">
      <img class="img-responsive index"
        src="${request.static_url('salishsea_site:static/img/index.svg')}"
        alt="Salish Sea Oceanography Model Products">
    </div>
  </div>
</div>
