# Copyright 2013-2017 The Salish Sea MEOPAR Contributors
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


@attr.s
class FigureMetadata:
    #: Figure title that appears on rendered page.
    title = attr.ib()
    #: SVG file name of figure, excluding date part and .svg extension.
    #: So, if the file name is Vic_maxSSH_05nov16.svg, the svg_name value
    #: is Vic_maxSSH.
    svg_name = attr.ib()
    #: Text to appear in list of choices for figure in group of figures.
    #: Clicking on this text will swap this figure into the figure group
    #: display elements.
    link_text = attr.ib(default='')

    FIG_DIR_TMPL = '/results/nowcast-sys/figures/{run_type}/{run_dmy}/'

    def available(self, request, run_type, run_date, session):
        """Return a boolean indicating whether or not the figure is available
        on the static file server that provides figure files.

        :param request: HTTP request.
        :type request: :py:class:`pyramid.request.Request`

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param session: Requests session object to re-use server connection,
                        if possible.
        :type session: :py:class:`requests.Session`

        :return: Figure is availability on the static figure file server.
        :rtype: boolean
        """
        figure_url = request.static_url(self.path(run_type, run_date))
        try:
            return session.head(figure_url).status_code == 200
        except requests.ConnectionError:
            # Development environment
            dev_figure_url = figure_url.replace('4567', '6543')
            return session.head(dev_figure_url).status_code == 200

    def filename(self, run_dmy):
        """Return the figure file name.

        :param str run_dmy: Run date for which the figure was generated,
                            formatted like `06jul17`.

        :returns: Figure file name.
        :rtype: str
        """
        return '{svg_name}_{run_dmy}.svg'.format(
            svg_name=self.svg_name, run_dmy=run_dmy
        )

    def path(self, run_type, run_date):
        """Return the figure file path.

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :return: Figure file path.
        :rtype: str
        """
        run_dmy = run_date.format('DDMMMYY').lower()
        fig_dir = self.FIG_DIR_TMPL.format(
            run_type=run_type, svg_name=self.svg_name, run_dmy=run_dmy
        )
        return os.path.join(fig_dir, self.filename(run_dmy))


@attr.s
class FigureGroup:
    #: Figure group description.
    #: Used in the list of plots to link to the figure group section of the
    #: page.
    #: Also used as the heading text for the figure links list,
    #: and as the basis for the figure group permalink slug.
    description = attr.ib()
    #:
    figures = attr.ib(default=[])

    def __iter__(self):
        return (figure for figure in self.figures)

    def available(self, request, run_type, run_date, session):
        """Return a boolean indicating whether or not the figure is available
        on the static file server that provides figure files.

        :param request: HTTP request.
        :type request: :py:class:`pyramid.request.Request`

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param session: Requests session object to re-use server connection,
                        if possible.
        :type session: :py:class:`requests.Session`

        :return: Figure is availability on the static figure file server.
        :rtype: list
        """
        return [
            figure.available(request, run_type, run_date, session)
            for figure in self.figures
        ]


@attr.s
class ImageLoop:
    #: :py:class:`~salishsea_site.views.salishseacast.FigureMetaData` instance
    #: that describes the image loop figures.
    metadata = attr.ib()
    #: Typical number of images to be displayed in the loop.
    nominal_image_count = attr.ib(default=24)

    @property
    def title(self):
        return self.metadata.title

    def __iter__(self):
        return (self for i in range(1))

    def available(self, request, run_type, run_date, session):
        """Return a list of run hours for which image loop figures are
        available on the static file server that provides figure files.

        :param request: HTTP request.
        :type request: :py:class:`pyramid.request.Request`

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param session: Requests session object to re-use server connection,
                        if possible.
        :type session: :py:class:`requests.Session`

        :return: Run hours for which figures are available on the
                 static figure file server.
        :rtype: list of ints
        """
        available_hrs = []
        for run_hr in range(self.nominal_image_count):
            path = self.path(run_type, run_date, run_hr)
            try:
                if session.head(request.static_url(path)).status_code == 200:
                    available_hrs.append(run_hr)
            except requests.ConnectionError:
                # Development environment
                url = request.static_url(path).replace('4567', '6543')
                if session.head(url).status_code == 200:
                    available_hrs.append(run_hr)
        return available_hrs

    def filename(self, run_date, run_hr):
        """Return the figure file name.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param int run_hr: Run hour for which the figure was generated.

        :returns: Figure file name.
        :rtype: str
        """
        return '{svg_name}_{run_yyyymmdd}_{run_hr:02d}3000_UTC.png'.format(
            svg_name=self.metadata.svg_name,
            run_yyyymmdd=run_date.format('YYYYMMDD'),
            run_hr=run_hr,
        )

    def path(self, run_type, run_date, run_hr):
        """Return the figure file path.

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param int run_hr: Run hour for which the figure was generated.

        :return: Figure file path.
        :rtype: str
        """
        run_dmy = run_date.format('DDMMMYY').lower()
        fig_dir = self.metadata.FIG_DIR_TMPL.format(
            run_type=run_type,
            svg_name=self.metadata.svg_name,
            run_dmy=run_dmy
        )
        return os.path.join(fig_dir, self.filename(run_date, run_hr))


