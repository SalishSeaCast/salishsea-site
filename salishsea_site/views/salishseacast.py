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
import requests


logger = logging.getLogger(__name__)

FIG_FILE_TMPL = (
    '/results/nowcast-sys/figures/{run_type}/{run_dmy}/{svg_name}_{run_dmy}.svg'
)

@attr.s
class FigureMetadata:
    #: Figure title that appears on rendered page.
    title = attr.ib()
    #: SVG file name of figure, excluding date part and .svg extension.
    #: So, if the file name is Vic_maxSSH_05nov16.svg, the svg_name value
    #: is Vic_maxSSH.
    svg_name = attr.ib()

    def available(self, request, run_type, run_date, session):
        """Return a boolean indicating whether or not the figure is available
        on the static file server that provides figure files.

        :param request: HTTP request.
        :type request: :py:class:`pyramid.request.Request`

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date:

        :param session: Requests session object to re-use server connection,
                        if possible.
        :type session: :py:class:`requests.Session`

        :return: Figure is availability on the static figure file server.
        :rtype: boolean
        """
        path = FIG_FILE_TMPL.format(run_type=run_type,
            svg_name=self.svg_name, run_dmy=run_date.format('DDMMMYY').lower())
        figure_url = request.static_url(
            path)
        try:
            return session.head(figure_url).status_code == 200
        except requests.ConnectionError:
            # Development environment
            return session.head(
                figure_url.replace('4567', '6543')).status_code == 200


publish_figures = [
    FigureMetadata(
        title='Marine and Atmospheric Conditions - Storm Surge Alerts',
        svg_name='Threshold_website'),
    FigureMetadata(
        title='Tidal Predictions for Point Atkinson',
        svg_name='PA_tidal_predictions'),
    FigureMetadata(
        title='Victoria Sea Surface Height',
        svg_name='Vic_maxSSH'),
    FigureMetadata(
        title='Cherry Point Sea Surface Height',
        svg_name='CP_maxSSH'),
    FigureMetadata(
        title='Point Atkinson Sea Surface Height',
        svg_name='PA_maxSSH'),
    FigureMetadata(
        title='Nanaimo Sea Surface Height',
        svg_name='Nan_maxSSH'),
    FigureMetadata(
        title='Campbell River Sea Surface Height',
        svg_name='CR_maxSSH'),
    FigureMetadata(
        title='Sea Surface Height at Selected NOAA Stations',
        svg_name='NOAA_ssh'),
    FigureMetadata(
        title='Storm Surge Alert Thresholds',
        svg_name='WaterLevel_Thresholds'),
    FigureMetadata(
        title='Sandheads Wind',
        svg_name='SH_wind'),
    FigureMetadata(
        title='Winds from Atmospheric Forcing Averaged Over Run Duration',
        svg_name='Avg_wind_vectors'),
    FigureMetadata(
        title='Instantaneous Winds from Atmospheric Forcing',
        svg_name='Wind_vectors_at_max'),
]

research_figures = [
    FigureMetadata(
        title='Salinity Field Along Thalweg',
        svg_name='Salinity_on_thalweg'),
    FigureMetadata(
        title='Temperature Field Along Thalweg',
        svg_name='Temperature_on_thalweg'),
    FigureMetadata(
        title='Surface Salinity, Temperature and Currents',
        svg_name='T_S_Currents_on_surface'),
    FigureMetadata(
        title='Model Currents at ONC VENUS East Node',
        svg_name='Currents_at_VENUS_East'),
    FigureMetadata(
        title='Model Currents at ONC VENUS Central Node',
        svg_name='Currents_at_VENUS_Central'),
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
@view_config(
    route_name='results.nowcast.publish.html', renderer='publish.mako')
def nowcast_publish(request):
    """Render storm surge nowcast figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    return _data_for_publish_template(
        request, 'nowcast', results_date, publish_figures,
        run_date=results_date)


@view_config(route_name='results.forecast.publish', renderer='publish.mako')
@view_config(
    route_name='results.forecast.publish.html', renderer='publish.mako')
def forecast_publish(request):
    """Render storm surge forecast figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    run_date = results_date.replace(days=-1)
    return _data_for_publish_template(
        request, 'forecast', results_date, publish_figures, run_date)


@view_config(route_name='results.forecast2.publish', renderer='publish.mako')
@view_config(
    route_name='results.forecast2.publish.html', renderer='publish.mako')
def forecast2_publish(request):
    """Render preliminary storm surge forecast figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    run_date = results_date.replace(days=-2)
    return _data_for_publish_template(
        request, 'forecast2', results_date, publish_figures, run_date)


@view_config(route_name='results.nowcast.research', renderer='research.mako')
@view_config(
    route_name='results.nowcast.research.html', renderer='research.mako')
def nowcast_research(request):
    """Render model research evaluation results figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    with requests.Session() as session:
        available_figures = [
            fig for fig in research_figures
            if fig.available(request, 'nowcast', results_date, session)]
    if not available_figures:
        raise HTTPNotFound
    return {
        'results_date': results_date,
        'run_type': 'nowcast',
        'run_date': results_date,
        'figures': available_figures,
        'FIG_FILE_TMPL': FIG_FILE_TMPL,
    }


def _data_for_publish_template(
    request, run_type, results_date, figures, run_date,
):
    """Calculate template variable values for a storm surge forecast figures
    page.
    """
    with requests.Session() as session:
        storm_surge_alerts_fig_ready = publish_figures[0].available(request,
            run_type, run_date, session)
        if not storm_surge_alerts_fig_ready:
            raise HTTPNotFound
        available_figures = [
            fig for fig in figures
            if fig.available(request, run_type, run_date, session)]
    run_type_titles = {
        'nowcast': 'Nowcast',
        'forecast': 'Forecast',
        'forecast2': 'Preliminary Forecast',
    }
    return {
        'results_date': results_date,
        'run_type_title': run_type_titles[run_type],
        'run_type': run_type,
        'run_date': run_date,
        'figures': available_figures,
        'FIG_FILE_TMPL': FIG_FILE_TMPL,
    }
