# Copyright 2014-2019 The Salish Sea MEOPAR Contributors
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
"""salishsea_site VHFR FVCOM results views
"""
import logging

import arrow
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from salishsea_site.views.figures import FigureMetadata, FigureGroup, ImageLoop, ImageLoopGroup

logger = logging.getLogger(__name__)

tide_stn_water_level_figure_group = FigureGroup(
    description='Tide Gauge Station Water Levels',
    figures=[
        FigureMetadata(
            title='Sandy Cove Water Level',
            link_text='Sandy Cove',
            svg_name='SC_waterlevel'
        ),
        FigureMetadata(
            title='Calamity Point Water Level',
            link_text='Calamity Point',
            svg_name='CP_waterlevel'
        ),
        FigureMetadata(
            title='Vancouver Harbour Water Level',
            link_text='Vancouver Harbour',
            svg_name='VH_waterlevel'
        ),
        FigureMetadata(
            title='Port Moody Water Level',
            link_text='Port Moody',
            svg_name='PM_waterlevel'
        ),
        FigureMetadata(
            title='Indian Arm Head Water Level',
            link_text='Indian Arm Head',
            svg_name='IAH_waterlevel'
        ),
        FigureMetadata(
            title='Sand Heads Water Level',
            link_text='Sand Heads',
            svg_name='SH_waterlevel'
        ),
        FigureMetadata(
            title='Woodwards Landing Water Level',
            link_text='Woodwards Landing',
            svg_name='WL_waterlevel'
        ),
        FigureMetadata(
            title='New Westminster Water Level',
            link_text='New Westminster',
            svg_name='NW_waterlevel'
        ),
    ]
)

second_narrows_current_figure = FigureMetadata(
    title='Near-Surface Current at 2nd Narrows',
    svg_name='2ndNarrows_current',
)

image_loops = ImageLoopGroup(
    description='Surface Currents and Thalweg Transects',
    loops=[
        ImageLoop(
            model_var='English Bay',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Surface Currents in English Bay',
                link_text='English Bay Surface Currents',
                svg_name='EnglishBay_surface_currents',
            )
        ),
        ImageLoop(
            model_var='Vancouver Harbour',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Surface Currents in Vancouver Harbour',
                link_text='Vancouver Harbour Surface Currents',
                svg_name='VancouverHarbour_surface_currents',
            )
        ),
        ImageLoop(
            model_var='Indian Arm',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Surface Currents in Indian Arm',
                link_text='Indian Arm Surface Currents',
                svg_name='IndianArm_surface_currents',
            )
        ),
        ImageLoop(
            model_var='Vancouver Harbour Salinity',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Salinity in Vancouver Harbour',
                link_text='Vancouver Harbour Salinity',
                svg_name='VancouverHarbour_thalweg_salinity',
            )
        ),
        ImageLoop(
            model_var='Vancouver Harbour Temperature',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Temperature in Vancouver Harbour',
                link_text='Vancouver Harbour Temperature',
                svg_name='VancouverHarbour_thalweg_temp',
            )
        ),
        ImageLoop(
            model_var='Vancouver Harbour Tangential Velocity',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Tangential Velocity in Vancouver Harbour',
                link_text='Vancouver Harbour Tangential Velocity',
                svg_name='VancouverHarbour_thalweg_tangential_velocity',
            )
        ),
        ImageLoop(
            model_var='Port Moody Salinity',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Salinity in Port Moody Arm',
                link_text='Port Moody Salinity',
                svg_name='PortMoody_thalweg_salinity',
            )
        ),
        ImageLoop(
            model_var='Port Moody Temperature',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Temperature in Port Moody Arm',
                link_text='Port Moody Temperature',
                svg_name='PortMoody_thalweg_temp',
            )
        ),
        ImageLoop(
            model_var='Port Moody Tangential Velocity',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Tangential Velocity in Port Moody Arm',
                link_text='Port Moody Tangential Velocity',
                svg_name='PortMoody_thalweg_tangential_velocity',
            )
        ),
        ImageLoop(
            model_var='Indian Arm Salinity',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Salinity in Indian Arm',
                link_text='Indian Arm Salinity',
                svg_name='IndianArm_thalweg_salinity',
            )
        ),
        ImageLoop(
            model_var='Indian Arm Temperature',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Temperature in Indian Arm',
                link_text='Indian Arm Temperature',
                svg_name='IndianArm_thalweg_temp',
            )
        ),
        ImageLoop(
            model_var='Indian Arm Tangential Velocity',
            first_hr=1,
            image_minute=0,
            metadata=FigureMetadata(
                title='Tangential Velocity in Indian Arm',
                link_text='Indian Arm Tangential Velocity',
                svg_name='IndianArm_thalweg_tangential_velocity',
            )
        ),
    ]
)


