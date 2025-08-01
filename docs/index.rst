.. Copyright 2014 – present by the Mesoscale Ocean and Atmospheric Dynamics (MOAD) group
.. in the Department of Earth, Ocean, and Atmospheric Sciences
.. at The University of British Columbia
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

.. SPDX-License-Identifier: Apache-2.0


.. _SalishSeaSiteWebApp:

*********************************
salishsea.eos.ubc.ca Site Web App
*********************************

+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Continuous Integration** | .. image:: https://github.com/SalishSeaCast/salishsea-site/actions/workflows/pytest-with-coverage.yaml/badge.svg                                                                                         |
|                            |      :target: https://github.com/SalishSeaCast/salishsea-site/actions?query=workflow:pytest-with-coverage                                                                                                |
|                            |      :alt: Pytest with Coverage Status                                                                                                                                                                   |
|                            | .. image:: https://codecov.io/gh/SalishSeaCast/salishsea-site/branch/main/graph/badge.svg                                                                                                                |
|                            |      :target: https://app.codecov.io/gh/SalishSeaCast/salishsea-site                                                                                                                                     |
|                            |      :alt: Codecov Testing Coverage Report                                                                                                                                                               |
|                            | .. image:: https://github.com/SalishSeaCast/salishsea-site/actions/workflows/codeql-analysis.yaml/badge.svg                                                                                              |
|                            |      :target: https://github.com/SalishSeaCast/salishsea-site/actions?query=workflow:CodeQL                                                                                                              |
|                            |      :alt: CodeQL analysis                                                                                                                                                                               |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Documentation**          | .. image:: https://app.readthedocs.org/projects/salishsea-site/badge/?version=latest                                                                                                                     |
|                            |      :target: https://salishsea-site.readthedocs.io                                                                                                                                                      |
|                            |      :alt: Documentation Status                                                                                                                                                                          |
|                            | .. image:: https://github.com/SalishSeaCast/salishsea-site/actions/workflows/sphinx-linkcheck.yaml/badge.svg                                                                                             |
|                            |      :target: https://github.com/SalishSeaCast/salishsea-site/actions?query=workflow:sphinx-linkcheck                                                                                                    |
|                            |      :alt: Sphinx linkcheck                                                                                                                                                                              |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Package**                | .. image:: https://img.shields.io/github/v/release/SalishSeaCast/salishsea-site?logo=github                                                                                                              |
|                            |      :target: https://github.com/SalishSeaCast/salishsea-site/releases                                                                                                                                   |
|                            |      :alt: Releases                                                                                                                                                                                      |
|                            | .. image:: https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/SalishSeaCast/salishsea-site/main/pyproject.toml&logo=Python&logoColor=gold&label=Python   |
|                            |      :target: https://docs.python.org/3.13/                                                                                                                                                              |
|                            |      :alt: Python Version from PEP 621 TOML                                                                                                                                                              |
|                            | .. image:: https://img.shields.io/github/issues/SalishSeaCast/salishsea-site?logo=github                                                                                                                 |
|                            |      :target: https://github.com/SalishSeaCast/salishsea-site/issues                                                                                                                                     |
|                            |      :alt: Issue Tracker                                                                                                                                                                                 |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Meta**                   | .. image:: https://img.shields.io/badge/license-Apache%202-cb2533.svg                                                                                                                                    |
|                            |      :target: https://www.apache.org/licenses/LICENSE-2.0                                                                                                                                                |
|                            |      :alt: Licensed under the Apache License, Version 2.0                                                                                                                                                |
|                            | .. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github                                                                                                                       |
|                            |      :target: https://github.com/SalishSeaCast/salishsea-site                                                                                                                                            |
|                            |      :alt: Git on GitHub                                                                                                                                                                                 |
|                            | .. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white                                                                                                  |
|                            |      :target: https://pre-commit.com                                                                                                                                                                     |
|                            |      :alt: pre-commit                                                                                                                                                                                    |
|                            | .. image:: https://img.shields.io/badge/code%20style-black-000000.svg                                                                                                                                    |
|                            |      :target: https://black.readthedocs.io/en/stable/                                                                                                                                                    |
|                            |      :alt: The uncompromising Python code formatter                                                                                                                                                      |
|                            | .. image:: https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg                                                                                                                                    |
|                            |      :target: https://github.com/pypa/hatch                                                                                                                                                              |
|                            |      :alt: Hatch project                                                                                                                                                                                 |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
  .. _HTML5: https://developer.mozilla.org/en-US/docs/Glossary/HTML5
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

