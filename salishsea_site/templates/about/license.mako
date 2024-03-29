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

<%block name="title">Salish Sea - License</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>License</h1>
      <p>
        The salishsea.eos.ubc.ca site content,
        build tools,
        and documentation are copyright 2013 – present by the Mesoscale Ocean and Atmospheric Dynamics (MOAD) group in the Department of Earth, Ocean, and Atmospheric Sciences at The University of British Columbia.
        Please see <a href=${request.route_url('about.contributors')}>Contributors</a> for details.
      </p>
      <p>
        They are licensed under the Apache License, Version 2.0.
        <a href="https://www.apache.org/licenses/LICENSE-2.0">https://www.apache.org/licenses/LICENSE-2.0</a>
      </p>
      <pre>${license}</pre>
    </div>
  </div>
</div>
