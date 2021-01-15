# Copyright 2014-2021 The Salish Sea MEOPAR Contributors
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
"""Unit tests for salishseacast views module.
"""
from unittest.mock import patch

import arrow

import salishsea_site.views.figures


class TestImageLoop:
    """Unit tests for ImageLoop class."""

    def test_first_available(self):
        img_loop = salishsea_site.views.figures.ImageLoop(
            model_var="salinity",
            metadata=salishsea_site.views.figures.FigureMetadata(
                title="Salinity Fields Along Thalweg and on Surface",
                link_text="Salinity",
                svg_name="salinity_thalweg_and_surface",
            ),
        )
        with patch(
            "salishsea_site.views.salishseacast.Path.exists",
            return_value=True,
            autospec=True,
        ):
            assert img_loop.available("nowcast", arrow.get("2018-12-14"))

    def test_subsequent_available(self):
        img_loop = salishsea_site.views.figures.ImageLoop(
            model_var="salinity",
            metadata=salishsea_site.views.figures.FigureMetadata(
                title="Salinity Fields Along Thalweg and on Surface",
                link_text="Salinity",
                svg_name="salinity_thalweg_and_surface",
            ),
        )
        with patch(
            "salishsea_site.views.salishseacast.Path.exists", autospec=True
        ) as p_exists:
            p_exists.side_effect = (False, False, True)
            assert img_loop.available("nowcast", arrow.get("2018-12-14"))

    def test_none_available(self):
        img_loop = salishsea_site.views.figures.ImageLoop(
            model_var="salinity",
            metadata=salishsea_site.views.figures.FigureMetadata(
                title="Salinity Fields Along Thalweg and on Surface",
                link_text="Salinity",
                svg_name="salinity_thalweg_and_surface",
            ),
        )
        with patch(
            "salishsea_site.views.salishseacast.Path.exists",
            return_value=False,
            autospec=True,
        ):
            assert not img_loop.available("nowcast", arrow.get("2018-12-14"))