publish_figures = [
    FigureMetadata(
        title='Marine and Atmospheric Conditions - Storm Surge Alerts',
        svg_name='Threshold_website'
    ),
    FigureMetadata(
        title='Tidal Predictions for Point Atkinson',
        svg_name='PA_tidal_predictions'
    ),
]

publish_tides_max_ssh_figure_group = FigureGroup(
    description='Tide Gauge Station Sea Surface Heights',
    figures=[
        FigureMetadata(
            title='Neah Bay Sea Surface Height',
            link_text='Neah Bay',
            svg_name='NB_maxSSH'
        ),
        FigureMetadata(
            title='Victoria Sea Surface Height',
            link_text='Victoria',
            svg_name='Vic_maxSSH'
        ),
        FigureMetadata(
            title='Cherry Point Sea Surface Height',
            link_text='Cherry Point',
            svg_name='CP_maxSSH'
        ),
        FigureMetadata(
            title='Point Atkinson Sea Surface Height',
            link_text='Point Atkinson',
            svg_name='PA_maxSSH'
        ),
        FigureMetadata(
            title='Nanaimo Sea Surface Height',
            link_text='Nanaimo',
            svg_name='Nan_maxSSH'
        ),
        FigureMetadata(
            title='Campbell River Sea Surface Height',
            link_text='Campbell River',
            svg_name='CR_maxSSH'
        ),
    ]
)

publish_wind_figure_group = FigureGroup(
    description='Modelled and Observed Winds',
    figures=[
        FigureMetadata(
            title='Sand Heads Wind',
            link_text='Sand Heads',
            svg_name='SH_wind'
        ),
        FigureMetadata(
            title='Winds from Atmospheric Forcing Averaged Over Run Duration',
            link_text='Averaged Over Run Duration',
            svg_name='Avg_wind_vectors'
        ),
        FigureMetadata(
            title='Instantaneous Winds from Atmospheric Forcing',
            link_text='Instantaneous at Pt. Atkinson High Water Time',
            svg_name='Wind_vectors_at_max'
        ),
    ]
)

salinity_image_loop = ImageLoop(
    metadata=FigureMetadata(
        title='Salinity Fields Along Thalweg and on Surface',
        svg_name='salinity_thalweg_and_surface',
    )
)

temperature_image_loop = ImageLoop(
    metadata=FigureMetadata(
        title='Temperature Fields Along Thalweg and on Surface',
        svg_name='temperature_thalweg_and_surface',
    )
)

currents_physics_figures = [
    FigureMetadata(
        title='Surface Salinity, Temperature and Currents',
        svg_name='T_S_Currents_on_surface'
    ),
    FigureMetadata(
        title='Model Currents at ONC VENUS East Node',
        svg_name='Currents_at_VENUS_East'
    ),
    FigureMetadata(
        title='Model Currents at ONC VENUS Central Node',
        svg_name='Currents_at_VENUS_Central'
    ),
]

nitrate_image_loop = ImageLoop(
    metadata=FigureMetadata(
        title='Nitrate Fields Along Thalweg and on Surface',
        svg_name='nitrate_thalweg_and_surface',
    )
)

timeseries_figure_group = FigureGroup(
    description='nowcast-green Time Series',
    figures=[
        FigureMetadata(
            title='Temperature and Salinity',
            link_text='Temperature and Salinity',
            svg_name='temperature_salinity_timeseries',
        ),
        FigureMetadata(
            title='Nitrate and Diatom Concentrations',
            link_text='Nitrate and Diatom Concentrations',
            svg_name='nitrate_diatoms_timeseries',
        ),
        FigureMetadata(
            title='Mesodinium rubrum and Flagellates Concentrations',
            link_text='Mesodinium rubrum and Flagellates Concentrations',
            svg_name='mesodinium_flagellates_timeseries',
        ),
        FigureMetadata(
            title='Mesozooplankton and Microzooplankton Concentrations',
            link_text='Mesozooplankton and Microzooplankton Concentrations',
            svg_name='mesozoo_microzoo_timeseries',
        ),
    ]
)

