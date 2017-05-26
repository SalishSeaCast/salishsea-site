## Copyright 2013-2017 The Salish Sea MEOPAR Contributors
## and The University of British Columbia
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##    http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

<%inherit file="../site.mako"/>

<%block name="title">
  Strait of Georgia Bloomcast
</%block>

<div class="container">
  <div class="row">
    <div class="col-md-10 col-md-offset-1">
      <h1>Strait of Georgia Bloomcast</h1>

      <h2>About the Project</h2>
      <p class="text-justify">
        The timing of the spring phytoplankton bloom in the Strait of Georgia is highly variable,
        ranging from late February to mid-April.
        Changes in the timing have been related to the success of herring larval recruitment
        <a href="#footnote1" id="footnote1-back-link" title="Link to citation">[1]</a>
        and studies in a nearby fjord suggest it may affect the zooplankton species composition
        <a href="#footnote2" id="footnote2-back-link" title="Link to citation">[2]</a>.
        In this well stratified,
        mid-latitude system,
        the timing is controlled by the light availability to the phytoplankton which is in turn controlled by the incoming light
        (cloud fraction decreases this)
        and by the depth over which the phytoplankton are mixed
        (wind increases this).
        The role of freshwater is more nuanced;
        more river outflow both:
      </p>
      <ol class="lower-alpha">
        <li>
          stabilizes the water column which decreases the depth over which the phytoplankton are mixed,
          increasing their growth rate,
          and
        </li>
        <li>
          increases the advection loss of phytoplankton.
        </li>
      </ol>
      <p class="text-justify">
        The <a href="https://www.eoas.ubc.ca/~sallen/SOG-docs/">SOG biophysical model for deep estuaries</a>
        <a href="#footnote3" id="footnote3-back-link" title="Link to citation">[3]</a>
        is a vertical-mixing layer model forced by observed winds at Sand Heads,
        observed air temperature and humidity at Vancouver International Airport (YVR)
        <a href="#footnote4" id="footnote4-back-link" title="Link to citation">[4]</a>,
        Fraser River flow at Hope and Englishman River flow at Parksville
        <a href="#footnote5" id="footnote5-back-link" title="Link to citation">[5]</a>.
        The latter is multiplied by 55 to represent all river flows into the Strait other than the Fraser River.
        Cloud fraction is interpreted based on the weather description and the historical average cloud fraction to weather,
        done by month for the most common weather descriptions.
      </p>
      <p class="text-justify">
        The physical model is based on the Large et al. (1994) KPP-model with an estuarine circulation model added 
        <a href="#footnote6" id="footnote6-back-link" title="Link to citation">[6]</a>.
        To model a spring bloom,
        only a simple nitrate-diatom biological model is used.
        The diatom growth parameters are taken from the literature based on the first phytoplankton to bloom in the Strait 
        (<em>Thalassiosira</em> spp.).
        The model zooplankton concentration was taken from observations 
        <a href="#footnote7" id="footnote7-back-link" title="Link to citation">[7]</a>
        and the model was tuned by adjusting the phytoplankton growth rate 
        <a href="#footnote3" id="footnote3-back-link" title="Link to citation">[3]</a>
        within the range measured in the laboratory.
        The model was tuned,
        within 4 days,
        for the spring blooms of 2002-2005 for which detailed observations were made as part of the STRATOGEM project 
        <a href="#footnote3" id="footnote3-back-link" title="Link to citation">[3]</a>.
      </p>
      <p class="text-justify">
        A carbon module that models dissolved inorganic carbon and total alkalinity has been added to the model and allows estimation of aragonite saturation state 
        <a href="#footnote8" id="footnote8-back-link" title="Link to citation">[8]</a>.
      </p>

      <h3>Results</h3>
      <p class="text-justify">
        The most recent predictions for the first spring diatom bloom in the Strait of Georgia are available at 
        <a href="https://salishsea.eos.ubc.ca/bloomcast/spring_diatoms.html">https://salishsea.eos.ubc.ca/bloomcast/spring_diatoms.html</a>.
      </p>

      <h3>References</h3>
      <p class="text-justify">
        <a id="footnote1" href="#footnote1-back-link" title="Link to reference">[1]</a>
        Schweigert, J.F., M. Thompson, C. Fort, D.E. Hay, T.W. Therriault, and L.N. Brown. (2013).
        Factors linking Pacific herring (<em>Clupea pallasi</em>) productivity and the spring plankton bloom in the Strait of Georgia, British Columbia, Canada.
        Prog. Oceanogr., volume 115, pp 103-110.
        <a href="http://dx.doi.org/10.1016/j.pocean.2013.05.017" title="Link to paper via DOI">
          http://dx.doi.org/10.1016/j.pocean.2013.05.017
        </a>
      </p>
      <p class="text-justify">
        <a id="footnote2" href="#footnote2-back-link" title="Link to reference">[2]</a>
        Tommasi, D., B.P.V. Hunt, E.A. Pakhomov, and D.L. Mackas. (2013).
        Mesozooplankton community seasonal succession and its drivers: Insights from a British Columbia, Canada, fjord.
        J. Mar. Systems, volume 115, pp. 10-32.
        <a href="http://dx.doi.org/10.1016/j.jmarsys.2013.01.005" title="Link to paper via DOI">
          http://dx.doi.org/10.1016/j.jmarsys.2013.01.005
        </a>
      </p>
      <p class="text-justify">
        <a id="footnote3" href="#footnote3-back-link" title="Link to reference">[3]</a>
        Allen, S. E. and M. A. Wolfe. (2013).
        Hindcast of the Timing of the Spring Phytoplankton Bloom in the Strait of Georgia, 1968-2010.
        Progress in Oceanography, volume 115, pp 6-13.
        <a href="http://dx.doi.org/10.1016/j.pocean.2013.05.026" title="Link to paper via DOI">
          http://dx.doi.org/10.1016/j.pocean.2013.05.026
        </a>
      </p>
      <p class="text-justify">
        <a id="footnote4" href="#footnote4-back-link" title="Link to reference">[4]</a>
        Environment Canada, (${ec_database_year}). Climate database.
        <a href="http://climate.weather.gc.ca/index_e.html" title="Link to database description">
          http://climate.weather.gc.ca/index_e.html
        </a>
      </p>
      <p class="text-justify">
        <a id="footnote5" href="#footnote5-back-link" title="Link to reference">[5]</a>
        Environment Canada, (${ec_database_year}). Hydrometric data.
        <a href="http://www.ec.gc.ca/rhc-wsc/" title="Link to database description">
          http://www.ec.gc.ca/rhc-wsc/
        </a>
      </p>
      <p class="text-justify">
        <a id="footnote6" href="#footnote6-back-link" title="Link to reference">[6]</a>
        Collins, A. K., S. E. Allen, and R. Pawlowicz. (2009).
        The role of wind in determining the timing of the spring bloom in the Strait of Georgia.
        Can. J. Fish. Aquat. Sci, volume 66, pp. 1597-1616.
        <a href="http://dx.doi.org/10.1139/F09-071 " title="Link to paper via DOI">
          http://dx.doi.org/10.1139/F09-071
        </a>
      </p>
      <p class="text-justify">
        <a id="footnote7" href="#footnote7-back-link" title="Link to reference">[7]</a>
        Sastri, A. R., and J. F. Dower. (2009).
        Interannual variability in chitobiase-based production rates of the crustacean zooplankton community in the Strait of Georgia, British Columbia, Canada.
        Mar. Ecol. Prog. Ser. volume 388, pp. 147–157.
        <a href="https://doi.org/10.3354/meps08111" title="Link to paper via DOI">
          https://doi.org/10.3354/meps08111
        </a>
      </p>
      <p class="text-justify">
        <a id="footnote8" href="#footnote8-back-link" title="Link to reference">[8]</a>
        Moore-Maley, Benjamin. (2014).
        The inorganic carbonate chemistry of the southern Strait of Georgia,
        Masters Thesis, University of British Columbia.
        <a href="https://circle.ubc.ca/handle/2429/51770" title="Link to thesis">
          https://circle.ubc.ca/handle/2429/51770
        </a>
      </p>
    </div>
  </div>
</div>
