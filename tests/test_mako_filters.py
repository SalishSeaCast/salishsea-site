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


"""Unit tests for mako_filters module."""
import pytest

from salishsea_site import mako_filters


@pytest.mark.parametrize(
    "text, expected",
    [
        ("foo", "foo"),
        ("foo bar", "foo-bar"),
        ("foo Bar", "foo-bar"),
        ("foo-Bar", "foo-bar"),
        ("FOO BAR", "foo-bar"),
        ("foo - bar", "foo---bar"),
        ("foo — bar", "foo-—-bar"),
    ],
)
class TestSlug:
    def test_slug(self, text, expected):
        slug = mako_filters.slug(text)
        assert slug == expected
