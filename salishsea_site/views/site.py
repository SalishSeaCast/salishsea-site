# Copyright 2014-2019 The Salish Sea MEOPAR Contributors
# and The University of British Columbia

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""salishsea_site index page view
"""
import logging

from pyramid.view import view_config

logger = logging.getLogger(__name__)


@view_config(route_name='site.index', renderer='index.mako')
@view_config(route_name='site.index.html', renderer='index.mako')
def index(request):
    """Render site index page.
    """
    return {}


@view_config(route_name='robots.txt', renderer='robots.mako')
def robots(request):
    """Render robots.txt page.
    """
    return {}