comparison_figures = [
    FigureMetadata(
        title='Modeled and Observed Winds at Sand Heads', svg_name='SH_wind'
    ),
    FigureMetadata(
        title=(
            'Modeled and Observed Surface Salinity '
            'Along Horseshoe Bay-Departure Bay Ferry Route'
        ),
        svg_name='HB_DB_ferry_salinity'
    ),
    FigureMetadata(
        title=(
            'Modeled and Observed Surface Salinity '
            'Along Tsawwassen-Duke Pt. Ferry Route'
        ),
        svg_name='TW_DP_ferry_salinity'
    ),
    FigureMetadata(
        title=(
            'Modeled and Observed Surface Salinity '
            'Along Tsawwassen-Schwartz Bay Ferry Route'
        ),
        svg_name='TW_SB_ferry_salinity'
    ),
]
onc_venus_comparison_figure_group = FigureGroup(
    description='Salinity and Temperature at ONC VENUS Nodes',
    figures=[
        FigureMetadata(
            title='Salinity and Temperature at ONC VENUS Central Node',
            link_text='Central Node',
            svg_name='Compare_VENUS_Central'
        ),
        FigureMetadata(
            title='Salinity and Temperature at ONC VENUS East Node',
            link_text='East Node',
            svg_name='Compare_VENUS_East'
        ),
        FigureMetadata(
            title='Salinity and Temperature at ONC VENUS Delta BBL Node',
            link_text='BBL Node',
            svg_name='Compare_VENUS_Delta_BBL'
        ),
        FigureMetadata(
            title='Salinity and Temperature at ONC VENUS Delta DDL Node',
            link_text='DDL Node',
            svg_name='Compare_VENUS_Delta_DDL'
        ),
    ]
)


@view_config(
    route_name='storm_surge.portal', renderer='storm_surge/portal.mako'
)
# Legacy route
@view_config(
    route_name='storm_surge.index.html', renderer='storm_surge/portal.mako'
)
def storm_surge_portal(request):
    """Render storm surge portal page.
    """
    return {}


@view_config(
    route_name='storm_surge.forecast', renderer='salishseacast/publish.mako'
)
# Legacy route
@view_config(
    route_name='storm_surge.forecast.html',
    renderer='salishseacast/publish.mako'
)
def storm_surge_forecast(request):
    """Render storm surge forecast page that shows most recent forecast or
    forecast2 results figures.
    """
    fcst_date = arrow.now().floor('day').replace(days=+1)
    try:
        try:
            return _data_for_publish_template(
                request,
                'forecast',
                fcst_date,
                publish_figures,
                publish_tides_max_ssh_figure_group,
                publish_wind_figure_group,
                fcst_date.replace(days=-1)
            )
        except HTTPNotFound:
            return _data_for_publish_template(
                request,
                'forecast2',
                fcst_date,
                publish_figures,
                publish_tides_max_ssh_figure_group,
                publish_wind_figure_group,
                fcst_date.replace(days=-2)
            )
    except HTTPNotFound:
        return _data_for_publish_template(
            request,
            'forecast',
            fcst_date.replace(days=-1),
            publish_figures,
            publish_tides_max_ssh_figure_group,
            publish_wind_figure_group,
            fcst_date.replace(days=-2)
        )


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
    route_name='salishseacast.about', renderer='salishseacast/about.mako'
)
# Legacy route
@view_config(
    route_name='nemo.index.html', renderer='salishseacast/about.mako'
)
def about(request):
    return {}


