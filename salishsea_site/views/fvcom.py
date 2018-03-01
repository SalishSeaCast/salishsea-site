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
