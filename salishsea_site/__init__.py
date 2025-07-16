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


"""Pyramid web app that serves the salishsea.eos.ubc.ca site"""
import os

import sentry_sdk
from pyramid.config import Configurator
from pyramid.static import static_view
from sentry_sdk.integrations.pyramid import PyramidIntegration

sentry_sdk.init(dsn=os.environ.get("SENTRY_DSN"), integrations=[PyramidIntegration()])


def main(global_config, **settings):
    """Configure the Pyramid WSGI application."""
    config = Configurator(settings=settings)
    _static_views(config, settings)
    _erddap_url(config)
    _site_routes(config)
    _salishseacast_routes(config)
    _bloomcast_routes(config)
    _about_site_routes(config)
    _figure_server(config)
    config.scan()
    return config.make_wsgi_app()


def _static_views(config, settings):
    config.add_static_view(name="static", path="salishsea_site:static")
    config.add_static_view(
        name=settings["nowcast_figures_server_name"],
        path="/results/nowcast-sys/figures",
    )


def _erddap_url(config):
    def _add_erddap_url(request):
        return "https://salishsea.eos.ubc.ca/erddap/"

    config.add_request_method(_add_erddap_url, "erddap_url", reify=True)


def _site_routes(config):
    config.add_route("site.index", "/")
    config.add_route("robots.txt", "/robots.txt")
    # Legacy route
    config.add_route("site.index.html", "/index.html")


def _salishseacast_routes(config):
    config.add_route("storm_surge.portal", "storm-surge/")
    config.add_route("storm_surge.forecast", "storm-surge/forecast")
    config.add_route("storm_surge.alert.feed", "storm-surge/atom/{filename}")
    config.add_route("salishseacast.about", "nemo/")
    config.add_route("results.index", "nemo/results/")
    config.add_route(
        "results.forecast.publish", "nemo/results/forecast/publish/{results_date}"
    )
    config.add_route(
        "results.forecast2.publish", "nemo/results/forecast2/publish/{results_date}"
    )
    config.add_route(
        "results.forecast.surfacecurrents",
        "nemo/results/forecast/surfacecurrents/{results_date}",
    )
    config.add_route(
        "results.forecast2.surfacecurrents",
        "nemo/results/forecast2/surfacecurrents/{results_date}",
    )
    config.add_route(
        "results.nowcast-green.surfacecurrents",
        "nemo/results/nowcast-green/surfacecurrents/{results_date}",
    )
    config.add_route(
        "results.nowcast.currents", "nemo/results/nowcast/currents/{results_date}"
    )
    config.add_route(
        "results.nowcast.biology", "nemo/results/nowcast/biology/{results_date}"
    )
    config.add_route(
        "results.nowcast.timeseries", "nemo/results/nowcast/timeseries/{results_date}"
    )
    config.add_route(
        "results.nowcast.comparison", "nemo/results/nowcast/comparison/{results_date}"
    )
    config.add_route("nowcast.monitoring", "nemo/nowcast/monitoring")
    config.add_route("nowcast.logs", "nemo/nowcast/logs/{filename}{token:.*}")
    # VHFR FVCOM model results routes
    config.add_route("fvcom.results.index", "fvcom/results/")
    config.add_route(
        "fvcom.results.nowcast-x2.publish",
        "fvcom/results/nowcast-x2/publish/{results_date}",
    )
    config.add_route(
        "fvcom.results.nowcast-r12.publish",
        "fvcom/results/nowcast-r12/publish/{results_date}",
    )
    config.add_route(
        "fvcom.results.forecast-x2.publish",
        "fvcom/results/forecast-x2/publish/{results_date}",
    )
    # WAVEWATCH III® model results routes
    config.add_route("wwatch3.results.index", "wwatch3/results/")
    config.add_route(
        "wwatch3.results.forecast.publish",
        "wwatch3/results/forecast/publish/{results_date}",
    )
    config.add_route(
        "wwatch3.results.forecast2.publish",
        "wwatch3/results/forecast2/publish/{results_date}",
    )
    # Legacy routes
    config.add_route("storm_surge.index.html", "storm-surge/index.html")
    config.add_route("storm_surge.forecast.html", "storm-surge/forecast.html")
    config.add_route("results.index.html", "nemo/results/index.html")
    config.add_route("nemo.index.html", "nemo/index.html")
    config.add_route(
        "results.forecast.publish.html",
        "nemo/results/forecast/publish_{results_date}.html",
    )
    config.add_route(
        "results.forecast2.publish.html",
        "nemo/results/forecast2/publish_{results_date}.html",
    )
    config.add_route(
        "results.nowcast.research", "nemo/results/nowcast/research/{results_date}"
    )
    config.add_route(
        "results.nowcast.research.html",
        "nemo/results/nowcast/research_{results_date}.html",
    )
    config.add_route(
        "results.nowcast.comparison.html",
        "nemo/results/nowcast/comparison_{results_date}.html",
    )
    config.add_route(
        "fvcom.results.nowcast.publish", "fvcom/results/nowcast/publish/{results_date}"
    )
    config.add_route(
        "fvcom.results.forecast.publish",
        "fvcom/results/forecast/publish/{results_date}",
    )


def _bloomcast_routes(config):
    config.add_route("bloomcast.about", "bloomcast/")
    config.add_route("bloomcast.spring_diatoms", "bloomcast/spring_diatoms")
    # Legacy routes
    config.add_route("bloomcast.index.html", "bloomcast.html")
    config.add_route("bloomcast.spring_diatoms.html", "bloomcast/spring_diatoms.html")


def _about_site_routes(config):
    config.add_route("about.contributors", "contributors")
    config.add_route("about.publications", "publications")
    config.add_route("about.license", "license")
    # Legacy route
    config.add_route("about.contributors.html", "contributors.html")
    config.add_route("about.license.html", "license.html")


def _figure_server(config):
    config.add_view("salishsea_site._figure", route_name="figure")
    config.add_route("figure", "/*subpath")


_figure = static_view("/var/www/html/nowcast-sys/figures", use_subpath=True)
