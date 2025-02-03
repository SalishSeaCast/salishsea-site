# Copyright 2014 – present by the Mesoscale Ocean and Atmospheric Dynamics (MOAD) group
# in the Department of Earth, Ocean, and Atmospheric Sciences
# at The University of British Columbia

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# SPDX-License-Identifier: Apache-2.0


"""salishsea_site WAVEWATCH III® results views"""
import logging

import arrow
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from salishsea_site.views.figures import FigureMetadata, FigureGroup

logger = logging.getLogger(__name__)

wave_height_period_figure_group = FigureGroup(
    description="Wave Height and Period at Buoys",
    figures=[
        FigureMetadata(
            title="Halibut Bank Wave Height and Period",
            link_text="Halibut Bank",
            svg_name="HB_waves",
        ),
        FigureMetadata(
            title="Sentry Shoal Wave Height and Period",
            link_text="Sentry Shoal",
            svg_name="SS_waves",
        ),
    ],
)


@view_config(route_name="wwatch3.results.index", renderer="wwatch3/results_index.mako")
def results_index(request):
    """Render results calendar grid index page."""
    INDEX_GRID_COLS = 21
    # Calculate the date range to display in the grid and the number of
    # columns for the month headings of the grid
    fcst_date = arrow.now().floor("day").shift(days=+1)
    dates = list(
        arrow.Arrow.range(
            "day", fcst_date.shift(days=-(INDEX_GRID_COLS - 1)), fcst_date
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
        ("forecast", "forecast", wave_height_period_figure_group, "publish"),
        ("prelim forecast", "forecast2", wave_height_period_figure_group, "publish"),
    )
    grid_dates = {
        row: _exclude_missing_dates(dates, figures, figs_type, run_type)
        for row, run_type, figures, figs_type in grid_rows
    }
    return {
        "first_date": dates[0],
        "last_date": dates[-1],
        "this_month_cols": this_month_cols,
        "last_month_cols": last_month_cols,
        "grid_dates": grid_dates,
    }


def _exclude_missing_dates(dates, figures, figs_type, run_type):
    return (
        (
            d
            if any(fig.available(run_type, d, model="wwatch3") for fig in figures)
            else None
        )
        for d in dates
    )


@view_config(
    route_name="wwatch3.results.forecast.publish", renderer="wwatch3/publish.mako"
)
def forecast_publish(request):
    """Render forecast figures page."""
    results_date = arrow.get(request.matchdict["results_date"], "DDMMMYY")
    figures_available = wave_height_period_figure_group.available(
        "forecast", results_date, "wwatch3"
    )
    if not any(figures_available):
        raise HTTPNotFound
    return {
        "results_date": results_date,
        "run_type_title": "Forecast",
        "run_type": "forecast",
        "run_date": results_date,
        "figures": wave_height_period_figure_group,
        "figures_available": figures_available,
    }


@view_config(
    route_name="wwatch3.results.forecast2.publish", renderer="wwatch3/publish.mako"
)
def forecast2_publish(request):
    """Render forecast2 figures page."""
    results_date = arrow.get(request.matchdict["results_date"], "DDMMMYY")
    figures_available = wave_height_period_figure_group.available(
        "forecast2", results_date, "wwatch3"
    )
    if not any(figures_available):
        raise HTTPNotFound
    return {
        "results_date": results_date,
        "run_type_title": "Preliminary Forecast",
        "run_type": "forecast2",
        "run_date": results_date,
        "figures": wave_height_period_figure_group,
        "figures_available": figures_available,
    }