@view_config(
    route_name='fvcom.results.index', renderer='fvcom/results_index.mako'
)
def results_index(request):
    """Render results calendar grid index page.
    """
    INDEX_GRID_COLS = 21
    # Calculate the date range to display in the grid and the number of
    # columns for the month headings of the grid
    fcst_date = arrow.now().floor('day').shift(days=+1)
    dates = list(
        arrow.Arrow.range(
            'day', fcst_date.shift(days=-(INDEX_GRID_COLS - 1)), fcst_date
        )
    )
    if dates[0].month != dates[-1].month:
        this_month_cols = dates[-1].day
        last_month_cols = INDEX_GRID_COLS - this_month_cols
    else:
        this_month_cols, last_month_cols = INDEX_GRID_COLS, 0
    # Replace dates for which there are no figures with None
    grid_rows = (
        # Calendar grid row key, run type, figures, figures type
        (
            'x2 nowcast water levels', 'nowcast-x2',
            tide_stn_water_level_figure_group
        ),
        (
            'r12 nowcast water levels', 'nowcast-r12',
            tide_stn_water_level_figure_group
        ),
        (
            'x2 forecast water levels', 'forecast-x2',
            tide_stn_water_level_figure_group
        ),
    )
    grid_dates = {
        row: _exclude_missing_dates(dates, figures, run_type)
        for row, run_type, figures in grid_rows
    }
    return {
        'first_date': dates[0],
        'last_date': dates[-1],
        'this_month_cols': this_month_cols,
        'last_month_cols': last_month_cols,
        'grid_dates': grid_dates,
    }


def _exclude_missing_dates(dates, figures, run_type):
    return ((
        d if any(fig.available(run_type, d, model='fvcom')
                 for fig in figures) else None
    ) for d in dates)


@view_config(
    route_name='fvcom.results.nowcast-x2.publish',
    renderer='fvcom/publish.mako'
)
# Legacy route
@view_config(
    route_name='fvcom.results.nowcast.publish', renderer='fvcom/publish.mako'
)
def nowcast_x2_publish(request):
    """Render nowcast figures page.
    """
    return _values_for_publish_template(request, 'nowcast-x2')


@view_config(
    route_name='fvcom.results.nowcast-r12.publish',
    renderer='fvcom/publish.mako'
)
def nowcast_r12_publish(request):
    """Render nowcast figures page.
    """
    return _values_for_publish_template(request, 'nowcast-r12')


@view_config(
    route_name='fvcom.results.forecast-x2.publish',
    renderer='fvcom/publish.mako'
)
# Legacy route
@view_config(
    route_name='fvcom.results.forecast.publish', renderer='fvcom/publish.mako'
)
def forecast_x2_publish(request):
    """Render forecast figures page.
    """
    return _values_for_publish_template(request, 'forecast-x2')


def _values_for_publish_template(request, run_type):
    """Calculate template variable values for a figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    available_figures = {
        "water levels":
        tide_stn_water_level_figure_group.available(
            run_type, results_date, 'fvcom'
        ),
        "2nd narrows currents": [
            second_narrows_current_figure.available(
                run_type, results_date, 'fvcom'
            )
        ],
        "image loops": [],
    }
    for image_loop in image_loops.loops:
        images_available = image_loop.available(
            run_type, results_date, 'fvcom'
        )
        if images_available:
            available_figures["image loops"].append(images_available)
            run_duration = 24 if run_type == "nowcast" else 60  # hours
            image_loop.hrs = image_loop.hours(
                run_type,
                results_date,
                model='fvcom',
                file_dates=arrow.Arrow.range(
                    'day',
                    results_date,
                    results_date.shift(hours=+run_duration)
                ),
            )
    if not any(available_figures[figs] for figs in available_figures):
        raise HTTPNotFound
    figure_links = []
    if available_figures["water levels"]:
        figure_links.append(tide_stn_water_level_figure_group.description)
    if available_figures["2nd narrows currents"]:
        figure_links.append(second_narrows_current_figure.title)
    if available_figures["image loops"]:
        figure_links.append(image_loops.description)
    return {
        'results_date': results_date,
        'run_type_title': run_type.title(),
        'run_type': run_type,
        'run_date': results_date,
        'figure_links': figure_links,
        'available_figures': available_figures,
        'water_level_figures': tide_stn_water_level_figure_group,
        'second_narrows_current_figure': second_narrows_current_figure,
        'image_loops': image_loops,
    }
