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


"""salishsea_site SalishSeaCast views
"""
import logging
import os
import urllib.parse
from pathlib import Path

import arrow
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from salishsea_site.views.figures import (
    FigureMetadata,
    FigureGroup,
    ImageLoop,
    ImageLoopGroup,
)

logger = logging.getLogger(__name__)

publish_figures = [
    FigureMetadata(
        title="Marine and Atmospheric Conditions - Storm Surge Alerts",
        svg_name="Threshold_website",
    ),
    FigureMetadata(
        title="Tidal Predictions for Point Atkinson", svg_name="PA_tidal_predictions"
    ),
]

publish_tides_max_ssh_figure_group = FigureGroup(
    description="Tide Gauge Station Sea Surface Heights",
    figures=[
        # Keep Point Atkinson at the top of the list
        FigureMetadata(
            title="Point Atkinson Sea Surface Height",
            link_text="Point Atkinson",
            svg_name="PA_maxSSH",
        ),
        # Keep the rest of the list in alphabetical order by place name
        FigureMetadata(
            title="Boundary Bay Sea Surface Height",
            link_text="Boundary Bay",
            svg_name="BB_maxSSH",
        ),
        FigureMetadata(
            title="Campbell River Sea Surface Height",
            link_text="Campbell River",
            svg_name="CR_maxSSH",
        ),
        FigureMetadata(
            title="Cherry Point Sea Surface Height",
            link_text="Cherry Point",
            svg_name="CP_maxSSH",
        ),
        FigureMetadata(
            title="Friday Harbor Sea Surface Height",
            link_text="Friday Harbor",
            svg_name="FH_maxSSH",
        ),
        FigureMetadata(
            title="Halfmoon Bay Surface Height",
            link_text="Halfmoon Bay",
            svg_name="HB_maxSSH",
        ),
        FigureMetadata(
            title="Nanaimo Sea Surface Height",
            link_text="Nanaimo",
            svg_name="Nan_maxSSH",
        ),
        FigureMetadata(
            title="Neah Bay Sea Surface Height",
            link_text="Neah Bay",
            svg_name="NB_maxSSH",
        ),
        FigureMetadata(
            title="New Westminster Sea Surface Height",
            link_text="New Westminster",
            svg_name="NW_maxSSH",
        ),
        FigureMetadata(
            title="Patricia Bay Sea Surface Height",
            link_text="Patricia Bay",
            svg_name="PB_maxSSH",
        ),
        FigureMetadata(
            title="Port Renfrew Sea Surface Height",
            link_text="Port Renfrew",
            svg_name="PR_maxSSH",
        ),
        FigureMetadata(
            title="Sand Heads Sea Surface Height",
            link_text="Sand Heads",
            svg_name="SH_maxSSH",
        ),
        FigureMetadata(
            title="Sandy Cove Sea Surface Height",
            link_text="Sandy Cove",
            svg_name="SC_maxSSH",
        ),
        FigureMetadata(
            title="Squamish Sea Surface Height",
            link_text="Squamish",
            svg_name="Sqam_maxSSH",
        ),
        FigureMetadata(
            title="Victoria Sea Surface Height",
            link_text="Victoria",
            svg_name="Vic_maxSSH",
        ),
        FigureMetadata(
            title="Woodwards Landing Sea Surface Height",
            link_text="Woodwards Landing",
            svg_name="WL_maxSSH",
        ),
    ],
)

surface_currents_image_loops = ImageLoopGroup(
    description="Surface Currents",
    loops=[
        ImageLoop(
            model_var=f"Tile{tile_number:02d}",
            metadata=FigureMetadata(
                title=f"Surface currents - tile{tile_number:02d}",
                link_text=f"Tile{tile_number:02d}",
                svg_name=f"surface_currents_tile{tile_number:02d}",
            ),
        )
        for tile_number in range(1, 21)
    ],
)