.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Sphinx: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html


.. _SalishSeaSiteDevelopment:

Web App Package Development
===========================

.. _SalishSeaSitePythonVersions:

Python Versions
---------------

.. image:: https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/SalishSeaCast/salishsea-site/main/pyproject.toml&logo=Python&logoColor=gold&label=Python
    :target: https://docs.python.org/3.13/
    :alt: Python Version

The :kbd:`salishsea-site` package is developed,
tested,
and deployed using `Python`_ 3.13.


.. _SalishSeaSiteGettingTheCode:

Getting the Code
----------------

.. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    :target: https://github.com/SalishSeaCast/salishsea-site
    :alt: Git on GitHub

Clone the :ref:`salishsea-site-repo` code and documentation `repository`_ from GitHub with:

.. _repository: https://github.com/SalishSeaCast/salishsea-site

.. code-block:: bash

    $ git clone git@github.com:SalishSeaCast/salishsea-site.git

or

.. code-block:: bash

    $ git clone https://github.com/SalishSeaCast/salishsea-site.git

if you don't have `ssh key authentication`_ set up on GitHub
(or copy the link from the :guilabel:`Clone or download` button on the `repository`_ page).

.. _ssh key authentication: https://docs.github.com/en/authentication/connecting-to-github-with-ssh


.. _SalishSeaSiteDevelopmentEnvironment:

Development Environment
=======================

Setting up an isolated development environment using `Conda`_ is strongly recommended.
Assuming that you have :ref:`AnacondaPythonDistro` or `Miniconda3`_ installed,
you can create and activate an environment called :kbd:`salishsea-site` that will have all of the Python packages necessary for development,
testing,
and building the documentation with the commands:

.. _Conda: https://docs.conda.io/en/latest/
.. _Miniconda3: https://docs.conda.io/en/latest/miniconda.html

.. code-block:: bash

    $ cd salishsea-site
    $ conda env create -f env/environment-dev.yaml

The :kbd:`salishsea-site` package is installed in `editable install mode`_
as part of the conda environment creation process.
That means that the package is installed from the cloned repo via symlinks so that
it will be automatically updated as the repo evolves.

.. _editable install mode: https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs

To deactivate the environment use:

.. code-block:: bash

    (salishsea-site)$ conda deactivate


.. _SalishSeaSiteCodingStyle:

Coding Style
------------

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://pre-commit.com
   :alt: pre-commit
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://black.readthedocs.io/en/stable/
    :alt: The uncompromising Python code formatter

The :kbd:`salishsea-site` package uses Git pre-commit hooks managed by `pre-commit`_
to maintain consistent code style and and other aspects of code,
docs,
and repo QA.

.. _pre-commit: https://pre-commit.com/

To install the `pre-commit` hooks in a newly cloned repo,
activate the conda development environment,
and run :command:`pre-commit install`:

.. code-block:: bash

    $ cd salishsea-site
    $ conda activate salishsea-site
    (salishsea-site)$ pre-commit install


.. note::
    You only need to install the hooks once immediately after you make a new clone of the
    `salishsea-site repository`_ and build your :ref:`SalishSeaSiteDevelopmentEnvironment`.

.. _salishsea-site repository: https://github.com/SalishSeaCast/salishsea-site


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

.. image:: https://app.readthedocs.org/projects/salishsea-site/badge/?version=latest
    :target: https://salishsea-site.readthedocs.io
    :alt: Documentation Status

The documentation for the :kbd:`salishsea-site` package is written in `reStructuredText`_ and converted to HTML using `Sphinx`_.

If you have write access to the `repository`_ on GitHub,
whenever you push changes to GitHub the documentation is automatically re-built and rendered at https://salishsea-site.readthedocs.io.

Additions,
improvements,
and corrections to these docs are *always* welcome.