@view_config(
    route_name='results.index', renderer='salishseacast/results_index.mako'
)
# Legacy route
@view_config(
    route_name='results.index.html',
    renderer='salishseacast/results_index.mako'
)
def results_index(request):
    """Render results calendar grid index page.
    """
    INDEX_GRID_COLS = 21
    # Calculate the date range to display in the grid and the number of
    # columns for the month headings of the grid
    fcst_date = arrow.now().floor('day').replace(days=+1)
    dates = arrow.Arrow.range(
        'day', fcst_date.replace(days=-(INDEX_GRID_COLS - 1)), fcst_date
    )
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
        ('nowcast currents', 'nowcast', currents_physics_figures, 'currents'),
        ('nowcast biology', 'nowcast-green', nitrate_image_loop, 'biology'),
        (
            'nowcast timeseries', 'nowcast-green', timeseries_figure_group,
            'timeseries'
        ),
        ('nowcast comparison', 'nowcast', comparison_figures, 'comparison'),
    )
    with requests.Session() as session:
        grid_dates = {
            row: _exclude_missing_dates(
                request, dates, figures, figs_type, run_type, session
            )
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
    request, dates, figures, figs_type, run_type, session
):
    run_date_offsets = {'nowcast': 0, 'forecast': -1, 'forecast2': -2}
    if figs_type == 'publish':
        return ((
            d if figures[0].available(
                request,
                run_type,
                d.replace(days=run_date_offsets[run_type]),
                session
            ) else None
        ) for d in dates)
    else:
        return ((
            d if any(
                fig.available(request, run_type, d, session) for fig in figures
            ) else None
        ) for d in dates)


@view_config(
    route_name='results.nowcast.publish',
    renderer='salishseacast/publish.mako'
)
# Legacy route
@view_config(
    route_name='results.nowcast.publish.html',
    renderer='salishseacast/publish.mako'
)
def nowcast_publish(request):
    """Render storm surge nowcast figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    return _data_for_publish_template(
        request,
        'nowcast',
        results_date,
        publish_figures,
        publish_tides_max_ssh_figure_group,
        publish_wind_figure_group,
        run_date=results_date
    )


@view_config(
    route_name='results.forecast.publish',
    renderer='salishseacast/publish.mako'
)
# Legacy route
@view_config(
    route_name='results.forecast.publish.html',
    renderer='salishseacast/publish.mako'
)
def forecast_publish(request):
    """Render storm surge forecast figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    run_date = results_date.replace(days=-1)
    return _data_for_publish_template(
        request, 'forecast', results_date, publish_figures,
        publish_tides_max_ssh_figure_group, publish_wind_figure_group, run_date
    )


@view_config(
    route_name='results.forecast2.publish',
    renderer='salishseacast/publish.mako'
)
# Legacy route
@view_config(
    route_name='results.forecast2.publish.html',
    renderer='salishseacast/publish.mako'
)
def forecast2_publish(request):
    """Render preliminary storm surge forecast figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    run_date = results_date.replace(days=-2)
    return _data_for_publish_template(
        request, 'forecast2', results_date, publish_figures,
        publish_tides_max_ssh_figure_group, publish_wind_figure_group, run_date
    )


@view_config(
    route_name='results.nowcast.currents',
    renderer='salishseacast/currents.mako'
)
# Legacy routes
@view_config(
    route_name='results.nowcast.research',
    renderer='salishseacast/currents.mako'
)
@view_config(
    route_name='results.nowcast.research.html',
    renderer='salishseacast/currents.mako'
)
def nowcast_currents_physics(request):
    """Render model research currents and physics evaluation results figures 
    page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    with requests.Session() as session:
        available_figures = [
            fig for fig in currents_physics_figures
            if fig.available(request, 'nowcast', results_date, session)
        ]
        salinity_available_hrs = (
            salinity_image_loop.available(
                request, 'nowcast', results_date, session
            )
        )
        temperature_available_hrs = (
            temperature_image_loop.available(
                request, 'nowcast', results_date, session
            )
        )
    all_available_figures = (
        available_figures + salinity_available_hrs + temperature_available_hrs
    )
    if not any(all_available_figures):
        raise HTTPNotFound
    figure_links = [salinity_image_loop.title
                    ] if salinity_available_hrs else []
    if temperature_available_hrs:
        figure_links.append(temperature_image_loop.title)
    figure_links.extend(figure.title for figure in available_figures)
    return {
        'results_date': results_date,
        'run_type': 'nowcast',
        'run_date': results_date,
        'figure_links': figure_links,
        'figures': available_figures,
        'salinity_image_loop': salinity_image_loop,
        'salinity_image_loop_hrs': salinity_available_hrs,
        'temperature_image_loop': temperature_image_loop,
        'temperature_image_loop_hrs': temperature_available_hrs,
    }


