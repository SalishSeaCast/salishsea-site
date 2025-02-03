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


"""Classes for managing results figures."""
import os
from pathlib import Path

import attr


@attr.s
class FigureMetadata:
    #: Figure title that appears on rendered page.
    title = attr.ib()
    #: SVG file name of figure, excluding date part and .svg extension.
    #: So, if the file name is Vic_maxSSH_05nov16.svg, the svg_name value
    #: is Vic_maxSSH.
    svg_name = attr.ib()
    #: Text to appear in list of choices for figure in group of figures.
    #: Clicking on this text will swap this figure into the figure group
    #: display elements.
    link_text = attr.ib(default="")

    FIG_DIR_TMPLS = {
        "nemo": "/results/nowcast-sys/figures/{run_type}/{run_dmy}/",
        "surface currents": "/results/nowcast-sys/figures/surface_currents/{run_type}/{run_dmy}/",
        "fvcom": "/results/nowcast-sys/figures/fvcom/{run_type}/{run_dmy}/",
        "wwatch3": "/results/nowcast-sys/figures/wwatch3/{run_type}/{run_dmy}/",
    }

    def available(self, run_type, run_date, model="nemo"):
        """Return a boolean indicating whether or not the figure is available
        on the static file server that provides figure files.

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param str model: Model name to use to select figures directory
                          template for figure file path construction;
                          'nemo' or 'fvcom'.

        :return: Figure is availability on the static figure file server.
        :rtype: boolean
        """
        return Path(self.path(run_type, run_date, model)).exists()

    def filename(self, run_dmy):
        """Return the figure file name.

        :param str run_dmy: Run date for which the figure was generated,
                            formatted like `06jul17`.

        :returns: Figure file name.
        :rtype: str
        """
        return "{svg_name}_{run_dmy}.svg".format(
            svg_name=self.svg_name, run_dmy=run_dmy
        )

    def path(self, run_type, run_date, model="nemo"):
        """Return the figure file path.

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param str model: Model name to use to select figures directory
                          template for figure file path construction;
                          'nemo' or 'fvcom'.

        :return: Figure file path.
        :rtype: str
        """
        run_dmy = run_date.format("DDMMMYY").lower()
        fig_dir = self.FIG_DIR_TMPLS[model].format(
            run_type=run_type, svg_name=self.svg_name, run_dmy=run_dmy
        )
        return os.path.join(fig_dir, self.filename(run_dmy))


@attr.s
class FigureGroup:
    #: Figure group description.
    #: Used in the list of plots to link to the figure group section of the
    #: page.
    #: Also used as the heading text for the figure selector,
    #: and as the basis for the figure group permalink slug.
    description = attr.ib()
    #: List of :py:class:`~salishsea_site.views.salishseacast.FigureMetadata`
    #: instances that make up the figure group.
    figures = attr.ib(default=[])

    def __iter__(self):
        return (figure for figure in self.figures)

    def available(self, run_type, run_date, model="nemo"):
        """Return a list of booleans indicating whether or not each of the
        figures in the group is available on the static file server that
        provides figure files.

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param str model: Model name to use to select figures directory
                          template for figure file path construction;
                          'nemo' or 'fvcom'.

        :return: Figures that are availability on the static figure file server.
        :rtype: list
        """
        return [figure.available(run_type, run_date, model) for figure in self.figures]


