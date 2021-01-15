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

.. note:: :py:func:`pconfig` fixture is defined in :file:`tests/conftest.py`.
"""
import os
from pathlib import Path
from unittest.mock import call, patch

import arrow
import pytest
from pyramid.httpexceptions import HTTPNotFound
from pyramid.threadlocal import get_current_request

from salishsea_site.views import salishseacast


class TestStormSurgePortal:
    """Unit tests for storm_surge_portal view."""

    def test_storm_surge_portal(self):
        request = get_current_request()
        data = salishseacast.storm_surge_portal(request)
        assert data == {}


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast._data_for_publish_template")
class TestStormSurgeForecast:
    """Unit tests for storm_surge_forecast view."""

    def test_no_forecast(self, m_dfpt):
        m_dfpt.side_effect = HTTPNotFound
        request = get_current_request()
        with patch("salishsea_site.views.salishseacast.arrow.now") as m_now:
            m_now.return_value = arrow.get("2016-11-06 18:09:42+07:00")
            with pytest.raises(HTTPNotFound):
                salishseacast.storm_surge_forecast(request)

    def test_forecast(self, m_dfpt):
        m_dfpt.side_effect = [{}, HTTPNotFound, HTTPNotFound]
        request = get_current_request()
        with patch("salishsea_site.views.salishseacast.arrow.now") as m_now:
            m_now.return_value = arrow.get("2016-11-06 18:09:42+07:00")
            data = salishseacast.storm_surge_forecast(request)
            assert data == {}
            expected = call(
                request,
                "forecast",
                m_now().floor("day").shift(days=+1),
                salishseacast.publish_figures,
                salishseacast.publish_tides_max_ssh_figure_group,
                m_now().floor("day"),
            )
            assert m_dfpt.call_args_list[0] == expected

    def test_forecast2(self, m_dfpt):
        m_dfpt.side_effect = [HTTPNotFound, {}, HTTPNotFound]
        request = get_current_request()
        with patch("salishsea_site.views.salishseacast.arrow.now") as m_now:
            m_now.return_value = arrow.get("2016-11-06 18:09:42+07:00")
            data = salishseacast.storm_surge_forecast(request)
            assert data == {}
            expected = call(
                request,
                "forecast2",
                m_now().floor("day").shift(days=+1),
                salishseacast.publish_figures,
                salishseacast.publish_tides_max_ssh_figure_group,
                m_now().floor("day").shift(days=-1),
            )
            assert m_dfpt.call_args_list[1] == expected

    def test_previous_forecast(self, m_dfpt):
        m_dfpt.side_effect = [HTTPNotFound, HTTPNotFound, {}]
        request = get_current_request()
        with patch("salishsea_site.views.salishseacast.arrow.now") as m_now:
            m_now.return_value = arrow.get("2016-11-06 18:09:42+07:00")
            data = salishseacast.storm_surge_forecast(request)
            assert data == {}
            expected = call(
                request,
                "forecast",
                m_now().floor("day"),
                salishseacast.publish_figures,
                salishseacast.publish_tides_max_ssh_figure_group,
                m_now().floor("day").shift(days=-1),
            )
            assert m_dfpt.call_args_list[2] == expected


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast.logger")
class TestStormSurgeAlertFeed:
    """Unit tests for storm_surge_alert_feed view."""

    def test_feed_file_not_found(self, m_logger, pconfig):
        pconfig.add_settings(nowcast_figures_server_name="nowcast-sys/figures/")
        pconfig.add_static_view(
            name="nowcast-sys/figures/", path="/results/nowcast-sys/figures"
        )
        request = get_current_request()
        request.registry = pconfig.registry
        request.matchdict = {"filename": "foo"}
        with pytest.raises(HTTPNotFound):
            salishseacast.storm_surge_alert_feed(request)
        assert m_logger.debug.called

    @patch("salishsea_site.views.salishseacast.Path", spec=Path)
    def test_render_feed_file(self, m_path, m_logger, pconfig):
        pconfig.add_settings(nowcast_figures_server_name="nowcast-sys/figures/")
        pconfig.add_static_view(
            name="nowcast-sys/figures/", path="/results/nowcast-sys/figures"
        )
        request = get_current_request()
        request.registry = pconfig.registry
        request.matchdict = {"filename": "foo"}
        m_path().__truediv__().open().read.return_value = "foo"
        response = salishseacast.storm_surge_alert_feed(request)
        assert response == "foo"
        assert request.response.content_type == "application/atom+xml"


class TestAboutSalishSeaCast:
    """Unit tests for SalishSeaCast about view."""

    def test_about(self):
        request = get_current_request()
        data = salishseacast.about(request)
        assert data == {}


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast.FigureMetadata.available")
class TestResultsIndex:
    """Unit tests for results_index view."""

    def test_first_date(self, m_available):
        m_available.return_value = True
        request = get_current_request()
        with patch("salishsea_site.views.salishseacast.arrow.now") as m_now:
            m_now.return_value = arrow.get("2016-11-06 13:05:42+07:00")
            data = salishseacast.results_index(request)
        assert data["first_date"] == arrow.get("2016-10-18 00:00:00+07:00")

    def test_last_date(self, m_available):
        m_available.return_value = True
        request = get_current_request()
        with patch("salishsea_site.views.salishseacast.arrow.now") as m_now:
            m_now.return_value = arrow.get("2016-11-06 13:09:42+07:00")
            data = salishseacast.results_index(request)
        assert data["last_date"] == arrow.get("2016-11-07 00:00:00+07:00")

    @pytest.mark.parametrize(
        "now, this_month_cols, last_month_cols",
        [
            (arrow.get("2016-11-06 13:15:42+07:00"), 7, 14),
            (arrow.get("2016-10-30 13:15:42+07:00"), 21, 0),
            (arrow.get("2016-10-31 13:15:42+07:00"), 1, 20),
            (arrow.get("2016-10-19 13:15:42+07:00"), 20, 1),
            (arrow.get("2016-02-28 13:15:42+07:00"), 21, 0),
            (arrow.get("2016-02-29 13:15:42+07:00"), 1, 20),
            (arrow.get("2015-02-28 13:15:42+07:00"), 1, 20),
            (arrow.get("2016-12-30 13:15:42+07:00"), 21, 0),
            (arrow.get("2016-12-31 13:15:42+07:00"), 1, 20),
            (arrow.get("2017-01-06 13:15:42+07:00"), 7, 14),
        ],
    )
    def test_month_cols(self, m_available, now, this_month_cols, last_month_cols):
        m_available.return_value = True
        request = get_current_request()
        with patch("salishsea_site.views.salishseacast.arrow.now") as m_now:
            m_now.return_value = now
            data = salishseacast.results_index(request)
        assert data["this_month_cols"] == this_month_cols
        assert data["last_month_cols"] == last_month_cols

    @patch("salishsea_site.views.salishseacast._exclude_missing_dates")
    def test_grid_dates(self, m_exlude_missing_dates, m_available):
        m_available.return_value = True
        request = get_current_request()
        with patch("salishsea_site.views.salishseacast.arrow.now") as m_now:
            m_now.return_value = arrow.get("2016-11-06 13:09:42+07:00")
            data = salishseacast.results_index(request)
        expected = {
            "prelim storm surge forecast": m_exlude_missing_dates(),
            "storm surge forecast": m_exlude_missing_dates(),
            "prelim surface currents forecast": m_exlude_missing_dates(),
            "surface currents forecast": m_exlude_missing_dates(),
            "nowcast currents": m_exlude_missing_dates(),
            "nowcast biology": m_exlude_missing_dates(),
            "nowcast timeseries": m_exlude_missing_dates(),
            "nowcast comparison": m_exlude_missing_dates(),
        }
        assert data["grid_dates"] == expected

    @pytest.mark.parametrize(
        "figures, figs_type, run_type, model",
        [
            (salishseacast.publish_figures, "publish", "forecast", "nemo"),
            (salishseacast.publish_figures, "publish", "forecast2", "nemo"),
            (
                salishseacast.surface_currents_image_loops,
                "publish",
                "forecast",
                "surface currents",
            ),
            (
                salishseacast.surface_currents_image_loops,
                "publish",
                "forecast2",
                "surface currents",
            ),
            (salishseacast.currents_physics_figures, "currents", "nowcast", "nemo"),
            (salishseacast.biology_image_loops, "biology", "nowcast-green", "nemo"),
            (
                salishseacast.timeseries_figure_group,
                "timeseries",
                "nowcast-green",
                "nemo",
            ),
            (salishseacast.comparison_figures, "comparison", "nowcast", "nemo"),
        ],
    )
    @patch("salishsea_site.views.salishseacast._exclude_missing_dates")
    def test_exclude_missing_dates_calls(
        self, m_exlude_missing_dates, m_available, figures, figs_type, run_type, model
    ):
        m_available.return_value = True
        request = get_current_request()
        with patch("salishsea_site.views.salishseacast.arrow.now") as m_now:
            m_now.return_value = arrow.get("2016-11-06 13:09:42+07:00")
            salishseacast.results_index(request)
        fcst_date = m_now().floor("day").shift(days=+1)
        dates = list(arrow.Arrow.range("day", fcst_date.shift(days=-20), fcst_date))
        expected = call(dates, figures, figs_type, run_type, model)
        assert expected in m_exlude_missing_dates.call_args_list


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast._data_for_publish_template")
class TestForecastPublish:
    """Unit test for forecast_publish view view."""

    def test_forecast_publish(self, m_dfpt):
        request = get_current_request()
        request.matchdict = {"results_date": "04nov16"}
        salishseacast.forecast_publish(request)
        m_dfpt.assert_called_once_with(
            request,
            "forecast",
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-03"),
        )


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast._data_for_publish_template")
class TestForecast2Publish:
    """Unit test for forecast2_publish view view."""

    def test_forecast2_publish(self, m_dfpt):
        request = get_current_request()
        request.matchdict = {"results_date": "04nov16"}
        salishseacast.forecast2_publish(request)
        m_dfpt.assert_called_once_with(
            request,
            "forecast2",
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-02"),
        )


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast.FigureMetadata.available")
class TestCurrentsPhysics:
    """Unit tests for nowcast_currents_physics view."""

    def test_no_figures_raises_httpnotfound(self, m_available):
        request = get_current_request()
        m_available.return_value = False
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_currents_physics(request)

    def test_results_date(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        m_available.return_value = True
        data = salishseacast.nowcast_currents_physics(request)
        assert data["results_date"] == arrow.get("2016-11-06")

    def test_run_type(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        m_available.return_value = True
        data = salishseacast.nowcast_currents_physics(request)
        assert data["run_type"] == "nowcast"

    def test_run_date(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        m_available.return_value = True
        data = salishseacast.nowcast_currents_physics(request)
        assert data["run_date"] == arrow.get("2016-11-06")

    def test_figures(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        m_available.return_value = True
        data = salishseacast.nowcast_currents_physics(request)
        assert data["figures"] == salishseacast.currents_physics_figures


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast.ImageLoop.available")
class TestBiology:
    """Unit tests for nowcast_biology view."""

    def test_no_figures_raises_httpnotfound(self, m_available):
        request = get_current_request()
        m_available.return_value = False
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_biology(request)

    def test_results_date(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "07may17"}
        m_available.return_value = True
        data = salishseacast.nowcast_biology(request)
        assert data["results_date"] == arrow.get("2017-05-07")

    def test_run_type(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "07may17"}
        m_available.return_value = True
        data = salishseacast.nowcast_biology(request)
        assert data["run_type"] == "nowcast-green"

    def test_run_date(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "07may17"}
        m_available.return_value = True
        data = salishseacast.nowcast_biology(request)
        assert data["run_date"] == arrow.get("2017-05-07")

    def test_image_loop(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "07may17"}
        m_available.return_value = True
        data = salishseacast.nowcast_biology(request)
        assert data["image_loops"] == salishseacast.biology_image_loops


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast.FigureGroup.available")
class TestTimeseries:
    """Unit tests for nowcast_timeseries view."""

    def test_no_figures_raises_httpnotfound(self, m_available):
        request = get_current_request()
        m_available.return_value = []
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_timeseries(request)

    def test_results_date(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "27jun17"}
        m_available.return_value = [True]
        data = salishseacast.nowcast_timeseries(request)
        assert data["results_date"] == arrow.get("2017-06-27")

    def test_run_type(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "27jun17"}
        m_available.return_value = [True]
        data = salishseacast.nowcast_timeseries(request)
        assert data["run_type"] == "nowcast-green"

    def test_run_date(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "27jun17"}
        m_available.return_value = [True]
        data = salishseacast.nowcast_timeseries(request)
        assert data["run_date"] == arrow.get("2017-06-27")

    def test_figures(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "27jun17"}
        m_available.return_value = [True]
        data = salishseacast.nowcast_timeseries(request)
        assert data["figures"] == salishseacast.timeseries_figure_group


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast.FigureMetadata.available")
class TestNowcastComparison:
    """Unit tests for nowcast_comparison view."""

    def test_no_figures_raises_httpnotfound(self, m_available):
        request = get_current_request()
        m_available.return_value = False
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_comparison(request)

    def test_results_date(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        m_available.return_value = True
        data = salishseacast.nowcast_comparison(request)
        assert data["results_date"] == arrow.get("2016-11-06")

    def test_run_type(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        m_available.return_value = True
        data = salishseacast.nowcast_comparison(request)
        assert data["run_type"] == "nowcast"

    def test_run_date(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        m_available.return_value = True
        data = salishseacast.nowcast_comparison(request)
        assert data["run_date"] == arrow.get("2016-11-06")

    def test_figure_links(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        m_available.return_value = True
        data = salishseacast.nowcast_comparison(request)
        expected = [fig.title for fig in salishseacast.comparison_figures]
        expected.append(salishseacast.onc_venus_comparison_figure_group.description)
        assert data["figure_links"] == expected

    def test_figures(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        m_available.return_value = True
        data = salishseacast.nowcast_comparison(request)
        assert data["figures"] == salishseacast.comparison_figures

    def test_onc_venus_figures(self, m_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        m_available.return_value = True
        data = salishseacast.nowcast_comparison(request)
        expected = salishseacast.onc_venus_comparison_figure_group
        assert data["onc_venus_figures"] == expected


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast.FigureMetadata.available")
class TestDataForPublishTemplate:
    """Unit test for _data_for_publish_template view utility function."""

    def test_no_alerts_fig_raises_httpnotfound(self, m_available):
        request = get_current_request()
        m_available.return_value = False
        with pytest.raises(HTTPNotFound):
            salishseacast._data_for_publish_template(
                request,
                "nowcast",
                arrow.get("2016-11-04"),
                salishseacast.publish_figures,
                salishseacast.publish_tides_max_ssh_figure_group,
                arrow.get("2016-11-04"),
            )

    def test_results_date(self, m_available):
        request = get_current_request()
        m_available.return_value = True
        data = salishseacast._data_for_publish_template(
            request,
            "forecast",
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-03"),
        )
        assert data["results_date"] == arrow.get("2016-11-04")

    @pytest.mark.parametrize(
        "run_type, expected",
        [("forecast", "Forecast"), ("forecast2", "Preliminary Forecast")],
    )
    def test_run_type_title(self, m_available, run_type, expected):
        request = get_current_request()
        m_available.return_value = True
        data = salishseacast._data_for_publish_template(
            request,
            run_type,
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-04"),
        )
        assert data["run_type_title"] == expected

    def test_run_type(self, m_available):
        request = get_current_request()
        m_available.return_value = True
        data = salishseacast._data_for_publish_template(
            request,
            "forecast",
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-03"),
        )
        assert data["run_type"] == "forecast"

    def test_run_date(self, m_available):
        request = get_current_request()
        m_available.return_value = True
        data = salishseacast._data_for_publish_template(
            request,
            "forecast",
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-03"),
        )
        assert data["run_date"] == arrow.get("2016-11-03")

    def test_figures(self, m_available):
        request = get_current_request()
        m_available.return_value = True
        data = salishseacast._data_for_publish_template(
            request,
            "forecast",
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-03"),
        )
        assert data["figures"] == salishseacast.publish_figures

    def test_missing_figures(self, m_available):
        request = get_current_request()
        m_available.side_effect = (
            [True, True]
            + [False] * (len(salishseacast.publish_figures) - 1)
            + [True] * len(salishseacast.publish_tides_max_ssh_figure_group.figures)
        )
        data = salishseacast._data_for_publish_template(
            request,
            "forecast",
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-03"),
        )
        assert data["figures"] == [salishseacast.publish_figures[0]]


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast.logger")
class TestNowcastLogs:
    """Unit tests for nowcast_logs view."""

    def test_envvar_not_set(self, m_logger):
        request = get_current_request()
        request.matchdict = {"filename": "foo"}
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_logs(get_current_request())
        m_logger.warning.assert_called_once_with(
            "NOWCAST_LOGS environment variable is not set"
        )

    def test_log_file_not_found(self, m_logger):
        request = get_current_request()
        request.matchdict = {"filename": "foo"}
        with patch.dict(os.environ, NOWCAST_LOGS="logs/nowcast/"):
            with pytest.raises(HTTPNotFound):
                salishseacast.nowcast_logs(request)
        assert m_logger.debug.called

    @patch("salishsea_site.views.salishseacast.Path", spec=Path)
    def test_render_log_file(self, m_path, m_logger):
        request = get_current_request()
        request.matchdict = {"filename": "nowcast.log"}
        m_path().__truediv__().open().read.return_value = "foo"
        with patch.dict(os.environ, NOWCAST_LOGS="logs/nowcast/"):
            response = salishseacast.nowcast_logs(request)
        assert response == "foo"