currents_physics_image_loops = ImageLoopGroup(
    description="Tracer Fields Along Thalweg and on Surface",
    loops=[
        ImageLoop(
            model_var="salinity",
            metadata=FigureMetadata(
                title="Salinity Fields Along Thalweg and on Surface",
                link_text="Salinity",
                svg_name="salinity_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="temperature",
            metadata=FigureMetadata(
                title="Temperature Fields Along Thalweg and on Surface",
                link_text="Temperature",
                svg_name="temperature_thalweg_and_surface",
            ),
        ),
    ],
)

currents_physics_figures = [
    FigureMetadata(
        title="Surface Currents and Velocity Cross-sections",
        svg_name="Currents_sections_and_surface",
    ),
    FigureMetadata(
        title="Model Currents at ONC VENUS East Node", svg_name="Currents_at_VENUS_East"
    ),
    FigureMetadata(
        title="Model Currents at ONC VENUS Central Node",
        svg_name="Currents_at_VENUS_Central",
    ),
]

baynes_sound_figures = [
    FigureMetadata(title="Baynes Sound Surface Fields", svg_name="baynes_sound_surface")
]

biology_image_loops = ImageLoopGroup(
    description="Tracer Fields Along Thalweg and Near Surface",
    loops=[
        ImageLoop(
            model_var="salinity",
            metadata=FigureMetadata(
                title="Salinity Fields Along Thalweg and at Surface",
                link_text="Surface Salinity",
                svg_name="salinity_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="temperature",
            metadata=FigureMetadata(
                title="Temperature Fields Along Thalweg and at Surface",
                link_text="Surface Temperature",
                svg_name="temperature_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="nitrate",
            metadata=FigureMetadata(
                title="Nitrate Fields Along Thalweg and at Surface",
                link_text="Surface Nitrate",
                svg_name="nitrate_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="ammonium",
            metadata=FigureMetadata(
                title="Ammonium Fields Along Thalweg and at Surface",
                link_text="Surface Ammonium",
                svg_name="ammonium_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="silicon",
            metadata=FigureMetadata(
                title="Silicon Fields Along Thalweg and at Surface",
                link_text="Surface Silicon",
                svg_name="silicon_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="dissolved_organic_nitrogen",
            metadata=FigureMetadata(
                title="Dissolved Organic Nitrogen Fields Along Thalweg and at "
                "Surface",
                link_text="Surface Dissolved Organic Nitrogen",
                svg_name="dissolved_organic_nitrogen_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="particulate_organic_nitrogen",
            metadata=FigureMetadata(
                title="Particulate Organic Nitrogen Fields Along Thalweg and at "
                "Surface",
                link_text="Surface Particulate Organic Nitrogen",
                svg_name="particulate_organic_nitrogen_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="biogenic_silicon",
            metadata=FigureMetadata(
                title="Biogenic Silicon Fields Along Thalweg and at Surface",
                link_text="Surface Biogenic Silicon",
                svg_name="biogenic_silicon_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="diatoms",
            metadata=FigureMetadata(
                title="Diatoms Fields Along Thalweg and Near Surface",
                link_text="Depth Integrated Diatoms",
                svg_name="diatoms_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="ciliates",
            metadata=FigureMetadata(
                title="Ciliates Fields Along Thalweg and Near Surface",
                link_text="Depth Integrated Ciliates",
                svg_name="ciliates_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="flagellates",
            metadata=FigureMetadata(
                title="Flagellates Fields Along Thalweg and Near Surface",
                link_text="Depth Integrated Flagellates",
                svg_name="flagellates_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="microzooplankton",
            metadata=FigureMetadata(
                title="Microzooplankton Fields Along Thalweg and Near Surface",
                link_text="Depth Integrated Microzooplankton",
                svg_name="microzooplankton_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="mesozooplankton",
            metadata=FigureMetadata(
                title="Mesozooplankton Fields Along Thalweg and Near Surface",
                link_text="Depth Integrated Mesozooplankton",
                svg_name="mesozooplankton_thalweg_and_surface",
            ),
        ),
        ImageLoop(
            model_var="Fraser_tracer",
            metadata=FigureMetadata(
                title="Fraser River Turbidity Fields Along Thalweg and at Surface",
                link_text="Surface Fraser River Turbidity",
                svg_name="Fraser_tracer_thalweg_and_surface",
            ),
        ),
    ],
)

timeseries_figure_group = FigureGroup(
    description="nowcast-green Time Series",
    figures=[
        FigureMetadata(
            title="Temperature and Salinity",
            link_text="Surface Temperature and Salinity",
            svg_name="temperature_salinity_timeseries",
        ),
        FigureMetadata(
            title="Nitrate and Diatom Concentrations",
            link_text="Surface Nitrate and Diatom Concentrations",
            svg_name="nitrate_diatoms_timeseries",
        ),
        FigureMetadata(
            title="Mesodinium rubrum and Flagellates Concentrations",
            link_text="Surface Mesodinium rubrum and Flagellates Concentrations",
            svg_name="mesodinium_flagellates_timeseries",
        ),
        FigureMetadata(
            title="Mesozooplankton and Microzooplankton Concentrations",
            link_text="Surface Mesozooplankton and Microzooplankton Concentrations",
            svg_name="mesozoo_microzoo_timeseries",
        ),
    ],
)

comparison_figures = [
    FigureMetadata(
        title="Modeled and Observed Winds at Sand Heads", svg_name="SH_wind"
    ),
    FigureMetadata(
        title=(
            "Modeled and Observed Surface Salinity "
            "Along Horseshoe Bay-Departure Bay Ferry Route"
        ),
        svg_name="HB_DB_ferry_salinity",
    ),
    FigureMetadata(
        title=(
            "Modeled and Observed Surface Salinity "
            "Along Tsawwassen-Duke Pt. Ferry Route"
        ),
        svg_name="TW_DP_ferry_salinity",
    ),
    FigureMetadata(
        title=(
            "Modeled and Observed Surface Salinity "
            "Along Tsawwassen-Schwartz Bay Ferry Route"
        ),
        svg_name="TW_SB_ferry_salinity",
    ),
]
onc_venus_comparison_figure_group = FigureGroup(
    description="Salinity and Temperature at ONC VENUS Nodes",
    figures=[
        FigureMetadata(
            title="Salinity and Temperature at ONC VENUS Central Node",
            link_text="Central Node",
            svg_name="Compare_VENUS_Central",
        ),
        FigureMetadata(
            title="Salinity and Temperature at ONC VENUS East Node",
            link_text="East Node",
            svg_name="Compare_VENUS_East",
        ),
        FigureMetadata(
            title="Salinity and Temperature at ONC VENUS Delta DDL Node",
            link_text="DDL Node",
            svg_name="Compare_VENUS_Delta_DDL",
        ),
    ],
)


@view_config(route_name="storm_surge.portal", renderer="storm_surge/portal.mako")
# Legacy route
@view_config(route_name="storm_surge.index.html", renderer="storm_surge/portal.mako")
def storm_surge_portal(request):
    """Render storm surge portal page."""
    return {}


@view_config(route_name="storm_surge.forecast", renderer="salishseacast/publish.mako")
# Legacy route
@view_config(
    route_name="storm_surge.forecast.html", renderer="salishseacast/publish.mako"
)
def storm_surge_forecast(request):
    """Render storm surge forecast page that shows most recent forecast or
    forecast2 results figures.
    """
    fcst_date = arrow.now().floor("day").shift(days=+1)
    try:
        try:
            return _data_for_publish_template(
                request,
                "forecast",
                fcst_date,
                publish_figures,
                publish_tides_max_ssh_figure_group,
                fcst_date.shift(days=-1),
            )
        except HTTPNotFound:
            return _data_for_publish_template(
                request,
                "forecast2",
                fcst_date,
                publish_figures,
                publish_tides_max_ssh_figure_group,
                fcst_date.shift(days=-2),
            )
    except HTTPNotFound:
        return _data_for_publish_template(
            request,
            "forecast",
            fcst_date.shift(days=-1),
            publish_figures,
            publish_tides_max_ssh_figure_group,
            fcst_date.shift(days=-2),
        )


@view_config(route_name="storm_surge.alert.feed", renderer="string")
def storm_surge_alert_feed(request):
    """Render the requested storm surge alert ATOM feed file."""
    introspector = request.registry.introspector
    figs_server = request.registry.settings["nowcast_figures_server_name"]
    figs_path = introspector.get("static views", figs_server)["spec"]
    feeds_path = Path(figs_path, "storm-surge/atom")
    try:
        request.response.content_type = "application/atom+xml"
        return (feeds_path / request.matchdict["filename"]).open().read()
    except FileNotFoundError as e:
        logger.debug(e)
        raise HTTPNotFound


@view_config(route_name="salishseacast.about", renderer="salishseacast/about.mako")
# Legacy route
@view_config(route_name="nemo.index.html", renderer="salishseacast/about.mako")
def about(request):
    return {}


@view_config(route_name="results.index", renderer="salishseacast/results_index.mako")
# Legacy route
@view_config(
    route_name="results.index.html", renderer="salishseacast/results_index.mako"
)
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
        # Calendar grid row key, run type, figures, figures type, model
        (
            "prelim storm surge forecast",
            "forecast2",
            publish_figures,
            "publish",
            "nemo",
        ),
        ("storm surge forecast", "forecast", publish_figures, "publish", "nemo"),
        (
            "prelim surface currents forecast",
            "forecast2",
            surface_currents_image_loops,
            "publish",
            "surface currents",
        ),
        (
            "surface currents forecast",
            "forecast",
            surface_currents_image_loops,
            "publish",
            "surface currents",
        ),
        ("nowcast currents", "nowcast", currents_physics_figures, "currents", "nemo"),
        ("nowcast biology", "nowcast-green", biology_image_loops, "biology", "nemo"),
        (
            "nowcast timeseries",
            "nowcast-green",
            timeseries_figure_group,
            "timeseries",
            "nemo",
        ),
        ("nowcast comparison", "nowcast", comparison_figures, "comparison", "nemo"),
    )
    grid_dates = {
        row: _exclude_missing_dates(dates, figures, figs_type, run_type, model)
        for row, run_type, figures, figs_type, model in grid_rows
    }
    return {
        "first_date": dates[0],
        "last_date": dates[-1],
        "this_month_cols": this_month_cols,
        "last_month_cols": last_month_cols,
        "grid_dates": grid_dates,
    }


def _exclude_missing_dates(dates, figures, figs_type, run_type, model):
    if figs_type == "publish":
        run_date_offsets = {"forecast": -1, "forecast2": -2}
        return (
            (
                d
                if figures[0].available(
                    run_type, d.shift(days=run_date_offsets[run_type]), model
                )
                else None
            )
            for d in dates
        )
    else:
        return (
            (d if any(fig.available(run_type, d, model) for fig in figures) else None)
            for d in dates
        )


@view_config(
    route_name="results.forecast.publish", renderer="salishseacast/publish.mako"
)
# Legacy route
@view_config(
    route_name="results.forecast.publish.html", renderer="salishseacast/publish.mako"
)
def forecast_publish(request):
    """Render storm surge forecast figures page."""
    results_date = arrow.get(request.matchdict["results_date"], "DDMMMYY")
    run_date = results_date.shift(days=-1)
    return _data_for_publish_template(
        request,
        "forecast",
        results_date,
        publish_figures,
        publish_tides_max_ssh_figure_group,
        run_date,
    )


@view_config(
    route_name="results.forecast2.publish", renderer="salishseacast/publish.mako"
)
# Legacy route
@view_config(
    route_name="results.forecast2.publish.html", renderer="salishseacast/publish.mako"
)
def forecast2_publish(request):
    """Render preliminary storm surge forecast figures page."""
    results_date = arrow.get(request.matchdict["results_date"], "DDMMMYY")
    run_date = results_date.shift(days=-2)
    return _data_for_publish_template(
        request,
        "forecast2",
        results_date,
        publish_figures,
        publish_tides_max_ssh_figure_group,
        run_date,
    )


@view_config(
    route_name="results.forecast.surfacecurrents",
    renderer="salishseacast/surface_currents.mako",
)
def forecast_surface_currents(request):
    """Render surface currents tiles forecast figures page."""
    results_date = arrow.get(request.matchdict["results_date"], "DDMMMYY")
    run_date = results_date.shift(days=-1)
    tile_dates = list(
        arrow.Arrow.range("day", run_date.shift(days=-1), run_date.shift(days=+2))
    )
    tiles_pdf_url_stub = _calc_tiles_pdf_url_stub(
        request, "forecast", run_date, tile_dates
    )
    return {
        "results_date": results_date,
        "run_type": "forecast",
        "run_date": run_date,
        "tile_dates": tile_dates,
        "image_loops": surface_currents_image_loops,
        "tiles_pdf_url_stub": tiles_pdf_url_stub,
    }


@view_config(
    route_name="results.forecast2.surfacecurrents",
    renderer="salishseacast/surface_currents.mako",
)
def forecast2_surface_currents(request):
    """Render surface currents tiles forecast2 figures page."""
    results_date = arrow.get(request.matchdict["results_date"], "DDMMMYY")
    run_date = results_date.shift(days=-2)
    tile_dates = list(arrow.Arrow.range("day", run_date, run_date.shift(days=+3)))
    tiles_pdf_url_stub = _calc_tiles_pdf_url_stub(
        request, "forecast2", run_date, tile_dates
    )
    return {
        "results_date": results_date,
        "run_type": "forecast2",
        "run_date": run_date,
        "tile_dates": tile_dates,
        "image_loops": surface_currents_image_loops,
        "tiles_pdf_url_stub": tiles_pdf_url_stub,
    }


@view_config(
    route_name="results.nowcast-green.surfacecurrents",
    renderer="salishseacast/surface_currents.mako",
)
def nowcast_green_surface_currents(request):
    """Render surface currents tiles nowcast-green figures page."""
    results_date = arrow.get(request.matchdict["results_date"], "DDMMMYY")
    run_date = results_date
    tile_dates = list(arrow.Arrow.range("day", run_date, run_date.shift(days=+3)))
    tiles_pdf_url_stub = _calc_tiles_pdf_url_stub(
        request, "nowcast-green", run_date, tile_dates
    )
    return {
        "results_date": results_date,
        "run_type": "nowcast-green",
        "run_date": run_date,
        "tile_dates": tile_dates,
        "image_loops": surface_currents_image_loops,
        "tiles_pdf_url_stub": tiles_pdf_url_stub,
    }


def _calc_tiles_pdf_url_stub(request, run_type, run_date, tile_dates):
    available_loop_images = []
    for image_loop in surface_currents_image_loops.loops:
        images_available = image_loop.available(
            run_type, run_date, model="surface currents"
        )
        if images_available:
            available_loop_images.append(images_available)
            image_loop.hrs = image_loop.hours(
                run_type, run_date, model="surface currents", file_dates=tile_dates
            )
    if not any(available_loop_images):
        raise HTTPNotFound
    # Build a URL stub for the tilexx.pdf files that will be transformed in the template javascript
    img_url = request.static_url(
        surface_currents_image_loops.loops[0].path(
            run_type, run_date, 0, "surface currents"
        )
    )
    parsed_url = urllib.parse.urlparse(img_url)
    tiles_pdf_path = os.fspath(Path(parsed_url.path).parent / "tilexx.pdf")
    tiles_pdf_url_stub = urllib.parse.urlunparse(
        (
            parsed_url.scheme,
            parsed_url.netloc,
            tiles_pdf_path,
            parsed_url.params,
            parsed_url.query,
            parsed_url.fragment,
        )
    )
    return tiles_pdf_url_stub


@view_config(
    route_name="results.nowcast.currents", renderer="salishseacast/currents.mako"
)
# Legacy routes
@view_config(
    route_name="results.nowcast.research", renderer="salishseacast/currents.mako"
)
@view_config(
    route_name="results.nowcast.research.html", renderer="salishseacast/currents.mako"
)
def nowcast_currents_physics(request):
    """Render model research currents and physics evaluation results figures
    page.
    """
    results_date = arrow.get(request.matchdict["results_date"], "DDMMMYY")
    available_figures = [
        fig
        for fig in currents_physics_figures
        if fig.available("nowcast", results_date)
    ]
    available_loop_images = []
    for image_loop in currents_physics_image_loops.loops:
        images_available = image_loop.available("nowcast", results_date)
        if images_available:
            available_loop_images.append(images_available)
            image_loop.hrs = image_loop.hours("nowcast", results_date)
    if not any(available_figures + available_loop_images):
        raise HTTPNotFound
    figure_links = (
        [currents_physics_image_loops.description] if available_loop_images else []
    )
    figure_links.extend(figure.title for figure in available_figures)
    return {
        "results_date": results_date,
        "run_type": "nowcast",
        "run_date": results_date,
        "figure_links": figure_links,
        "figures": available_figures,
        "image_loops": currents_physics_image_loops,
    }


@view_config(
    route_name="results.nowcast.biology", renderer="salishseacast/biology.mako"
)
def nowcast_biology(request):
    """Render model research biology evaluation results figures page."""
    results_date = arrow.get(request.matchdict["results_date"], "DDMMMYY")
    available_figures = {
        "baynes sound": [
            fig.available("nowcast-agrif", results_date) for fig in baynes_sound_figures
        ],
        "biology loops": [],
    }
    for image_loop in biology_image_loops.loops:
        images_available = image_loop.available("nowcast-green", results_date)
        if images_available:
            available_figures["biology loops"].append(images_available)
            image_loop.hrs = image_loop.hours("nowcast-green", results_date)
    if not any(available_figures["baynes sound"] + available_figures["biology loops"]):
        raise HTTPNotFound
    figure_links = (
        [biology_image_loops.description] if available_figures["biology loops"] else []
    )
    figure_links.extend(
        [fig.title for fig in baynes_sound_figures]
        if available_figures["baynes sound"]
        else []
    )
    return {
        "results_date": results_date,
        "run_type": "nowcast-green",
        "run_date": results_date,
        "figure_links": figure_links,
        "available_figures": available_figures,
        "image_loops": biology_image_loops,
        "baynes_sound_figures": baynes_sound_figures,
    }


@view_config(
    route_name="results.nowcast.timeseries", renderer="salishseacast/timeseries.mako"
)
def nowcast_timeseries(request):
    """Render model research timeseries evaluation results figures page."""
    results_date = arrow.get(request.matchdict["results_date"], "DDMMMYY")
    available_figures = timeseries_figure_group.available("nowcast-green", results_date)
    if not any(available_figures):
        raise HTTPNotFound
    return {
        "results_date": results_date,
        "run_type": "nowcast-green",
        "run_date": results_date,
        "figures": timeseries_figure_group,
        "available_figures": available_figures,
    }


@view_config(
    route_name="results.nowcast.comparison", renderer="salishseacast/comparison.mako"
)
# Legacy route
@view_config(
    route_name="results.nowcast.comparison.html",
    renderer="salishseacast/comparison.mako",
)
def nowcast_comparison(request):
    """Render model and observation comparisons figures page."""
    results_date = arrow.get(request.matchdict["results_date"], "DDMMMYY")
    ungrouped_figures = [
        fig for fig in comparison_figures if fig.available("nowcast", results_date)
    ]
    onc_venus_figures_available = onc_venus_comparison_figure_group.available(
        "nowcast", results_date
    )
    if not ungrouped_figures and not any(onc_venus_figures_available):
        raise HTTPNotFound
    figure_links = [figure.title for figure in ungrouped_figures]
    if any(onc_venus_figures_available):
        figure_links.append(onc_venus_comparison_figure_group.description)
    return {
        "results_date": results_date,
        "run_type": "nowcast",
        "run_date": results_date,
        "figure_links": figure_links,
        "figures": ungrouped_figures,
        "onc_venus_figures_available": onc_venus_figures_available,
        "onc_venus_figures": onc_venus_comparison_figure_group,
    }


def _data_for_publish_template(
    request, run_type, results_date, figures, tides_max_ssh_figure_group, run_date
):
    """Calculate template variable values for a storm surge forecast figures
    page.
    """
    run_type_titles = {"forecast": "Forecast", "forecast2": "Preliminary Forecast"}
    available_figures, tides_max_ssh_figures_available = [], []
    storm_surge_alerts_fig_ready = publish_figures[0].available(run_type, run_date)
    if not storm_surge_alerts_fig_ready:
        raise HTTPNotFound
    available_figures.extend(
        [fig for fig in figures if fig.available(run_type, run_date)]
    )
    tides_max_ssh_figures_available = tides_max_ssh_figure_group.available(
        run_type, run_date
    )
    figure_links = [figure.title for figure in available_figures]
    template_data = {
        "results_date": results_date,
        "run_type_title": run_type_titles[run_type],
        "run_type": run_type,
        "run_date": run_date,
        "figure_links": figure_links,
        "figures": available_figures,
    }
    if any(tides_max_ssh_figures_available):
        figure_links.append(tides_max_ssh_figure_group.description)
        template_data[
            "tides_max_ssh_figures_available"
        ] = tides_max_ssh_figures_available
        template_data["tides_max_ssh_figures"] = tides_max_ssh_figure_group
    return template_data


@view_config(
    route_name="nowcast.monitoring", renderer="salishseacast/nowcast_monitoring.mako"
)
def nowcast_monitoring(request):
    return {
        "grib_to_netcdf_png": "/results/nowcast-sys/figures/monitoring/wg.png",
        "get_NeahBay_ssh_png": "/results/nowcast-sys/figures/monitoring/NBssh.png",
    }


@view_config(route_name="nowcast.logs", renderer="string")
def nowcast_logs(request):
    """Render the requested file from the :envvar:`NOWCAST_LOGS` directory
    as text.
    """
    try:
        logs_dir = Path(os.environ["NOWCAST_LOGS"])
    except KeyError:
        logger.warning("NOWCAST_LOGS environment variable is not set")
        raise HTTPNotFound
    try:
        return (logs_dir / request.matchdict["filename"]).open().read()
    except FileNotFoundError as e:
        logger.debug(e)
        raise HTTPNotFound
