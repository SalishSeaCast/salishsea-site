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

"""Pyramid web app that serves the salishsea.eos.ubc.ca site
"""
import datetime

from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    _static_views(config, settings)
    _copyright_year_range(config)
    _salishseacast_routes(config)
    _about_site_routes(config)
    _catchall_static_pages(config)
    config.scan()
    return config.make_wsgi_app()


def _copyright_year_range(config):
    def _add_copyright_year_range(request):
        return (
            '2013' if datetime.date.today().year == 2013
            else '2013-{:%Y}'.format(datetime.date.today()))
    config.add_request_method(
        _add_copyright_year_range, 'copyright_years', reify=True)


def _static_views(config, settings):
    config.add_static_view(name='static', path='salishsea_site:static')
    config.add_static_view(
        name=settings['nowcast_figures_server_name'],
        path='/results/nowcast-sys/figures')


def _salishseacast_routes(config):
    config.add_route(
        'storm_surge.forecast',
        'storm-surge/forecast')
    config.add_route(
        'storm_surge.alert.feed',
        'storm-surge/atom/{filename}')
    config.add_route(
        'results.index',
        'nemo/results/')
    config.add_route(
        'results.nowcast.publish',
        'nemo/results/nowcast/publish/{results_date}')
    config.add_route(
        'results.forecast.publish',
        'nemo/results/forecast/publish/{results_date}')
    config.add_route(
        'results.forecast2.publish',
        'nemo/results/forecast2/publish/{results_date}')
    config.add_route(
        'results.nowcast.research',
        'nemo/results/nowcast/research/{results_date}')
    config.add_route(
        'results.nowcast.comparison',
        'nemo/results/nowcast/comparison/{results_date}')
    config.add_route(
        'nowcast.logs',
        'nemo/nowcast/logs/{filename}')
    # Legacy routes
    config.add_route(
        'storm_surge.forecast.html',
        'storm-surge/forecast.html')
    config.add_route(
        'results.index.html',
        'nemo/results/index.html')
    config.add_route(
        'results.nowcast.publish.html',
        'nemo/results/nowcast/publish_{results_date}.html')
    config.add_route(
        'results.forecast.publish.html',
        'nemo/results/forecast/publish_{results_date}.html')
    config.add_route(
        'results.forecast2.publish.html',
        'nemo/results/forecast2/publish_{results_date}.html')
    config.add_route(
        'results.nowcast.research.html',
        'nemo/results/nowcast/research_{results_date}.html')
    config.add_route(
        'results.nowcast.comparison.html',
        'nemo/results/nowcast/comparison_{results_date}.html')


def _about_site_routes(config):
    config.add_route('about.contributors', 'contributors')
    config.add_route('about.contributors.html', 'contributors.html')


## TODO: Delete this function and the views.static_pages module
## once all pages have been converted to views.
def _catchall_static_pages(config):
    config.add_view(
        'salishsea_site.views.static_pages.static_page',
        route_name='catchall_static')
    config.add_route('catchall_static', '/*subpath')