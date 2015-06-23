.. salishsea.eos.ubc.ca/bloomcast section landing page

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


***************************
Strait of Georgia Bloomcast
***************************

About the Project
=================

The timing of the spring phytoplankton bloom in the Strait of Georgia is highly variable,
ranging from late February to mid-April.
Changes in the timing have been related to the success of herring larval recruitment [#f1]_ and studies in a nearby fjord suggest it may affect the zooplankton species composition [#f2]_.
In this well stratified,
mid-latitude system,
the timing is controlled by the light availability to the phytoplankton which is in turn controlled by the incoming light
(cloud fraction decreases this)
and by the depth over which the phytoplankton are mixed
(wind increases this).
The role of freshwater is more nuanced;
more river outflow both

a) stabilizes the water column which decreases the depth over which the phytoplankton are mixed,
   increasing their growth rate,
   and
b) increases the advection loss of phytoplankton.

The `SOG biophysical model for deep estuaries`_ [#f3]_ is a vertical-mixing layer model forced by observed winds at Sand Heads,
observed air temperature and humidity at Vancouver International Airport (YVR) [#f4]_,
Fraser River flow at Hope and Englishman River flow at Parksville [#f5]_.
The latter is multiplied by 55 to represent all river flows into the Strait other than the Fraser River.
Cloud fraction is interpreted based on the weather description and the historical average cloud fraction to weather,
done by month for the most common weather descriptions.

.. _SOG biophysical model for deep estuaries: http://www.eos.ubc.ca/~sallen/SOG-docs/

The physical model is based on the Large et al. (1994) KPP-model with an estuarine circulation model added [#f6]_.
To model a spring bloom,
only a simple nitrate-diatom biological model is used.
The diatom growth parameters are taken from the literature based on the first phytoplankton to bloom in the Strait (Thalassiosira spp.).
The model zooplankton concentration was taken from observations [#f7]_ and the model was tuned by adjusting the phytoplankton growth rate [#f3]_ within the range measured in the laboratory.
The model was tuned,
within 4 days,
for the spring blooms of 2002-2005 for which detailed observations were made as part of the STRATOGEM project [#f3]_.

A carbon module that models dissolved inorganic carbon and total alkalinity has been added to the model and allows estimation of aragonite saturation state [#f8]_.

Results
-------

The most recent predictions for the first spring diatom bloom in the Strait fo Georgia are available at http://salishsea.eos.ubc.ca/bloomcast/spring_diatoms.html.


References
----------

.. [#f1] Schweigert, J.F., M. Thompson, C. Fort, D.E. Hay, T.W. Therriault, and L.N. Brown. 2013. Factors linking Pacific herring (Clupea pallasi) productivity and the spring plankton bloom in the Strait of Georgia, British Columbia, Canada. Prog. Oceanogr., 115: 103-110

.. [#f2] Tommasi, D., B.P.V. Hunt, E.A. Pakhomov, and D.L. Mackas. 2013. Mesozooplankton community seasonal succession and its drivers: Insights from a British Columbia, Canada, fjord. J. Mar. Systems, 115: 10-32

.. [#f3] Allen, S. E. and M. A. Wolfe. 2013. Hindcast of the Timing of the Spring Phytoplankton Bloom in the Strait of Georgia, 1968-2010. Progress in Oceanography, vol 115, pp 6-13. http://dx.doi.org/10.1016/j.pocean.2013.05.026

.. [#f4] Environment Canada, 2015. Climate database. http://climate.weather.gc.ca/index_e.html

.. [#f5] Environment Canada, 2015. Hydrometric data. http://www.ec.gc.ca/rhc-wsc/

.. [#f6] Collins, A. K., S. E. Allen, and R. Pawlowicz. 2009. The role of wind in determining the timing of the spring bloom in the Strait of Georgia. Can. J. Fish. Aquat. Sci, 66:, 1597-1616.

.. [#f7] Sastri, A. R., and J. F. Dower. 2009. Interannual variability in chitobiase-based production rates of the crustacean zooplankton community in the Strait of Georgia, British Columbia, Canada. Mar. Ecol. Prog. Ser. 388,: 147–157.

.. [#f8] Moore-Maley, Benjamin. 2014. The inorganic carbonate chemistry of the southern Strait of Georgia, Masters Thesis, University of British Columbia. https://circle.ubc.ca/handle/2429/51770
