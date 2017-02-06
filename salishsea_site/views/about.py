# Copyright 2013-2016 The Salish Sea MEOPAR Contributors
# and The University of British Columbia

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""salishsea_site About views
"""
import logging
from pathlib import Path

from pyramid.view import view_config

logger = logging.getLogger(__name__)


@view_config(
    route_name='about.contributors', renderer='about/contributors.mako'
)
@view_config(
    route_name='about.contributors.html', renderer='about/contributors.mako'
)
def contributors(request):
    return {}


@view_config(route_name='about.license', renderer='about/license.mako')
@view_config(route_name='about.license.html', renderer='about/license.mako')
def license(request):
    with Path(request.registry.settings['license_file']).open('rt') as f:
        return {'license': f.read()}
