# Copyright 2014-2020 The Salish Sea MEOPAR Contributors
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
"""salishsea_site Bloomcast views
"""
import datetime
import logging
from pathlib import Path

import arrow
import yaml
from pyramid.view import view_config

logger = logging.getLogger(__name__)


@view_config(route_name="bloomcast.about", renderer="bloomcast/about.mako")
@view_config(route_name="bloomcast.index.html", renderer="bloomcast/about.mako")
def about(request):
    return {"ec_database_year": datetime.date.today().year}


@view_config(
    route_name="bloomcast.spring_diatoms", renderer="bloomcast/spring_diatoms.mako"
)
@view_config(
    route_name="bloomcast.spring_diatoms.html", renderer="bloomcast/spring_diatoms.mako"
)
def spring_diatoms(request):
    plots_path = Path("/results/nowcast-sys/figures/bloomcast")
    with (plots_path / "latest_bloomcast.yaml").open("rt") as f:
        latest_bloomcast = yaml.safe_load(f)
    with (plots_path / "bloom_date_evolution.log").open("rt") as f:
        bloom_date_log = [line.split() for line in f if not line.startswith("#")]
    bloom_date_log.reverse()
    data_date = arrow.get(latest_bloomcast["data_date"])
    forecast_date = data_date.shift(days=+1).format("YYYY-MM-DD")
    latest_bloomcast.update(
        {
            "forecast_date": forecast_date,
            "plots_path": plots_path,
            "bloom_date_log": bloom_date_log,
        }
    )
    return latest_bloomcast
