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
"""salishsea_site WaveWatch3(TM) results views
"""
import logging

import arrow
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config
import requests

from salishsea_site.views.salishseacast import FigureGroup, FigureMetadata

logger = logging.getLogger(__name__)

wave_height_period_figure_group = FigureGroup(
    description='Wave Height and Period at Buoys',
    figures=[
        FigureMetadata(
            title='Halibut Bank Wave Height and Period',
            link_text='Halibut Bank',
            svg_name='HB_waves'
        ),
        FigureMetadata(
            title='Sentry Shoal Wave Height and Period',
            link_text='Sentry Shoal',
            svg_name='SS_waves'
        ),
    ]
)


@view_config(
    route_name='wwatch3.results.forecast.publish',
    renderer='wwatch3/publish.mako'
)
def forecast_publish(request):
    """Render forecast figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    figures_available = []
    with requests.Session() as session:
        figures_available = wave_height_period_figure_group.available(
            request, 'forecast', results_date, session, 'wwatch3'
        )
    if not any(figures_available):
        raise HTTPNotFound
    return {
        'results_date': results_date,
        'run_type_title': 'Forecast',
        'run_type': 'forecast',
        'run_date': results_date,
        'figures': wave_height_period_figure_group,
        'figures_available': figures_available,
    }


@view_config(
    route_name='wwatch3.results.forecast2.publish',
    renderer='wwatch3/publish.mako'
)
def forecast2_publish(request):
    """Render forecast2 figures page.
    """
    results_date = arrow.get(request.matchdict['results_date'], 'DDMMMYY')
    figures_available = []
    with requests.Session() as session:
        figures_available = wave_height_period_figure_group.available(
            request, 'forecast2', results_date, session, 'wwatch3'
        )
    if not any(figures_available):
        raise HTTPNotFound
    return {
        'results_date': results_date,
        'run_type_title': 'Preliminary Forecast',
        'run_type': 'forecast2',
        'run_date': results_date,
        'figures': wave_height_period_figure_group,
        'figures_available': figures_available,
    }
