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


"""Unit tests for salishseacast views module.

.. note:: :py:func:`pconfig` fixture is defined in :file:`tests/conftest.py`.
"""
import logging
import os
from pathlib import Path
from unittest.mock import call, patch

import arrow
import pytest
from pyramid.httpexceptions import HTTPNotFound, HTTPForbidden
from pyramid.threadlocal import get_current_request

from salishsea_site.views import salishseacast


@pytest.fixture
def mock_figure_available(monkeypatch):
    def _figure_available(*args, **kwargs):
        return True

    monkeypatch.setattr(salishseacast.FigureMetadata, "available", _figure_available)


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

    @staticmethod
    @pytest.fixture
    def mock_now(monkeypatch):
        def _now():
            return arrow.get("2016-11-06 18:09:42+07:00")

        monkeypatch.setattr(salishseacast.arrow, "now", _now)

    def test_no_forecast(self, m_dfpt, mock_now):
        m_dfpt.side_effect = HTTPNotFound
        request = get_current_request()
        with pytest.raises(HTTPNotFound):
            salishseacast.storm_surge_forecast(request)

    def test_forecast(self, m_dfpt, mock_now):
        m_dfpt.side_effect = [{}, HTTPNotFound, HTTPNotFound]
        request = get_current_request()
        data = salishseacast.storm_surge_forecast(request)
        assert data == {}
        expected = call(
            request,
            "forecast",
            arrow.get("2016-11-06 18:09:42+07:00").floor("day").shift(days=+1),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-06 18:09:42+07:00").floor("day"),
        )
        assert m_dfpt.call_args_list[0] == expected

    def test_forecast2(self, m_dfpt, mock_now):
        m_dfpt.side_effect = [HTTPNotFound, {}, HTTPNotFound]
        request = get_current_request()
        data = salishseacast.storm_surge_forecast(request)
        assert data == {}
        expected = call(
            request,
            "forecast2",
            arrow.get("2016-11-06 18:09:42+07:00").floor("day").shift(days=+1),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-06 18:09:42+07:00").floor("day").shift(days=-1),
        )
        assert m_dfpt.call_args_list[1] == expected

    def test_previous_forecast(self, m_dfpt, mock_now):
        m_dfpt.side_effect = [HTTPNotFound, HTTPNotFound, {}]
        request = get_current_request()
        data = salishseacast.storm_surge_forecast(request)
        assert data == {}
        expected = call(
            request,
            "forecast",
            arrow.get("2016-11-06 18:09:42+07:00").floor("day"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-06 18:09:42+07:00").floor("day").shift(days=-1),
        )
        assert m_dfpt.call_args_list[2] == expected


@pytest.mark.usefixtures("pconfig")
class TestStormSurgeAlertFeed:
    """Unit tests for storm_surge_alert_feed view."""

    def test_feed_file_not_found(self, pconfig, caplog):
        pconfig.add_settings(nowcast_figures_server_name="nowcast-sys/figures/")
        pconfig.add_static_view(
            name="nowcast-sys/figures/", path="/results/nowcast-sys/figures"
        )
        request = get_current_request()
        request.registry = pconfig.registry
        request.matchdict = {"filename": "foo"}
        caplog.set_level(logging.DEBUG)
        with pytest.raises(HTTPNotFound):
            salishseacast.storm_surge_alert_feed(request)
        assert caplog.records[0].levelno == logging.DEBUG

    @patch("salishsea_site.views.salishseacast.Path", spec=Path)
    def test_render_feed_file(self, m_path, pconfig):
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
class TestResultsIndex:
    """Unit tests for results_index view."""

    @staticmethod
    @pytest.fixture
    def mock_now(monkeypatch):
        def _now():
            return arrow.get("2016-11-06 13:05:42+07:00")

        monkeypatch.setattr(salishseacast.arrow, "now", _now)

    def test_first_date(self, mock_figure_available, mock_now):
        request = get_current_request()
        data = salishseacast.results_index(request)
        assert data["first_date"] == arrow.get("2016-10-18 00:00:00+07:00")

    def test_last_date(self, mock_figure_available, mock_now):
        request = get_current_request()
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
    def test_month_cols(
        self, mock_figure_available, now, this_month_cols, last_month_cols, monkeypatch
    ):
        def mock_now():
            return now

        monkeypatch.setattr(salishseacast.arrow, "now", mock_now)
        request = get_current_request()
        data = salishseacast.results_index(request)
        assert data["this_month_cols"] == this_month_cols
        assert data["last_month_cols"] == last_month_cols

    @patch("salishsea_site.views.salishseacast._exclude_missing_dates")
    def test_grid_dates(self, m_exlude_missing_dates, mock_figure_available, mock_now):
        request = get_current_request()
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
        self,
        m_exclude_missing_dates,
        mock_figure_available,
        figures,
        figs_type,
        run_type,
        model,
        mock_now,
    ):
        request = get_current_request()
        salishseacast.results_index(request)
        fcst_date = arrow.get("2016-11-06 13:05:42+07:00").floor("day").shift(days=+1)
        dates = list(arrow.Arrow.range("day", fcst_date.shift(days=-20), fcst_date))
        expected = call(dates, figures, figs_type, run_type, model)
        assert expected in m_exclude_missing_dates.call_args_list