The quickest way to fix typos, etc. on existing pages is to use the :guilabel:`Edit on GitHub` link in the upper right corner of the page to get to the online editor for the page on `GitHub`_.

.. _GitHub: https://github.com/SalishSeaCast/salishsea-site

For more substantial work,
and to add new pages,
follow the instructions in the :ref:`SalishSeaSiteDevelopmentEnvironment` section above.
In the development environment you can build the docs locally instead of having to push commits to GitHub to trigger a `build on readthedocs.org`_ and wait for it to complete.
Below are instructions that explain how to:

.. _build on readthedocs.org: https://app.readthedocs.org/projects/salishsea-site/builds/

* build the docs with your changes,
  and preview them in Firefox

* check the docs for broken links


.. _SalishSeaSiteBuildingAndPreviewingTheDocumentation:

Building and Previewing the Documentation
-----------------------------------------

Building the documentation is driven by the :file:`docs/Makefile`.
With your :kbd:`salishsea-site` development environment activated,
use:

.. code-block:: bash

    (salishsea-site)$ (cd docs && make clean html)

to do a clean build of the documentation.
The output looks something like:

.. code-block:: text

    Removing everything under '_build'...
    Running Sphinx v8.1.3
    loading translations [en]... done
    making output directory... done
    loading intersphinx inventory 'python' from https://docs.python.org/3/objects.inv ...
    loading intersphinx inventory 'salishseadocs' from https://salishsea-meopar-docs.readthedocs.io/en/latest/objects.inv ...
    building [mo]: targets for 0 po files that are out of date
    writing output...
    building [html]: targets for 1 source files that are out of date
    updating environment: [new config] 1 added, 0 changed, 0 removed
    reading sources... [100%] index
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    copying assets...
    copying static files...
    Writing evaluated template result to /media/doug/warehouse/MEOPAR/salishsea-site/docs/_build/html/_static/language_data.js
    Writing evaluated template result to /media/doug/warehouse/MEOPAR/salishsea-site/docs/_build/html/_static/basic.css
    Writing evaluated template result to /media/doug/warehouse/MEOPAR/salishsea-site/docs/_build/html/_static/documentation_options.js
    Writing evaluated template result to /media/doug/warehouse/MEOPAR/salishsea-site/docs/_build/html/_static/js/versions.js
    copying static files: done
    copying extra files...
    copying extra files: done
    copying assets: done
    writing output... [100%] index
    generating indices... genindex done
    writing additional pages... search done
    dumping search index in English (code: en)... done
    dumping object inventory... done
    build succeeded.

    The HTML pages are in _build/html.

The HTML rendering of the docs ends up in :file:`docs/_build/html/`.
You can open the :file:`index.html` file in that directory tree in your browser to preview the results of the build before committing and pushing your changes to Bitbucket.

If you have write access to the `repository`_ on GitHub,
whenever you push changes to GitHub the documentation is automatically re-built and rendered at https://salishsea-site.readthedocs.io.


.. _SalishSeaSiteLinkCheckingTheDocumentation:

Link Checking the Documentation
-------------------------------

.. image:: https://github.com/SalishSeaCast/salishsea-site/workflows/sphinx-linkcheck/badge.svg
    :target: https://github.com/SalishSeaCast/salishsea-site/actions?query=workflow%3Asphinx-linkcheck
    :alt: Sphinx linkcheck Status

Sphinx also provides a link checker utility which can be run to find broken or redirected links in the docs.
With your :kbd:`salishsea-site` environment activated,
use:

.. code-block:: bash

    (salishsea-site)$ cd salishsea-site/docs/
    (salishsea-site) docs$ make clean linkcheck

The output looks something like:

