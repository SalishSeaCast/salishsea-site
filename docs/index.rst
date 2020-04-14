.. Copyright 2014-2020 The Salish Sea MEOPAR contributors
.. and The University of British Columbia
..
.. Licensed under the Apache License, Version 2.0 (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..
..    https://www.apache.org/licenses/LICENSE-2.0
..
.. Unless required by applicable law or agreed to in writing, software
.. distributed under the License is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.


.. _SalishSeaSiteWebApp:

*********************************
salishsea.eos.ubc.ca Site Web App
*********************************

The `salishsea.eos.ubc.ca`_ site is a dynamic web application written in `Python`_ 3 using the `Pyramid web framework`_.
These docs provide a brief explanation of the structure of the app,
and details about its development.

.. _salishsea.eos.ubc.ca: https://salishsea.eos.ubc.ca/
.. _Python: https://www.python.org/
.. _Pyramid web framework: https://docs.pylonsproject.org/projects/pyramid/en/latest/index.html

If you are new to Python web frameworks you should probably start by reading the `Pyramid Hello World`_ docs,
and then maybe proceed to the `Quick Tutorial`_.

If you have experience with any of the many other Python web frameworks such as Django,
flask,
bottle,
etc. you could start with the `Quick Tutorial`_,
or dive into the `narrative documentation`_.

.. _Pyramid Hello World: https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/firstapp.html#firstapp-chapter
.. _Quick Tutorial: https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html
.. _narrative documentation: https://docs.pylonsproject.org/projects/pyramid/en/latest/index.html#narrative-documentation


.. _salishSeaSiteStructure:

App Structure
-------------

The :file:`salishsea_site` directory tree contains the app package:

* The app configuration is defined in :file:`salishsea_site/__init__.py`.
  That file also contains functions that `map URL paths to route names`_.
  It also contains static view functions that serve the site static assets
  (see below)
  and model run results figures and other static files produced by the Salish Sea NEMO and SOG 1-D models.

  .. _map URL paths to route names: https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/urldispatch.html

* The :file:`salishsea_site/views/` directory contains Python modules that define the `view functions`_ that the routes connect to.
  The view functions handle the HTTP requests coming into the app,
  and calculate the dynamic elements of the responses which are returned by the functions as :py:class:`dict` objects.
  The view modules are organized to correspond to the site's top-of-page navigation bar.

  .. _view functions: https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/views.html

* The :file:`salishsea_site/templates/` directory tree contains the `page templates`_ that the view functions pass to the renderer to produce the HTML stream that is sent to the user's browser in the HTTP response.
  The :py:class:`dict` objects returned by the view functions contain the template variable names and the values to substitute for them.
  The templates are written in `HTML5`_.
  They use the `Bootstrap 3`_ HTML/CSS/JS framework for layout and client-side dynamic elements.
  The `Mako template library`_ is used to provide variable substitution,
  inheritance,
  and flow control in the templates.
  The templates are organized in sub-directories that correspond to the view modules.

  .. _page templates: https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/templates.html
  .. _HTML5: https://developer.mozilla.org/en/docs/Web/Guide/HTML/HTML5
  .. _Bootstrap 3: https://getbootstrap.com/
  .. _Mako template library: https://www.makotemplates.org/

* The :file:`salishsea_site/static/` directory tree contains the app's static assets,
  CSS files,
  images,
  and PDF documents.
  They are served by a static view defined in :file:`salishsea_site/__init__.py`.

The runtime configurations for running the app in a development environment,
and for its production deployment are contained in the :file:`development.ini` and :file:`production.ini` files in the top level of the repository.

Please see :ref:`SalishSeaSiteDevelopment` for details of how to set up an app development environment,
and :ref:`SalishSeaSiteRunningDevApp` for instructions on how to run the app in development mode on your local machine.

The :file:`tests/` directory tree contains the unit test suite for the package.
It is intended to be run using the `pytest`_ tool.
Please see :ref:`SalishSeaSiteRunningTheUnitTests` for details.

.. _pytest: https://docs.pytest.org/en/latest/

The :file:`docs/` directory tree contains the `reStructuredText`_ source files for these docs,
and the `Sphinx` configuration and :file:`Makefile` to render them to HTML.
Please see :ref:`SalishSeaSiteBuildingTheDocumentation` for details.

.. _reStructuredText: https://www.sphinx-doc.org/en/stable/rest.html
.. _Sphinx: https://www.sphinx-doc.org/en/stable/rest.html


.. _SalishSeaSiteDevelopment:

Web App Package Development
===========================

.. _SalishSeaSitePythonVersions:

Python Versions
---------------

.. image:: https://img.shields.io/badge/python-3.6+-blue.svg
    :target: https://docs.python.org/3.7/
    :alt: Python Version

The :kbd:`salishsea-site` package is developed,
tested,
and deployed using `Python`_ 3.6 or later.
The package uses some Python language features that are not available in versions prior to 3.6,
in particular:

* `Formatted string literals`_
  (aka *f-strings*)
* the `file system path protocol`_

.. _Formatted string literals: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
.. _file system path protocol: https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep519


.. _SalishSeaSiteGettingTheCode:

Getting the Code
----------------

.. image:: https://img.shields.io/badge/version%20control-hg-blue.svg
    :target: https://bitbucket.org/salishsea/salishsea-site/
    :alt: Mercurial on Bitbucket

Clone the :ref:`salishsea-site-repo` code and documentation `repository`_ from Bitbucket with:

.. _repository: https://bitbucket.org/salishsea/salishsea-site/

.. code-block:: bash

    $ hg clone ssh://hg@bitbucket.org/salishsea/salishsea-site

or

.. code-block:: bash

    $ hg clone https://<your_userid>@bitbucket.org/salishsea/salishsea-site

if you don't have `ssh key authentication`_ set up on Bitbucket.

.. _ssh key authentication: https://confluence.atlassian.com/bitbucket/set-up-ssh-for-mercurial-728138122.html


.. _SalishSeaSiteDevelopmentEnvironment:

Development Environment
=======================

Setting up an isolated development environment using `Conda`_ is strongly recommended.
Assuming that you have :ref:`AnacondaPythonDistro` or `Miniconda3`_ installed,
you can create and activate an environment called :kbd:`salishsea-site` that will have all of the Python packages necessary for development,
testing,
and building the documentation with the commands:

.. _Conda: https://conda.io/docs/
.. _Miniconda3: https://conda.io/docs/install/quick.html

.. code-block:: bash

    $ cd salishsea-site
    $ conda env create -f env/environment-dev.yaml
    $ source activate salishsea-site
    (salishsea-site)$ python3 -m pip install --editable .

The :kbd:`--editable` option in the :command:`pip install` commands above installs the :kbd:`salishsea-site` package via a symlink so that it is automatically updated as the repo evolves.

To deactivate the environment use:

.. code-block:: bash

    (salishsea-site)$ source deactivate


.. _SalishSeaSiteCodingStyle:

Coding Style
------------

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://black.readthedocs.io/en/stable/
    :alt: The uncompromising Python code formatter

The :kbd:`salishsea-site` package uses the `black`_ code formatting tool to maintain a coding style that is very close to `PEP 8`_.

.. _black: https://black.readthedocs.io/en/stable/
.. _PEP 8: https://www.python.org/dev/peps/pep-0008/

:command:`black` is installed as part of the :ref:`SalishSeaSiteDevelopmentEnvironment` setup.

o run :command:`black` on the entire code-base use:

.. code-block:: bash

    $ cd SalishSeaCmd
    $ conda activate salishsea-cmd
    (salishsea-cmd)$ black ./

in the repository root directory.
The output looks something like::

  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/salishsea_site/mako_filters.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/salishsea_site/views/site.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/salishsea_site/views/about.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/salishsea_site/views/bloomcast.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/tests/conftest.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/tests/test_mako_filters.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/tests/views/test_bloomcast.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/tests/views/test_figures.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/salishsea_site/views/wwatch3.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/salishsea_site/views/figures.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/salishsea_site/__init__.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/salishsea_site/views/fvcom.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/tests/views/test_salishseacast.py
  reformatted /media/doug/warehouse/MEOPAR/salishsea-site/salishsea_site/views/salishseacast.py
  All done! ✨ 🍰 ✨
  14 files reformatted, 4 file left unchanged.


.. _SalishSeaSiteRunningDevApp:

Running the App in Dev Mode
---------------------------

You can run the app in a development server on you local machine with the command:

.. code-block:: bash

    (salishsea-site)$ cd salishsea-site
    (salishsea-site)$ pserve --reload development.ini

With the dev server running you can view the site by navigating to :kbd:`http://localhost:6543/` in your browser.

The :kbd:`--reload` option in the :command:`pserve` command causes the dev server to monitor the app files in the :file:`salishsea-site/` directory tree and restart whenever it detects that a file has been changed.
That allows you to easily edit app code and templates and instantly see changes in your browser after a page refresh.

Logger messages from the app appear in the terminal session where you ran the :command:`pserve` command.

To stop the dev server use :kbd:`Ctrl-C` in the terminal session where you ran the :command:`pserve` command.

.. note::
    Several pages in the app require access to parts of the :file:`/results/` directory tree on :kbd:`skookum`.
    If you are working on a waterhole machine that has :file:`/results/` mounted,
    you are good to go.
    If you need to get :file:`/results/` mounted on a waterhole machine,
    please open an EOAS IT ticket with the request.
    If you are working on a remote machine or a laptop you can use :program:`sshfs` to mount :file:`/results/` from :kbd:`skookum` at a local :file:`/results/` mount point.


.. _SalishSeaSiteBuildingTheDocumentation:

Building the Documentation
--------------------------

.. image:: https://readthedocs.org/projects/salishsea-site/badge/?version=latest
    :target: https://salishsea-site.readthedocs.io/en/latest/
    :alt: Documentation Status

The documentation for the :kbd:`salishsea-site` package is written in `reStructuredText`_ and converted to HTML using `Sphinx`_.
Creating a :ref:`SalishSeaSiteDevelopmentEnvironment` as described above includes the installation of Sphinx.
Building the documentation is driven by :file:`docs/Makefile`.
With your :kbd:`salishsea-site` development environment activated,
use:

.. code-block:: bash

    (salishsea-site)$ (cd docs && make clean html)

to do a clean build of the documentation.
The output looks something like::

  Removing everything under '_build'...
  Running Sphinx v1.5.1
  making output directory...
  loading pickled environment... not yet created
  loading intersphinx inventory from https://docs.python.org/3/objects.inv...
  loading intersphinx inventory from http://salishsea-meopar-docs.readthedocs.org/en/latest/objects.inv...
  intersphinx inventory has moved: http://salishsea-meopar-docs.readthedocs.org/en/latest/objects.inv -> http://salishsea-meopar-docs.readthedocs.io/en/latest/objects.inv
  building [mo]: targets for 0 po files that are out of date
  building [html]: targets for 1 source files that are out of date
  updating environment: 1 added, 0 changed, 0 removed
  reading sources... [100%] index
  looking for now-outdated files... none found
  pickling environment... done
  checking consistency... done
  preparing documents... done
  writing output... [100%] index
  generating indices... genindex
  writing additional pages... search
  copying static files... done
  copying extra files... done
  dumping search index in English (code: en) ... done
  dumping object inventory... done
  build succeeded.

  Build finished. The HTML pages are in _build/html.

The HTML rendering of the docs ends up in :file:`docs/_build/html/`.
You can open the :file:`index.html` file in that directory tree in your browser to preview the results of the build before committing and pushing your changes to Bitbucket.

Whenever you push changes to :ref:`salishsea-site-repo` on Bitbucket the documentation is automatically re-built and rendered at https://salishsea-site.readthedocs.io/en/latest/.


.. _SalishSeaSiteRunningTheUnitTests:

Running the Unit Tests
----------------------

The test suite for the :kbd:`salishsea-site` package is in :file:`salishsea-site/tests/`.
The `pytest`_ tools is used for test fixtures and as the test runner for the suite.

With your :kbd:`salishsea-site` development environment activated,
use:

.. code-block:: bash

    (salishsea-site)$ cd salishsea-site/
    (salishsea-site)$ py.test

to run the test suite.
The output looks something like::

  =========================== test session starts ============================
  platform linux -- Python 3.6.0, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
  rootdir: /home/doug/Documents/MEOPAR/salishsea-site, inifile:
  collected 65 items

  tests/test_mako_filters.py .......
  tests/views/test_bloomcast.py ..
  tests/views/test_salishseacast.py ........................................................

  ======================== 65 passed in 0.87 seconds =========================

You can monitor what lines of code the test suite exercises using the `coverage.py`_ tool with the command:

.. _coverage.py: https://coverage.readthedocs.io/en/latest/

.. code-block:: bash

    (salishsea-site)$ cd salishsea-site/
    (salishsea-site)$ coverage run -m py.test

and generate a test coverage report with:

.. code-block:: bash

    (salishsea-site)$ coverage report

to produce a plain text report,
or

.. code-block:: bash

    (salishsea-site)$ coverage html

to produce an HTML report that you can view in your browser by opening :file:`salishsea-site/htmlcov/index.html`.


.. _SalishSeaSiteVersionControlRepository:

Version Control Repository
--------------------------

.. image:: https://img.shields.io/badge/version%20control-hg-blue.svg
    :target: https://bitbucket.org/salishsea/salishsea-site/
    :alt: Mercurial on Bitbucket

The :kbd:`salishsea-site` package code and documentation source files are available in the :ref:`salishsea-site-repo` `Mercurial`_ repository at https://bitbucket.org/salishsea/salishsea-site.

.. _Mercurial: https://www.mercurial-scm.org/


.. _SalishSeaSiteIssueTracker:

Issue Tracker
-------------

.. image:: https://img.shields.io/bitbucket/issues/salishsea/salishsea-site.svg
    :target: https://bitbucket.org/salishsea/salishsea-site/issues?status=new&status=open
    :alt: Issue Tracker

Development tasks,
bug reports,
and enhancement ideas are recorded and managed in the issue tracker at https://bitbucket.org/salishsea/salishsea-site/issues.


License
=======

.. image:: https://img.shields.io/badge/license-Apache%202-cb2533.svg
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: Licensed under the Apache License, Version 2.0

The salishsea.eos.ubc.ca site content, code, and documentation are
copyright 2014-2020 by the Mesoscale Ocean and Atmospheric Dynamics (MOAD) group
in the Department of Earth, Ocean, and Atmospheric Sciences
at The University of British Columbia.
Please see https://salishsea.eos.ubc.ca/contributors for details.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
