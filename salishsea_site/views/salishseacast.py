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
import requests
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

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
        path = FIG_FILE_TMPL.format(
            run_type=run_type,
            svg_name=self.svg_name, run_dmy=run_date.format('DDMMMYY').lower())
        figure_url = request.static_url(path)
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

comparison_figures = [
    FigureMetadata(
        title='Modeled and Observed Winds at Sandheads',
        svg_name='SH_wind'),
    FigureMetadata(
        title=(
            'Modeled and Observed Surface Salinity '
            'Along Horseshoe Bay-Departure Bay Ferry Route'),
        svg_name='HB_DB_ferry_salinity'),
    FigureMetadata(
        title=(
            'Modeled and Observed Surface Salinity '
            'Along Tsawwassen-Duke Pt. Ferry Route'),
        svg_name='TW_DP_ferry_salinity'),
    FigureMetadata(
        title=(
            'Modeled and Observed Surface Salinity '
            'Along Tsawwassen-Schwartz Bay Ferry Route'),
        svg_name='TW_SB_ferry_salinity'),
    FigureMetadata(
        title='Salinity and Temperature at ONC VENUS Central Node',
        svg_name='Compare_VENUS_Central'),
    FigureMetadata(
        title='Salinity and Temperature at ONC VENUS Delta BBL Node',
        svg_name='Compare_VENUS_Delta_BBL'),
    FigureMetadata(
        title='Salinity and Temperature at ONC VENUS Delta DDL Node',
        svg_name='Compare_VENUS_Delta_DDL'),
    FigureMetadata(
        title='Salinity and Temperature at ONC VENUS East Node',
        svg_name='Compare_VENUS_East'),
]


@view_config(
    route_name='storm_surge.portal', renderer='storm_surge_portal.mako')
@view_config(
    route_name='storm_surge.index.html', renderer='storm_surge_portal.mako')
def storm_surge_portal(request):
    """Render storm surge portal page.
    """
    return {}


@view_config(
    route_name='storm_surge.forecast', renderer='publish.mako')
@view_config(
    route_name='storm_surge.forecast.html', renderer='publish.mako')
def storm_surge_forecast(request):
    """Render storm surge forecast page that shows most recent forecast or
    forecast2 results figures.
    """
    fcst_date = arrow.now().floor('day').replace(days=+1)
    try:
        try:
            return _data_for_publish_template(
                request, 'forecast', fcst_date, publish_figures,
                fcst_date.replace(days=-1))
        except HTTPNotFound:
            return _data_for_publish_template(
                request, 'forecast2', fcst_date, publish_figures,
                fcst_date.replace(days=-2))
    except HTTPNotFound:
        return _data_for_publish_template(
            request, 'forecast', fcst_date.replace(days=-1), publish_figures,
            fcst_date.replace(days=-2))


@view_config(route_name='storm_surge.alert.feed', renderer='string')
def storm_surge_alert_feed(request):
    """Render the requested storm surge alert ATOM feed file.
    """
    introspector = request.registry.introspector
    figs_server = request.registry.settings['nowcast_figures_server_name']
    figs_path = introspector.get('static views', figs_server)['spec']
    feeds_path = Path(figs_path, 'storm-surge/atom')
    try:
        request.response.content_type = 'application/atom+xml'
        return (feeds_path / request.matchdict['filename']).open().read()
    except FileNotFoundError as e:
        logger.debug(e)
        raise HTTPNotFound


@view_config(
    route_name='salishseacast.about', renderer='about_salishseacast.mako')
@view_config(
    route_name='nemo.index.html', renderer='about_salishseacast.mako')
def about(request):
    return {}


@view_config(route_name='results.index', renderer='results_index.mako')
@view_config(route_name='results.index.html', renderer='results_index.mako')
def results_index(request):
    """Render results calendar grid index page.
    """
    INDEX_GRID_COLS = 21
    # Calculate the date range to display in the grid and the number of
    # columns for the month headings of the grid
    fcst_date = arrow.now().floor('day').replace(days=+1)
    dates = arrow.Arrow.range(
        'day', fcst_date.replace(days=-(INDEX_GRID_COLS - 1)), fcst_date)
    if dates[0].month != dates[-1].month:
        this_month_cols = dates[-1].day
        last_month_cols = INDEX_GRID_COLS - this_month_cols
    else:
        this_month_cols, last_month_cols = INDEX_GRID_COLS, 0
    # Replace dates for which there are no figures with None
    grid_rows = (
        # Calendar grid row key, run type, figures, figures type
        ('prelim forecast', 'forecast2', publish_figures, 'publish'),
        ('forecast', 'forecast', publish_figures, 'publish'),
        ('nowcast publish', 'nowcast', publish_figures, 'publish'),
        ('nowcast research', 'nowcast', research_figures, 'research'),
        ('nowcast comparison', 'nowcast', comparison_figures, 'comparison'),
    )
    with requests.Session() as session:
        grid_dates = {
            row: _exclude_missing_dates(
                request, dates, figures, figs_type, run_type, session)
            for row, run_type, figures, figs_type in grid_rows
        }
    return {
        'first_date': dates[0],
        'last_date': dates[-1],
        'this_month_cols': this_month_cols,
        'last_month_cols': last_month_cols,
        'grid_dates': grid_dates,
    }


def _exclude_missing_dates(
    request, dates, figures, figs_type, run_type, session,
):
    run_date_offsets = {
        'nowcast': 0,
        'forecast': -1,
        'forecast2': -2
    }
    if figs_type == 'publish':
        return (
            (d if figures[0].available(
                request, run_type,
                d.replace(days=run_date_offsets[run_type]), session) else None)
            for d in dates)
    else:
        return (
            (d if any(fig.available(
                request, run_type, d, session) for fig in figures) else None)
            for d in dates
        )


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


@view_config(
    route_name='results.nowcast.comparison', renderer='comparison.mako')
@view_config(
    route_name='results.nowcast.comparison.html', renderer='comparison.mako')
def nowcast_comparison(request):
    """Render model and observation comparisons figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    with requests.Session() as session:
        available_figures = [
            fig for fig in comparison_figures
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
        storm_surge_alerts_fig_ready = publish_figures[0].available(
            request, run_type, run_date, session)
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
