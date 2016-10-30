# Copyright 2013-2016 The Salish Sea MEOPAR Contributors
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

"""salishsea_site views
"""
import logging
import os
from pathlib import Path

import arrow
from pyramid.httpexceptions import HTTPNotFound
from pyramid.static import static_view
from pyramid.view import view_config


logger = logging.getLogger(__name__)


static_page = static_view(
    '/var/www/html', use_subpath=True, cache_max_age=3600)


@view_config(route_name='nowcast.logs', renderer='string')
def nowcast_logs(request):
    """Render the requested file from the :envvar:`NOWCAST_LOGS` directory
    as text.
    """
    try:
        logs_dir = Path(os.environ['NOWCAST_LOGS'])
    except KeyError:
        logger.warning('NOWCAST_LOGS environment variable is not set')
        raise HTTPNotFound
    try:
        return (logs_dir/request.matchdict['filename']).open().read()
    except FileNotFoundError as e:
        logger.debug(e)
        raise HTTPNotFound


@view_config(route_name='results.nowcast.publish', renderer='publish.mako')
def nowcast_publish(request):
    run_date = arrow.get(request.matchdict['run_date'], 'DDMMMYY')
    return {
        'run_type': 'nowcast',
        'run_date': run_date,
        'results_date': run_date,
        'plot_title': 'Marine and Atmospheric Conditions - Storm Surge Alerts',
        'svg_file': 'Threshold_website',
    }


@view_config(route_name='about.contributors', renderer='contributors.mako')
@view_config(route_name='about.contributors.html', renderer='contributors.mako')
def contributors(request):
    return {}
