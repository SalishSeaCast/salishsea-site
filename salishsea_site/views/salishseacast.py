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

"""salishsea_site SalishSeaCast views
"""
import logging
import os
from pathlib import Path

import arrow
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config


logger = logging.getLogger(__name__)


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
        return (logs_dir / request.matchdict['filename']).open().read()
    except FileNotFoundError as e:
        logger.debug(e)
        raise HTTPNotFound


@view_config(route_name='results.nowcast.publish', renderer='publish.mako')
def nowcast_publish(request):
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    return {
        'run_type': 'nowcast',
        'run_date': results_date,
        'results_date': results_date,
        'plot_title': 'Marine and Atmospheric Conditions - Storm Surge Alerts',
        'svg_file': 'Threshold_website',
    }


@view_config(route_name='results.forecast.publish', renderer='publish.mako')
def forecast_publish(request):
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    return {
        'run_type': 'forecast',
        'run_date': results_date.replace(days=-1),
        'results_date': results_date,
        'plot_title': 'Marine and Atmospheric Conditions - Storm Surge Alerts',
        'svg_file': 'Threshold_website',
    }


@view_config(route_name='results.forecast2.publish', renderer='publish.mako')
def forecast2_publish(request):
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    return {
        'run_type': 'forecast2',
        'run_date': results_date.replace(days=-2),
        'results_date': results_date,
        'plot_title': 'Marine and Atmospheric Conditions - Storm Surge Alerts',
        'svg_file': 'Threshold_website',
    }
