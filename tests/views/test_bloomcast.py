# Copyright 2013-2017 The Salish Sea MEOPAR Contributors
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

"""Unit tests for bloomcast views module.

.. note:: :py:func:`pconfig` fixture is defined in :file:`tests/conftest.py`.
"""
from pathlib import Path
from unittest.mock import patch

import datetime
from pyramid.threadlocal import get_current_request

from salishsea_site.views import bloomcast


class TestAbout:
    """Unit tests for bloomcast about view.
    """

    def test_about(self):
        request = get_current_request()
        data = bloomcast.about(request)
        assert data['ec_database_year'] == datetime.date.today().year


@patch('salishsea_site.views.bloomcast.Path', spec=Path)
class TestSpringDiatoms:
    """Unit tests for bloomcast sprint_diatoms view.
    """

    def test_spring_diatoms(self, m_path):
        m_path().__truediv__().open().__enter__.side_effect = (
            'run_start_date: 2016-09-19\n'  # latest_bloomcast.yaml
            'data_date: 2017-01-25\n'
            'prediction:\n'
            '  early: 2005\n'
            'bloom_dates:\n'
            '  1981: "2017-03-19"\n'
            'ts_plot_files:\n'
            '  mld_wind: mld_wind_timeseries.svg\n'
            'profiles_plot_file: profiles.svg\n',
            ['2017-01-25  2017-03-20  2004'],  # bloom_date_evolution.log
        )
        request = get_current_request()
        data = bloomcast.spring_diatoms(request)
        assert 'run_start_date' in data
        assert 'data_date' in data
        assert 'prediction' in data
        assert 'bloom_dates' in data
        assert 'ts_plot_files' in data
        assert 'profiles_plot_file' in data
        assert 'bloom_date_log' in data