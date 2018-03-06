# Copyright 2014-2018 The Salish Sea MEOPAR Contributors
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
import requests

from salishsea_site.views.salishseacast import FigureGroup, FigureMetadata

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


@view_config(
    route_name='fvcom.results.index', renderer='fvcom/results_index.mako'
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
        (
            'nowcast publish', 'nowcast', tide_stn_water_level_figure_group,
            'publish'
        ),
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
    return ((
        d if any(
            fig.available(request, run_type, d, session, model='fvcom')
            for fig in figures
        ) else None
    ) for d in dates)


@view_config(
    route_name='fvcom.results.nowcast.publish', renderer='fvcom/publish.mako'
)
def nowcast_publish(request):
    """Render nowcast figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    figures_available = []
    with requests.Session() as session:
        figures_available = tide_stn_water_level_figure_group.available(
            request, 'nowcast', results_date, session, 'fvcom'
        )
    if not any(figures_available):
        raise HTTPNotFound
    return {
        'results_date': results_date,
        'run_type_title': 'Nowcast',
        'run_type': 'nowcast',
        'run_date': results_date,
        'figures': tide_stn_water_level_figure_group,
        'figures_available': figures_available,
    }