@attr.s
class ImageLoop:
    #: :py:class:`~salishsea_site.views.salishseacast.FigureMetaData` instance
    #: that describes the image loop figures.
    metadata = attr.ib()
    #: Name of the model variable that the loop displays.
    model_var = attr.ib()
    #: First hour in the day for which image loop figures are stored;
    #: e.g. 0 for hourly average NEMO fields, 1 for FVCOM fields
    first_hr = attr.ib(default=0)
    #: Minute within the hour for which image loop figures are stored;
    #: e.g. 30 for hourly average NEMO fields, 0 for FVCOM fields
    image_minute = attr.ib(default=30)

    @property
    def title(self):
        return self.metadata.title

    @property
    def link_text(self):
        return self.metadata.link_text

    def __iter__(self):
        return (self for i in range(1))

    def available(self, run_type, run_date, model="nemo"):
        """Return a boolean indicating whether or not any of the image loop
        figures are available on the static file server that provides figure
        files.

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :return: Run hours for which figures are available on the
                 static figure file server.
        :rtype: list of ints
        """
        for run_hr in range(self.first_hr, 24):
            if Path(self.path(run_type, run_date, run_hr, model)).exists():
                return True
        else:
            return False

    def hours(self, run_type, run_date, model="nemo", file_dates=[]):
        """Return a list of run hours for which image loop figures are
        available on the static file server that provides figure files.

        :param str run_type: Run type for which the figures were generated.

        :param run_date: Run date for which the figures were generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param str model: Model name to use to select figures directory
                          template for figure file path construction;
                          'nemo' or 'fvcom'.

        :param file_dates: Date for which to check figures availability;
                           defaults to ``run_date`` if empty.
                           Use for image loops that span more than one day.
        :type file_dates: iterable of :py:class:`arrow.Arrow`

        :return: Run hours for which figures are available on the
                 static figure file server.
        :rtype: list of ints
        """
        available_hrs = {}
        file_dates = file_dates or [run_date]
        for file_date in file_dates:
            available_hrs[file_date] = []
            for run_hr in range(24):
                if Path(
                    self.path(run_type, run_date, run_hr, model, file_date)
                ).exists():
                    available_hrs[file_date].append(run_hr)
        return available_hrs

    def filename(self, file_date, run_hr):
        """Return the figure file name.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param int run_hr: Run hour for which the figure was generated.

        :returns: Figure file name.
        :rtype: str
        """
        file_date = file_date.format("YYYYMMDD")
        return f"{self.metadata.svg_name}_{file_date}_{run_hr:02d}{self.image_minute:02d}00_UTC.png"

    def path(self, run_type, run_date, run_hr, model="nemo", file_date=""):
        """Return the figure file path.

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param int run_hr: Run hour for which the figure was generated.

        :param str model: Model name to use to select figures directory
                          template for figure file path construction;
                          'nemo' or 'fvcom'.

        :param file_date: Date for which to calculate figure file path;
                           defaults to ``run_date`` if empty.
                           Use for image loops that span more than one day.
        :type file_date: iterable of :py:class:`arrow.Arrow`

        :return: Figure file path.
        :rtype: str
        """
        run_dmy = run_date.format("DDMMMYY").lower()
        fig_dir = self.metadata.FIG_DIR_TMPLS[model].format(
            run_type=run_type, svg_name=self.metadata.svg_name, run_dmy=run_dmy
        )
        file_date = file_date or run_date
        return os.path.join(fig_dir, self.filename(file_date, run_hr))


@attr.s
class ImageLoopGroup:
    #: Image loop group description.
    #: Used in the list of plots to link to the image loop group section of the
    #: page.
    #: Also used as the heading text for the image loop selector,
    #: and as the basis for the image loop group permalink slug.
    description = attr.ib()
    #: List of :py:class:`~salishsea_site.views.salishseacast.ImageLoop`
    #: instances that make up the image loop group.
    loops = attr.ib(default=[])

    def __iter__(self):
        return (loop for loop in self.loops)

    def __getitem__(self, item):
        return self.loops[item]

    def available(self, run_type, run_date, model="nemo"):
        """Return a list of booleans indicating whether or not any of the image loop
        figures are available on the static file server that provides figure
        files.

        :param str run_type: Run type for which the figure was generated.

        :param run_date: Run date for which the figure was generated.
        :type run_date: :py:class:`arrow.Arrow`

        :param str model: Model name to use to select figures directory
                          template for figure file path construction;
                          'nemo' or 'fvcom'.

        :return: Figure is availability on the static figure file server.
        :rtype: list
        """
        return [loop.available(run_type, run_date, model) for loop in self.loops]