.. code-block:: text

    Removing everything under '_build'...
    Running Sphinx v8.1.3
    loading translations [en]... done
    making output directory... done
    loading intersphinx inventory 'python' from https://docs.python.org/3/objects.inv ...
    loading intersphinx inventory 'salishseadocs' from https://salishsea-meopar-docs.readthedocs.io/en/latest/objects.inv ...
    building [mo]: targets for 0 po files that are out of date
    writing output...
    building [linkcheck]: targets for 1 source files that are out of date
    updating environment: [new config] 1 added, 0 changed, 0 removed
    reading sources... [100%] index
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    copying assets...
    copying assets: done
    writing output... [100%] index

    (           index: line   24) ok        https://black.readthedocs.io/en/stable/
    (           index: line  545) ok        https://coverage.readthedocs.io/en/latest/
    (           index: line   30) ok        https://codecov.io/gh/SalishSeaCast/salishsea-site/branch/main/graph/badge.svg
    (           index: line   37) ok        https://app.readthedocs.org/projects/salishsea-site/badge/?version=latest
    (           index: line  115) ok        https://developer.mozilla.org/en-US/docs/Glossary/HTML5
    (           index: line  208) ok        https://docs.conda.io/en/latest/miniconda.html
    (           index: line  591) ok        https://docs.github.com/en/actions
    (           index: line  197) ok        https://docs.github.com/en/authentication/connecting-to-github-with-ssh
    (           index: line   24) ok        https://app.codecov.io/gh/SalishSeaCast/salishsea-site
    (           index: line   71) ok        https://docs.pylonsproject.org/projects/pyramid/en/latest/index.html
    (           index: line  208) ok        https://docs.conda.io/en/latest/
    (           index: line   82) ok        https://docs.pylonsproject.org/projects/pyramid/en/latest/index.html#narrative-documentation
    (           index: line   79) ok        https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/firstapp.html#firstapp-chapter
    (           index: line  115) ok        https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/templates.html
    (           index: line  325) ok        https://app.readthedocs.org/projects/salishsea-site/builds/
    (           index: line   79) ok        https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html
    (           index: line  141) ok        https://docs.pytest.org/en/latest/
    (           index: line   24) ok        https://docs.python.org/3.13/
    (           index: line  108) ok        https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/views.html
    (           index: line  100) ok        https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/urldispatch.html
    (           index: line  605) ok        https://git-scm.com/
    (           index: line  108) ok        https://docs.python.org/3/library/stdtypes.html#dict
    (           index: line  115) ok        https://getbootstrap.com/
    (           index: line   33) ok        https://github.com/SalishSeaCast/salishsea-site/actions/workflows/codeql-analysis.yaml/badge.svg
    (           index: line   27) ok        https://github.com/SalishSeaCast/salishsea-site/actions/workflows/pytest-with-coverage.yaml/badge.svg
    (           index: line   40) ok        https://github.com/SalishSeaCast/salishsea-site/actions/workflows/sphinx-linkcheck.yaml/badge.svg
    (           index: line   24) ok        https://github.com/SalishSeaCast/salishsea-site
    (           index: line  580) ok        https://github.com/SalishSeaCast/salishsea-site/actions
    (           index: line  401) ok        https://github.com/SalishSeaCast/salishsea-site/actions?query=workflow%3Asphinx-linkcheck
    (           index: line  571) ok        https://github.com/SalishSeaCast/salishsea-site/actions?query=workflow%3Apytest-with-coverage
    (           index: line   24) ok        https://github.com/SalishSeaCast/salishsea-site/actions?query=workflow:pytest-with-coverage
    (           index: line   24) ok        https://github.com/SalishSeaCast/salishsea-site/actions?query=workflow:CodeQL
    (           index: line  573) ok        https://github.com/SalishSeaCast/salishsea-site/workflows/pytest-with-coverage/badge.svg
    (           index: line  403) ok        https://github.com/SalishSeaCast/salishsea-site/workflows/sphinx-linkcheck/badge.svg
    (           index: line   24) ok        https://github.com/SalishSeaCast/salishsea-site/actions?query=workflow:sphinx-linkcheck
    (           index: line   66) ok        https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg
    (           index: line   63) ok        https://img.shields.io/badge/code%20style-black-000000.svg
    (           index: line   54) ok        https://img.shields.io/badge/license-Apache%202-cb2533.svg
    (           index: line   60) ok        https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    (           index: line   57) ok        https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    (           index: line   50) ok        https://img.shields.io/github/issues/SalishSeaCast/salishsea-site?logo=github
    (           index: line   24) ok        https://github.com/SalishSeaCast/salishsea-site/issues
    (           index: line   44) ok        https://img.shields.io/github/v/release/SalishSeaCast/salishsea-site?logo=github
    (           index: line   47) ok        https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/SalishSeaCast/salishsea-site/main/pyproject.toml&logo=Python&logoColor=gold&label=Python
    (           index: line  222) ok        https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs
    (           index: line   24) ok        https://github.com/pypa/hatch
    (           index: line  545) ok        https://pytest-cov.readthedocs.io/en/latest/
    (           index: line  183) ok        https://salishsea-meopar-docs.readthedocs.io/en/latest/repos_organization.html#salishsea-site-repo
    (           index: line   24) ok        https://pre-commit.com
    (           index: line  580) ok        https://github.com/SalishSeaCast/salishsea-site/commits/main
    (           index: line  248) ok        https://pre-commit.com/
    (           index: line   71) ok        https://salishsea.eos.ubc.ca/
    (           index: line   24) ok        https://www.apache.org/licenses/LICENSE-2.0
    (           index: line  631) ok        https://salishsea.eos.ubc.ca/contributors
    (           index: line   71) ok        https://www.python.org/
    (           index: line  147) ok        https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
    (           index: line  208) ok        https://salishsea-meopar-docs.readthedocs.io/en/latest/work_env/anaconda_python.html#anacondapythondistro
    (           index: line   24) ok        https://github.com/SalishSeaCast/salishsea-site/releases
    (           index: line   24) ok        https://salishsea-site.readthedocs.io
    (           index: line  115) ok        https://www.makotemplates.org/
    build succeeded.

    Look for any errors in the above output or in _build/linkcheck/output.txt

