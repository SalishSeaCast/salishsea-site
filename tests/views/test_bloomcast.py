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


"""Unit tests for bloomcast views module.

.. note:: :py:func:`pconfig` fixture is defined in :file:`tests/conftest.py`.
"""
import datetime
from pathlib import Path
from unittest.mock import patch

from pyramid.threadlocal import get_current_request

from salishsea_site.views import bloomcast


class TestAbout:
    """Unit tests for bloomcast about view."""

    def test_about(self):
        request = get_current_request()
        data = bloomcast.about(request)
        assert data["ec_database_year"] == datetime.date.today().year


@patch("salishsea_site.views.bloomcast.Path", spec=Path)
class TestSpringDiatoms:
    """Unit tests for bloomcast sprint_diatoms view."""

    def test_spring_diatoms(self, m_path):
        m_path().__truediv__().open().__enter__.side_effect = (
            # latest_bloomcast.yaml
            "run_start_date: 2016-09-19\n"
            "data_date: 2017-01-25\n"
            "prediction:\n"
            "  early: 2005\n"
            "bloom_dates:\n"
            '  1981: "2017-03-19"\n'
            "ts_plot_files:\n"
            "  mld_wind: mld_wind_timeseries.svg\n"
            "profiles_plot_file: profiles.svg\n",
            # bloom_date_evolution.log
            ["2017-01-24  2017-03-21  2007", "2017-01-25  2017-03-20  2004"],
        )
        request = get_current_request()
        data = bloomcast.spring_diatoms(request)
        assert data["run_start_date"] == datetime.date(2016, 9, 19)
        assert data["data_date"] == datetime.date(2017, 1, 25)
        assert data["prediction"] == {"early": 2005}
        assert data["bloom_dates"] == {1981: "2017-03-19"}
        assert data["ts_plot_files"] == {"mld_wind": "mld_wind_timeseries.svg"}
        assert data["profiles_plot_file"] == "profiles.svg"
        assert data["forecast_date"] == "2017-01-26"
        expected = m_path("/results/nowcast-sys/figures/bloomcast")
        assert data["plots_path"] == expected
        expected = [
            ["2017-01-25", "2017-03-20", "2004"],
            ["2017-01-24", "2017-03-21", "2007"],
        ]
        assert data["bloom_date_log"] == expected
