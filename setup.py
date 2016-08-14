# Copyright 2013-2016 The Salish Sea MEOPAR Contributors
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

"""Pyramid web app that serves the salishsea.eos.ubc.ca site
"""
import os

from setuptools import (
    find_packages,
    setup,
)

import __pkg_metadata__


python_classifiers = [
    'Programming Language :: Python :: {0}'.format(py_version)
    for py_version in ['3', '3.5']]
other_classifiers = [
    'Development Status :: ' + __pkg_metadata__.DEV_STATUS,
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: Implementation :: CPython',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Framework :: Pyramid',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
]

here = os.path.abspath(os.path.dirname(__file__))
try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

install_requires = [
    # see environment-prod.yaml for conda environment production installation,
    # see environment-dev.yaml for conda environment dev installation,
    # see requirements.txt for package versions used during recent development
    'pyramid',
    'pyramid_crow',
    'pyramid_mako',
    'waitress',
]

setup(
    name=__pkg_metadata__.PROJECT,
    version=__pkg_metadata__.VERSION,
    description=__pkg_metadata__.DESCRIPTION,
    long_description=long_description,
    author='Doug Latornell',
    author_email='dlatornell@eos.ubc.ca',
    url='https://salishsea-site.readthedocs.io/en/latest/',
    license='Apache License, Version 2.0',
    classifiers=python_classifiers + other_classifiers,
    keywords='web pyramid pylons',
    platforms=['Linux'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""\
    [paste.app_factory]
    main = salishsea_site:main
    """,
)