@view_config(
    route_name='results.nowcast.biology',
    renderer='salishseacast/biology.mako'
)
def nowcast_biology(request):
    """Render model research biology evaluation results figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    with requests.Session() as session:
        available_hrs = (
            nitrate_image_loop.available(
                request, 'nowcast-green', results_date, session
            )
        )
    if not available_hrs:
        raise HTTPNotFound
    return {
        'results_date': results_date,
        'run_type': 'nowcast-green',
        'run_date': results_date,
        'nitrate_image_loop': nitrate_image_loop,
        'image_loop_hrs': available_hrs,
    }


@view_config(
    route_name='results.nowcast.timeseries',
    renderer='salishseacast/timeseries.mako'
)
def nowcast_timeseries(request):
    """Render model research timeseries evaluation results figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    with requests.Session() as session:
        available_figures = (
            timeseries_figure_group.available(
                request, 'nowcast-green', results_date, session
            )
        )
    if not available_figures:
        raise HTTPNotFound
    return {
        'results_date': results_date,
        'run_type': 'nowcast-green',
        'run_date': results_date,
        'figures': timeseries_figure_group,
    }


@view_config(
    route_name='results.nowcast.comparison',
    renderer='salishseacast/comparison.mako'
)
# Legacy route
@view_config(
    route_name='results.nowcast.comparison.html',
    renderer='salishseacast/comparison.mako'
)
def nowcast_comparison(request):
    """Render model and observation comparisons figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    with requests.Session() as session:
        ungrouped_figures = [
            fig for fig in comparison_figures
            if fig.available(request, 'nowcast', results_date, session)
        ]
        onc_venus_figures_available = any(
            onc_venus_comparison_figure_group.available(
                request, 'nowcast', results_date, session
            )
        )
    if not ungrouped_figures and not onc_venus_figures_available:
        raise HTTPNotFound
    figure_links = [figure.title for figure in ungrouped_figures]
    if onc_venus_figures_available:
        figure_links.append(onc_venus_comparison_figure_group.description)
    return {
        'results_date': results_date,
        'run_type': 'nowcast',
        'run_date': results_date,
        'figure_links': figure_links,
        'figures': ungrouped_figures,
        'onc_venus_figures_available': onc_venus_figures_available,
        'onc_venus_figures': onc_venus_comparison_figure_group,
    }


def _data_for_publish_template(
    request, run_type, results_date, figures, tides_max_ssh_figure_group,
    wind_figure_group, run_date
):
    """Calculate template variable values for a storm surge forecast figures
    page.
    :param publish_noaa_ssh_figure:
    :param wind_figure_group:
    :param tides_max_ssh_figure_group:
    """
    run_type_titles = {
        'nowcast': 'Nowcast',
        'forecast': 'Forecast',
        'forecast2': 'Preliminary Forecast',
    }
    with requests.Session() as session:
        storm_surge_alerts_fig_ready = publish_figures[0].available(
            request, run_type, run_date, session
        )
        if not storm_surge_alerts_fig_ready:
            raise HTTPNotFound
        available_figures = [
            fig for fig in figures
            if fig.available(request, run_type, run_date, session)
        ]
        tides_max_ssh_figures_available = any(
            tides_max_ssh_figure_group.available(
                request, run_type, run_date, session
            )
        )
        wind_figures_available = any(
            wind_figure_group.available(request, run_type, run_date, session)
        )
    figure_links = [figure.title for figure in available_figures]
    template_data = {
        'results_date': results_date,
        'run_type_title': run_type_titles[run_type],
        'run_type': run_type,
        'run_date': run_date,
        'figure_links': figure_links,
        'figures': available_figures,
    }
    if tides_max_ssh_figures_available:
        figure_links.append(tides_max_ssh_figure_group.description)
        template_data['tides_max_ssh_figures_available'
                      ] = tides_max_ssh_figures_available
        template_data['tides_max_ssh_figures'] = tides_max_ssh_figure_group
    if wind_figures_available:
        figure_links.append(wind_figure_group.description)
        template_data['wind_figures_available'] = wind_figures_available
        template_data['wind_figures'] = wind_figure_group
    return template_data


@view_config(
    route_name='nowcast.monitoring',
    renderer='salishseacast/nowcast_monitoring.mako'
)
def nowcast_monitoring(request):
    return {
        'grib_to_netcdf_png': '/results/nowcast-sys/figures/monitoring/wg.png',
        'get_NeahBay_ssh_png':
        '/results/nowcast-sys/figures/monitoring/NBssh.png',
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
