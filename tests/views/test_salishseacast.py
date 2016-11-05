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

"""Unit tests for salishseacast views module.

.. note:: :py:func:`pconfig` fixture is defined in :file:`tests/conftest.py`.
"""
import os
from pathlib import Path
from unittest.mock import (
    call,
    Mock,
    patch,
)

import arrow
import pytest
import requests
from pyramid.httpexceptions import HTTPNotFound
from pyramid.threadlocal import get_current_request

from salishsea_site.views import salishseacast


@pytest.mark.usefixtures('pconfig')
@patch('salishsea_site.views.salishseacast.requests.Session')
class TestFigureMetadata:
    """Unit tests for FigureMetadata class.
    """

    def test_available_in_production(self, m_session):
        request = get_current_request()
        request.static_url = Mock(name='static_url')
        figure = salishseacast.FigureMetadata(title='foo', svg_name='bar')
        figure.available(
            request, 'nowcast', arrow.get('2016-11-05'), m_session)
        request.static_url.assert_called_once_with(
            '/results/nowcast-sys/figures/nowcast/05nov16/bar_05nov16.svg')
        m_session.head.assert_called_once_with(request.static_url())

    def test_available_in_development(self, m_session):
        request = get_current_request()
        request.static_url = Mock(name='static_url')
        m_session.head.side_effect = (
            requests.ConnectionError, Mock(status_code=200))
        figure = salishseacast.FigureMetadata(title='foo', svg_name='bar')
        figure.available(
            request, 'nowcast', arrow.get('2016-11-05'), m_session)
        assert m_session.head.call_args == call(request.static_url().replace())


@pytest.mark.usefixtures('pconfig')
@patch('salishsea_site.views.salishseacast.logger')
class TestNowcastLogs:
    """Unit tests for nowcast_logs view function.
    """

    def test_envvar_not_Set(self, m_logger):
        request = get_current_request()
        request.matchdict = {'filename': 'foo'}
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_logs(get_current_request())
        m_logger.warning.assert_called_once_with(
            'NOWCAST_LOGS environment variable is not set')

    def test_log_file_not_found(self, m_logger):
        request = get_current_request()
        request.matchdict = {'filename': 'foo'}
        with patch.dict(os.environ, NOWCAST_LOGS='logs/nowcast/'):
            with pytest.raises(HTTPNotFound):
                salishseacast.nowcast_logs(request)
        assert m_logger.debug.called

    @patch('salishsea_site.views.salishseacast.Path', spec=Path)
    def test_render_log_file(self, m_path, m_logger):
        request = get_current_request()
        request.matchdict = {'filename': 'nowcast.log'}
        m_path().__truediv__().open().read.return_value = 'foo'
        with patch.dict(os.environ, NOWCAST_LOGS='logs/nowcast/'):
            response = salishseacast.nowcast_logs(request)
        assert response == 'foo'


@pytest.mark.usefixtures('pconfig')
@patch('salishsea_site.views.salishseacast._data_for_publish_template')
class TestNowcastPublish:
    """Unit test for nowcast_publish view function.
    """

    def test_nowcast_publish(self, m_dfpt):
        request = get_current_request()
        request.matchdict = {'results_date': '04nov16'}
        salishseacast.nowcast_publish(request)
        m_dfpt.assert_called_once_with(
            request, 'nowcast', arrow.get('2016-11-04'),
            salishseacast.publish_figures, run_date=arrow.get('2016-11-04'))


@pytest.mark.usefixtures('pconfig')
@patch('salishsea_site.views.salishseacast._data_for_publish_template')
class TestForecastPublish:
    """Unit test for forecast_publish view function.
    """

    def test_forecast_publish(self, m_dfpt):
        request = get_current_request()
        request.matchdict = {'results_date': '04nov16'}
        salishseacast.forecast_publish(request)
        m_dfpt.assert_called_once_with(
            request, 'forecast', arrow.get('2016-11-04'),
            salishseacast.publish_figures, arrow.get('2016-11-03'))


@pytest.mark.usefixtures('pconfig')
@patch('salishsea_site.views.salishseacast._data_for_publish_template')
class TestForecast2Publish:
    """Unit test for forecast2_publish view function.
    """

    def test_forecast2_publish(self, m_dfpt):
        request = get_current_request()
        request.matchdict = {'results_date': '04nov16'}
        salishseacast.forecast2_publish(request)
        m_dfpt.assert_called_once_with(
            request, 'forecast2', arrow.get('2016-11-04'),
            salishseacast.publish_figures, arrow.get('2016-11-02'))


@pytest.mark.usefixtures('pconfig')
@patch('salishsea_site.views.salishseacast.FigureMetadata.available')
class TestDataForPublishTemplate:
    """Unit test for _data_for_publish_template view utility functions.
    """

    def test_no_alerts_fig_raises_httpnotfound(self, m_available):
        request = get_current_request()
        m_available.return_value = False
        with pytest.raises(HTTPNotFound):
            salishseacast._data_for_publish_template(
                request, 'nowcast', arrow.get('2016-11-04'),
                salishseacast.publish_figures, arrow.get('2016-11-04'))

    def test_results_date(self, m_available):
        request = get_current_request()
        m_available.return_value = True
        data = salishseacast._data_for_publish_template(
            request, 'forecast',
            arrow.get('2016-11-04'), salishseacast.publish_figures,
            arrow.get('2016-11-03'))
        assert data['results_date'] == arrow.get('2016-11-04')

    @pytest.mark.parametrize('run_type, expected', [
        ('nowcast', 'Nowcast'),
        ('forecast', 'Forecast'),
        ('forecast2', 'Preliminary Forecast'),
    ])
    def test_run_type_title(self, m_available, run_type, expected):
        request = get_current_request()
        m_available.return_value = True
        data = salishseacast._data_for_publish_template(
            request, run_type,
            arrow.get('2016-11-04'), salishseacast.publish_figures,
            arrow.get('2016-11-04'))
        assert data['run_type_title'] == expected

    def test_run_type(self, m_available):
        request = get_current_request()
        m_available.return_value = True
        data = salishseacast._data_for_publish_template(
            request, 'forecast',
            arrow.get('2016-11-04'), salishseacast.publish_figures,
            arrow.get('2016-11-03'))
        assert data['run_type'] == 'forecast'

    def test_run_date(self, m_available):
        request = get_current_request()
        m_available.return_value = True
        data = salishseacast._data_for_publish_template(
            request, 'forecast',
            arrow.get('2016-11-04'), salishseacast.publish_figures,
            arrow.get('2016-11-03'))
        assert data['run_date'] == arrow.get('2016-11-03')

    def test_figures(self, m_available):
        request = get_current_request()
        m_available.return_value = True
        data = salishseacast._data_for_publish_template(
            request, 'forecast',
            arrow.get('2016-11-04'), salishseacast.publish_figures,
            arrow.get('2016-11-03'))
        assert data['figures'] == salishseacast.publish_figures

    def test_missing_figures(self, m_available):
        request = get_current_request()
        m_available.side_effect = (
            [True, True] + [False] * (len(salishseacast.publish_figures) - 1))
        data = salishseacast._data_for_publish_template(
            request, 'forecast',
            arrow.get('2016-11-04'), salishseacast.publish_figures,
            arrow.get('2016-11-03'))
        assert data['figures'] == [salishseacast.publish_figures[0]]
