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
import attr
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config


logger = logging.getLogger(__name__)


@attr.s
class FigureMetadata:
    title = attr.ib()
    svg_name = attr.ib()

    def file_available(self, run_type, run_date, path_prefix):
        run_dmy = run_date.format('DDMMMYY').lower()
        fig_path = Path(
            path_prefix, run_type, run_dmy,
            '{0.svg_name}_{run_dmy}.svg'.format(self, run_dmy=run_dmy))
        return fig_path.exists()


publish_figures = [
    FigureMetadata(
        title='Marine and Atmospheric Conditions - Storm Surge Alerts',
        svg_name='Threshold_website'),
    FigureMetadata(
        title='Tidal Predictions for Point Atkinson',
        svg_name='PA_tidal_predictions'),
]


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
    storm_surge_alerts_fig_ready = publish_figures[0].file_available(
        'nowcast', results_date, '/results/nowcast-sys/figures')
    if not storm_surge_alerts_fig_ready:
        raise HTTPNotFound
    return _template_data_publish(
        'nowcast', results_date, publish_figures, run_date=results_date)


@view_config(route_name='results.forecast.publish', renderer='publish.mako')
def forecast_publish(request):
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    run_date = results_date.replace(days=-1)
    storm_surge_alerts_fig_ready = publish_figures[0].file_available(
        'nowcast', run_date, '/results/nowcast-sys/figures')
    if not storm_surge_alerts_fig_ready:
        raise HTTPNotFound
    return _template_data_publish(
        'forecast', results_date, publish_figures, run_date)


@view_config(route_name='results.forecast2.publish', renderer='publish.mako')
def forecast2_publish(request):
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    run_date = results_date.replace(days=-2)
    storm_surge_alerts_fig_ready = publish_figures[0].file_available(
        'nowcast', run_date, '/results/nowcast-sys/figures')
    if not storm_surge_alerts_fig_ready:
        raise HTTPNotFound
    return _template_data_publish(
        'nowcast', results_date, publish_figures, run_date)


def _template_data_publish(run_type, results_date, figures, run_date):
    return {
        'run_type': run_type,
        'run_date': run_date,
        'results_date': results_date,
        'figures': figures,
    }
