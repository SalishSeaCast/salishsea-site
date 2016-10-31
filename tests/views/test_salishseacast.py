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
from unittest.mock import patch

from pyramid.httpexceptions import HTTPNotFound
from pyramid.threadlocal import get_current_request
import pytest

from salishsea_site.views import salishseacast


@pytest.mark.usefixtures('pconfig')
@patch('salishsea_site.views.salishseacast.logger')
class TestNowcastLogs:
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