:command:`make linkcheck` is run monthly via a `scheduled GitHub Actions workflow`_

.. _scheduled GitHub Actions workflow: https://github.com/SalishSeaCast/salishsea-site/actions?query=workflow%3Asphinx-linkcheck


.. _SalishSeaSiteRunningTheUnitTests:

Running the Unit Tests
----------------------

The test suite for the :kbd:`salishsea-site` package is in :file:`salishsea-site/tests/`.
The `pytest`_ tools is used for test fixtures and as the test runner for the suite.

With your :kbd:`salishsea-site` development environment activated,
use:

.. code-block:: bash

    (salishsea-site)$ cd salishsea-site/
    (salishsea-site)$ pytest

to run the test suite.
The output looks something like:

.. code-block:: text

    ============================== test session starts     ===============================
    platform linux -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
    rootdir: /media/doug/warehouse/MEOPAR/salishsea-site
    configfile: pyproject.toml
    plugins: anyio-4.9.0, cov-6.2.1
    collected 76 items

    tests/test_mako_filters.py .......                                              [  9%]
    tests/views/test_bloomcast.py ..                                                [ 11%]
    tests/views/test_figures.py ...                                                 [ 15%]
    tests/views/test_salishseacast.py ....................................................
    ............                                                                    [100%]
    ================================ 76 passed in 2.6s ===================================

You can monitor what lines of code the test suite exercises using the `coverage.py`_ and `pytest-cov`_ tools with the command:

.. _coverage.py: https://coverage.readthedocs.io/en/latest/
.. _pytest-cov: https://pytest-cov.readthedocs.io/en/latest/


.. code-block:: bash

    (salishsea-site)$ cd salishsea-site/
    (salishsea-site)$ pytest --cov=./

The test coverage report will be displayed below the test suite run output.

Alternatively,
you can use

.. code-block:: bash

    (salishsea-site)$ pytest --cov=./ --cov-report html

to produce an HTML report that you can view in your browser by opening :file:`salishsea-site/htmlcov/index.html`.


.. _SalishSeaSiteContinuousIntegration:

Continuous Integration
----------------------

.. image:: https://github.com/SalishSeaCast/salishsea-site/workflows/pytest-with-coverage/badge.svg
    :target: https://github.com/SalishSeaCast/salishsea-site/actions?query=workflow%3Apytest-with-coverage
    :alt: Pytest with Coverage Status
.. image:: https://codecov.io/gh/SalishSeaCast/salishsea-site/branch/main/graph/badge.svg
    :target: https://app.codecov.io/gh/SalishSeaCast/salishsea-site
    :alt: Codecov Testing Coverage Report