@pytest.mark.usefixtures("pconfig")
@patch("salishsea_site.views.salishseacast._data_for_publish_template")
class TestForecastPublish:
    """Unit test for forecast_publish view."""

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
    """Unit test for forecast2_publish view."""

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
class TestCurrentsPhysics:
    """Unit tests for nowcast_currents_physics view."""

    def test_no_figures_raises_httpnotfound(self, monkeypatch):
        def mock_figure_available(self, run_type, run_date):
            return False

        monkeypatch.setattr(
            salishseacast.FigureMetadata, "available", mock_figure_available
        )
        request = get_current_request()
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_currents_physics(request)

    def test_results_date(self, mock_figure_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        data = salishseacast.nowcast_currents_physics(request)
        assert data["results_date"] == arrow.get("2016-11-06")

    def test_run_type(self, mock_figure_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        data = salishseacast.nowcast_currents_physics(request)
        assert data["run_type"] == "nowcast"

    def test_run_date(self, mock_figure_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        data = salishseacast.nowcast_currents_physics(request)
        assert data["run_date"] == arrow.get("2016-11-06")

    def test_figures(self, mock_figure_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        data = salishseacast.nowcast_currents_physics(request)
        assert data["figures"] == salishseacast.currents_physics_figures


@pytest.mark.usefixtures("pconfig")
class TestBiology:
    """Unit tests for nowcast_biology view."""

    @staticmethod
    @pytest.fixture
    def mock_img_loop_available(monkeypatch):
        def _img_loop_available(self, run_type, run_date):
            return True

        monkeypatch.setattr(salishseacast.ImageLoop, "available", _img_loop_available)

    def test_no_figures_raises_httpnotfound(self, monkeypatch):
        def mock_img_loop_available(self, run_type, run_date):
            return False

        monkeypatch.setattr(
            salishseacast.ImageLoop, "available", mock_img_loop_available
        )

        request = get_current_request()
        request.matchdict = {"results_date": "07may17"}
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_biology(request)

    def test_results_date(self, mock_img_loop_available):
        request = get_current_request()
        request.matchdict = {"results_date": "07may17"}
        data = salishseacast.nowcast_biology(request)
        assert data["results_date"] == arrow.get("2017-05-07")

    def test_run_type(self, mock_img_loop_available):
        request = get_current_request()
        request.matchdict = {"results_date": "07may17"}
        data = salishseacast.nowcast_biology(request)
        assert data["run_type"] == "nowcast-green"

    def test_run_date(self, mock_img_loop_available):
        request = get_current_request()
        request.matchdict = {"results_date": "07may17"}
        data = salishseacast.nowcast_biology(request)
        assert data["run_date"] == arrow.get("2017-05-07")

    def test_image_loop(self, mock_img_loop_available):
        request = get_current_request()
        request.matchdict = {"results_date": "07may17"}
        data = salishseacast.nowcast_biology(request)
        assert data["image_loops"] == salishseacast.biology_image_loops


@pytest.mark.usefixtures("pconfig")
class TestTimeseries:
    """Unit tests for nowcast_timeseries view."""

    @staticmethod
    @pytest.fixture
    def mock_fig_group_available(monkeypatch):
        def _fig_group_available(*args, **kwargs):
            return [True]

        monkeypatch.setattr(
            salishseacast.FigureGroup, "available", _fig_group_available
        )

    def test_no_figures_raises_httpnotfound(self, monkeypatch):
        def mock_fig_group_available(*args, **kwargs):
            return []

        monkeypatch.setattr(
            salishseacast.FigureGroup, "available", mock_fig_group_available
        )

        request = get_current_request()
        request.matchdict = {"results_date": "27jun17"}
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_timeseries(request)

    def test_results_date(self, mock_fig_group_available):
        request = get_current_request()
        request.matchdict = {"results_date": "27jun17"}
        data = salishseacast.nowcast_timeseries(request)
        assert data["results_date"] == arrow.get("2017-06-27")

    def test_run_type(self, mock_fig_group_available):
        request = get_current_request()
        request.matchdict = {"results_date": "27jun17"}
        data = salishseacast.nowcast_timeseries(request)
        assert data["run_type"] == "nowcast-green"

    def test_run_date(self, mock_fig_group_available):
        request = get_current_request()
        request.matchdict = {"results_date": "27jun17"}
        data = salishseacast.nowcast_timeseries(request)
        assert data["run_date"] == arrow.get("2017-06-27")

    def test_figures(self, mock_fig_group_available):
        request = get_current_request()
        request.matchdict = {"results_date": "27jun17"}
        data = salishseacast.nowcast_timeseries(request)
        assert data["figures"] == salishseacast.timeseries_figure_group


@pytest.mark.usefixtures("pconfig")
class TestNowcastComparison:
    """Unit tests for nowcast_comparison view."""

    def test_no_figures_raises_httpnotfound(self, monkeypatch):
        def mock_figure_available(*args, **kwargs):
            return False

        monkeypatch.setattr(
            salishseacast.FigureMetadata, "available", mock_figure_available
        )
        request = get_current_request()
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_comparison(request)

    def test_results_date(self, mock_figure_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        data = salishseacast.nowcast_comparison(request)
        assert data["results_date"] == arrow.get("2016-11-06")

    def test_run_type(self, mock_figure_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        data = salishseacast.nowcast_comparison(request)
        assert data["run_type"] == "nowcast"

    def test_run_date(self, mock_figure_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        data = salishseacast.nowcast_comparison(request)
        assert data["run_date"] == arrow.get("2016-11-06")

    def test_figure_links(self, mock_figure_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        data = salishseacast.nowcast_comparison(request)
        expected = [fig.title for fig in salishseacast.comparison_figures]
        expected.append(salishseacast.onc_venus_comparison_figure_group.description)
        assert data["figure_links"] == expected

    def test_figures(self, mock_figure_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        data = salishseacast.nowcast_comparison(request)
        assert data["figures"] == salishseacast.comparison_figures

    def test_onc_venus_figures(self, mock_figure_available):
        request = get_current_request()
        request.matchdict = {"results_date": "06nov16"}
        data = salishseacast.nowcast_comparison(request)
        expected = salishseacast.onc_venus_comparison_figure_group
        assert data["onc_venus_figures"] == expected


@pytest.mark.usefixtures("pconfig")
class TestDataForPublishTemplate:
    """Unit test for _data_for_publish_template view utility function."""

    def test_no_alerts_fig_raises_httpnotfound(self, monkeypatch):
        def mock_figure_available(self, run_type, run_date):
            return False

        monkeypatch.setattr(
            salishseacast.FigureMetadata, "available", mock_figure_available
        )
        request = get_current_request()
        with pytest.raises(HTTPNotFound):
            salishseacast._data_for_publish_template(
                request,
                "nowcast",
                arrow.get("2016-11-04"),
                salishseacast.publish_figures,
                salishseacast.publish_tides_max_ssh_figure_group,
                arrow.get("2016-11-04"),
            )

    def test_results_date(self, mock_figure_available):
        request = get_current_request()
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
    def test_run_type_title(self, mock_figure_available, run_type, expected):
        request = get_current_request()
        data = salishseacast._data_for_publish_template(
            request,
            run_type,
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-04"),
        )
        assert data["run_type_title"] == expected

    def test_run_type(self, mock_figure_available):
        request = get_current_request()
        data = salishseacast._data_for_publish_template(
            request,
            "forecast",
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-03"),
        )
        assert data["run_type"] == "forecast"

    def test_run_date(self, mock_figure_available):
        request = get_current_request()
        data = salishseacast._data_for_publish_template(
            request,
            "forecast",
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-03"),
        )
        assert data["run_date"] == arrow.get("2016-11-03")

    def test_figures(self, mock_figure_available):
        request = get_current_request()
        data = salishseacast._data_for_publish_template(
            request,
            "forecast",
            arrow.get("2016-11-04"),
            salishseacast.publish_figures,
            salishseacast.publish_tides_max_ssh_figure_group,
            arrow.get("2016-11-03"),
        )
        assert data["figures"] == salishseacast.publish_figures

    @patch("salishsea_site.views.salishseacast.FigureMetadata.available")
    def test_missing_figures(self, m_figure_available):
        request = get_current_request()
        m_figure_available.side_effect = (
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
class TestNowcastLogs:
    """Unit tests for nowcast_logs view."""

    def test_nowcast_logs_envvar_not_set(self, caplog):
        request = get_current_request()
        request.matchdict = {"filename": "foo", "token": ""}
        caplog.set_level(logging.DEBUG)
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_logs(get_current_request())
        assert caplog.records[0].levelno == logging.WARNING
        assert caplog.messages[0] == "NOWCAST_LOGS environment variable is not set"

    def test_log_file_not_found(self, caplog, monkeypatch):
        request = get_current_request()
        request.matchdict = {"filename": "foo", "token": ""}
        monkeypatch.setenv("NOWCAST_LOGS", "logs/nowcast/")
        caplog.set_level(logging.DEBUG)
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_logs(request)
        assert caplog.records[0].levelno == logging.DEBUG

    def test_render_log_file(self, tmp_path, monkeypatch):
        test_log_file = tmp_path / "nowcast.log"
        test_log_file.write_text("foo")
        request = get_current_request()
        request.matchdict = {"filename": "nowcast.log", "token": ""}
        monkeypatch.setenv("NOWCAST_LOGS", os.fspath(tmp_path))
        response = salishseacast.nowcast_logs(request)
        assert response == "foo"

    def test_nowcast_debug_log_token_envvar_not_set(self, caplog, monkeypatch):
        request = get_current_request()
        request.matchdict = {"filename": "nowcast.debug.log", "token": ""}
        monkeypatch.setenv("NOWCAST_LOGS", "logs/nowcast/")
        caplog.set_level(logging.DEBUG)
        with pytest.raises(HTTPNotFound):
            salishseacast.nowcast_logs(get_current_request())
        assert caplog.records[0].levelno == logging.WARNING
        assert (
            caplog.messages[0]
            == "NOWCAST_DEBUG_LOG_TOKEN environment variable is not set"
        )

    @pytest.mark.parametrize("token", ["", "invalid"])
    def test_invalid_log_file_token(self, token, caplog, monkeypatch):
        request = get_current_request()
        request.matchdict = {"filename": "nowcast.debug.log", "token": token}
        caplog.set_level(logging.DEBUG)
        monkeypatch.setenv("NOWCAST_LOGS", "logs/nowcast/")
        monkeypatch.setenv("NOWCAST_DEBUG_LOG_TOKEN", "super-secret-token")
        with pytest.raises(HTTPForbidden):
            salishseacast.nowcast_logs(get_current_request())
        assert caplog.records[0].levelno == logging.WARNING
        assert caplog.messages[0] == "debug log file request token is invalid"

    def test_render_debug_log_file(self, tmp_path, monkeypatch):
        test_log_file = tmp_path / "nowcast.debug.log"
        test_log_file.write_text("foo")
        request = get_current_request()
        request.matchdict = {
            "filename": "nowcast.debug.log",
            "token": "super-secret-token",
        }
        monkeypatch.setenv("NOWCAST_LOGS", os.fspath(tmp_path))
        monkeypatch.setenv("NOWCAST_DEBUG_LOG_TOKEN", "super-secret-token")
        response = salishseacast.nowcast_logs(request)
        assert response == "foo"
