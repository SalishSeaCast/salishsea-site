.. salishsea.eos.ubc.ca/nemo section landing page

:license:
  Copyright 2014-2015 The Salish Sea MEOPAR Contributors
  and The University of British Columbia

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.


*********************
Salish Sea NEMO Model
*********************

About the Project
=================

The Salish Sea is home to a large population of Canadians living in coastal communities at risk to ocean related hazards.
There is an ongoing need to assess the impact of these hazards on human and marine environments through a multidisciplinary approach involving Canadian oceanographers,
biologists,
and social scientists.
The Marine Environmental Observation Prediction and Response network
(MEOPAR_)
provides a platform to accelerate this type of research.

.. _MEOPAR: http://meopar.ca/

The Salish Sea MEOPAR project team is developing a three-dimensional ocean model for the Strait of Georgia and Salish Sea.
Using the NEMO_ modelling architecture the Salish Sea model will be used to evaluate storm surge risk in coastal communities.
Long term goals include data assimilation from the VENUS network and a coupled biogeochemical modelling component.

Results
-------

The most recent Storm Surge Forecast is available at `forecast.html`_. More on our storm surge modelling is available at the bottom of the page, see StormSurge_.
Research results on current and previous nowcasts and forecasts are available `here`_.

.. _NEMO: http://www.nemo-ocean.eu/
.. _forecast.html: http://salishsea.eos.ubc.ca/storm-surge/forecast.html
.. _here: http://eoas.ubc.ca/~dlatorne/MEOPAR/nowcast/

.. image:: _static/nemo/SalishSeaImage.png
    :alt: Salish Sea NEMO Model Domain
    :align: center


Project Resources
=================

* The main project documentation site is at http://salishsea-meopar-docs.readthedocs.org/.
* The project team maintains a set of Mercurial_ version control repositories for code,
  documentation (including the source files for this site),
  and analyses of model results.
  The contents of those repositories and their development history is accessible at https://bitbucket.org/salishsea/.

.. _Mercurial: http://mercurial.selenic.com/


Project Team and Collaborators
==============================

The Salish Sea NEMO Model project is lead by `Susan Allen`_ in the Department of Earth, Ocean, and Atmospheric Sciences at the University of British Columbia.
Other team members:

* Nancy Soontiens
* Doug Latornell
* Ben Moore-Maley
* Idalia Machuca
* Jie Liu
* Kate Le Souëf (emeritus)

The team collaborates with other MEOPAR_ funded research teams at UBC:

* The observations team in EOAS lead by `Rich Pawlowicz`_:

  * Mark Halverson
  * Chuning Wang

* The impacts and indictors of marine hazards team in the UBC School of Community and Regional Planning lead by `Stephanie Chang`_:

  * Jackie Yip
  * Christopher Carter
  * Rebecca Chaster
  * Ashley Lowcock
  * Shona van Zijll de jong (emeritus)

.. _Susan Allen: http://eos.ubc.ca/~sallen/
.. _Rich Pawlowicz: http://www.eos.ubc.ca/~rich/research.html
.. _Stephanie Chang: https://sites.google.com/site/stephanieechang1/home

We also collaborate with MEOPAR_ researchers and NEMO_ users across Canada:

* Keith Thompson, Dalhousie University
* Vasily Korabel, Dalhousie University
* Youyu Lu, Fisheries and Oceans Canada
* J-P Paquin, Dalhousie University
* Fatemeh Chegini, Dalhousie University
* Luc Fillion, Environment Canada
* Kao-Shen Chung, Environment Canada
* Weiguang Chang, Environment Canada

and with many other researchers,
including:

* Diane Masson, Fisheries and Oceans Canada
* Mike Foreman, Fisheries and Oceans Canada
* Debby Ianson, Fisheries and Oceans Canada
* John Morrison, Fisheries and Oceans Canada
* Charles Hannah, Fisheries and Oceans Canada
* Pramod Thupaki, Fisheries and Oceans Canada

.. _StormSurge:

Storm Surge Modeling
====================

The Salish Sea models ability to calculate tides and sea surface height was evaluatee by hindcasting storm surge events that occurred between 2002 and 2011.  A manuscript (Soontiens et al) will be submitted soon.
Since Oct, 2014  the model is run daily to provide a nowcast and one or two forecasts, providing sea surface height forecasts that are published to the web.
The Salish Sea NEMO model `forecast results`_ are part of the `storm surge prediction and risk assessment resources`_.  

.. _storm surge prediction and risk assessment resources: storm-surge/index.html
.. _forecast results: http://salishsea.eos.ubc.ca/storm-surge/forecast.html


Reference
---------
Soontiens, N., Allen, S., Latornell, D., Le Souef, K., Machuca, I., Paquin, J.-P., Lu, Y., Thompson, K., Korabel, V. (2015). Storm surges in the Strait of Georgia simulated with a regional model. in prep.
