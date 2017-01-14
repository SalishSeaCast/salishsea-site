# Copyright 2013-2017 The Salish Sea MEOPAR Contributors
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

"""Unit tests for bloomcast views module.

.. note:: :py:func:`pconfig` fixture is defined in :file:`tests/conftest.py`.
"""
from unittest.mock import patch

import datetime
from pyramid.threadlocal import get_current_request

from salishsea_site.views import bloomcast


class TestBloomcastAbout:
    """Unit tests for bloomcast about view.
    """

    def test_storm_surge_portal(self):
        request = get_current_request()
        data = bloomcast.about(request)
        assert data['ec_database_year'] == datetime.date.today().year