The :kbd:`salishsea-site` package unit test suite is run and a coverage report is generated whenever changes are pushed to GitHub.
The results are visible on the `repo actions page`_,
from the green checkmarks beside commits on the `repo commits page`_,
or from the green checkmark to the left of the "Latest commit" message on the `repo code overview page`_ .
The testing coverage report is uploaded to `codecov.io`_

.. _repo actions page: https://github.com/SalishSeaCast/salishsea-site/actions
.. _repo commits page: https://github.com/SalishSeaCast/salishsea-site/commits/main
.. _repo code overview page: https://github.com/SalishSeaCast/salishsea-site
.. _codecov.io: https://app.codecov.io/gh/SalishSeaCast/salishsea-site

The `GitHub Actions`_ workflow configuration that defines the continuous integration tasks is in the :file:`.github/workflows/pytest-coverage.yaml` file.

.. _GitHub Actions: https://docs.github.com/en/actions


.. _SalishSeaSiteVersionControlRepository:

Version Control Repository
--------------------------

.. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    :target: https://github.com/SalishSeaCast/salishsea-site
    :alt: Git on GitHub

The :kbd:`salishsea-site` package code and documentation source files are available in the :ref:`salishsea-site-repo` `Git`_ repository at https://github.com/SalishSeaCast/salishsea-site.

.. _Git: https://git-scm.com/


.. _SalishSeaSiteIssueTracker:

Issue Tracker
-------------

.. image:: https://img.shields.io/github/issues/SalishSeaCast/salishsea-site?logo=github
    :target: https://github.com/SalishSeaCast/salishsea-site/issues
    :alt: Issue Tracker

Development tasks,
bug reports,
and enhancement ideas are recorded and managed in the issue tracker at https://github.com/SalishSeaCast/salishsea-site/issues.


License
=======

.. image:: https://img.shields.io/badge/license-Apache%202-cb2533.svg
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: Licensed under the Apache License, Version 2.0

The salishsea.eos.ubc.ca site content, code, and documentation are
Copyright 2014 – present by the Mesoscale Ocean and Atmospheric Dynamics (MOAD) group
in the Department of Earth, Ocean, and Atmospheric Sciences
at The University of British Columbia.
Please see https://salishsea.eos.ubc.ca/contributors for details.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.


Release Process
===============

.. image:: https://img.shields.io/github/v/release/SalishSeaCast/salishsea-site?logo=github
    :target: https://github.com/SalishSeaCast/salishsea-site/releases
    :alt: Releases
.. image:: https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg
    :target: https://github.com/pypa/hatch
    :alt: Hatch project


Releases are done at Doug's discretion when significant pieces of development work have been
completed.

The release process steps are:

#. Use :command:`hatch version release` to bump the version from ``.devn`` to the next release
   version identifier;
   e.g. ``24.1.dev0`` to ``24.1``

#. Commit the version bump

#. Create an annotated tag for the release with :guilabel:`Git -> New Tag...` in PyCharm
   or :command:`git tag -e -a vyy.n`;
   :command:`git tag -e -a v24.1`

#. Push the version bump commit and tag to GitHub

#. Use the GitHub web interface to create a release,
   editing the auto-generated release notes into sections:

   * Features
   * Bug Fixes
   * Documentation
   * Maintenance
   * Dependency Updates

#. Use the GitHub :guilabel:`Issues -> Milestones` web interface to edit the release
   milestone:

   * Change the :guilabel:`Due date` to the release date
   * Delete the "when it's ready" comment in the :guilabel:`Description`

#. Use the GitHub :guilabel:`Issues -> Milestones` web interface to create a milestone for
   the next release:

   * Set the :guilabel:`Title` to the next release version,
     prepended with a ``v``;
     e.g. ``v24.2``
   * Set the :guilabel:`Due date` to the end of the year of the next release
   * Set the :guilabel:`Description` to something like
     ``v24.2 release - when it's ready :-)``
   * Create the next release milestone

#. Review the open issues,
   especially any that are associated with the milestone for the just released version,
   and update their milestone.

#. Close the milestone for the just released version.

#. Use :command:`hatch version minor,dev` to bump the version for the next development cycle,
   or use :command:`hatch version major,minor,dev` for a year rollover version bump

#. Commit the version bump

#. Push the version bump commit to GitHub
