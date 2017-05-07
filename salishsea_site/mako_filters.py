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
"""salishsea-site app Mako template filter functions.
"""


def slug(text):
    """Transform text into an slug for use as a tag id or an anchor href.

    Spaces are replaced with hyphens, and the result is lower-cased.

    :param str text: Text to transform to a slug.

    :return: :py:obj:`text` with spaces replaced by hyphens, and the result
             lower-cased.
    :rtype: str
    """
    return text.replace(' ', '-').lower()
