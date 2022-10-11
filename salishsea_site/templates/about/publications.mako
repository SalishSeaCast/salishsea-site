## Copyright 2014 – present by the Mesoscale Ocean and Atmospheric Dynamics (MOAD) group
## in the Department of Earth, Ocean, and Atmospheric Sciences
## at The University of British Columbia
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##    https://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

## SPDX-License-Identifier: Apache-2.0


<%inherit file="../site.mako"/>

<%block name="title">Salish Sea – Publications</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
      <h1>Publications</h1>
        <p>
          The SalishSeaCast Project team have produced a number of refereed
          academic journal publications.
          If you use our model results,
          code,
          documentation,
          etc.,
          please cite one or more of our publications as appropriate.
        </p>
        <p>
          If our work is helpful or informative to you in a context where academic
          citation isn't possible we would appreciate you telling us with a quick
          email to Susan Allen
          &lt;<a href="mailto:sallen@eos.ubc.ca">sallen@eos.ubc.ca</a>&gt;.
        </p>

      <h2>Model Configuration, Evaluation, and Storm Surge Hindcasting</h2>
        <p>
          The Salish Sea NEMO model configuration and its ability to calculate
          tides and sea surface height was evaluated by hindcasting storm surge events
          that occurred between 2002 and 2011 in:
        </p>
        <p>
          Soontiens, N., Allen, S., Latornell, D., Le Souef, K., Machuca, I., Paquin, J.-P.,
          Lu, Y., Thompson, K., Korabel, V., 2016.
          Storm surges in the Strait of Georgia simulated with a regional model.
          <em>Atmosphere-Ocean</em> <strong>54</strong> 1-21.
        </p>
        <p>
          <a href="https://dx.doi.org/10.1080/07055900.2015.1108899">
            https://dx.doi.org/10.1080/07055900.2015.1108899
          </a>
        </p>

      <h2>Carbon Chemistry and Aragonite Saturation State</h2>
        <p>
          The seasonal variability of aragonite saturation and pH in the surface
          Strait of Georgia and their drivers were determined using a 1-D coupled
          biochemical-physical model in:
        </p>
        <p>
          Moore-Maley, B. L., S. E. Allen, and D. Ianson, 2016.
          Locally-driven interannual variability of near-surface pH and ΩA in the Strait of Georgia.
          <em>J. Geophys. Res. Oceans</em>, <strong>121(3)</strong>, 1600–1625.
        </p>
        <p>
          <a href="https://dx.doi.org/10.1002/2015JC011118">
            https://dx.doi.org/10.1002/2015JC011118
          </a>
        </p>

      <h2>Turbulence and Advective Mixing</h2>
        <p>
          The sensitivity of the deep water renewal into the Strait of Georgia
          and of fresh water pulses into Juan de Fuca Strait to modelling choices
          affecting both turbulence and advection has been determined in:
        </p>
        <p>
          Soontiens, N. and Allen, S.
          Modelling sensitivities to mixing and advection in a sill-basin estuarine system.
          <em>Ocean Modelling</em>, <strong>112</strong>, 17-32.
        </p>
        <p>
          <a href="https://dx.doi.org/10.1016/j.ocemod.2017.02.008">
            https://dx.doi.org/10.1016/j.ocemod.2017.02.008
          </a>
        </p>

      <h2>Salish Model Ecosystem-Lower Trophic (SMELT), the biological component of SalishSeaCast</h2>
        <p>
          The 3 nutrient- 3 phytoplankton- 1.5 zooplankton compartment model described in
          Moore-Maley et al . (2016) was adapted to three dimensions and coupled to the Salish
          Sea NEMO model described by Soontiens et al. (2016). Description and evaluation of the
          model can be found in:
        </p>
        <p>
          Olson, E. M., S. E. Allen, V. Do, M. Dunphy, and D. Ianson, 2020.
          Assessment of Nutrient Supply by a Tidal Jet in the Northern Strait of Georgia Based on a Biogeochemical Model.
          J. Geophys. Res. Oceans.
        </p>
        <p>
          <a href="https://dx.doi.org/10.1029/2019JC015766">
            https://dx.doi.org/10.1029/2019JC015766
          </a>
        </p>

      <h2>Cluster Analysis of Biophysical Dynamics</h2>
        <p>
          A cluster-based tool for model analysis and evaluation was developed and used to 
          determine biophysical dynamics of the system in:
        </p>
        <p>
          Jarníková, T., Olson, E. M., Allen, S. E., Ianson, D., and Suchy, K. D., 2021. 
          A clustering approach to determine biophysical provinces and physical drivers of 
          productivity dynamics in a complex coastal sea. 
          <em>Ocean Sci. Discuss.</em>, 1-36.
        </p>
        <p>
          <a href="https://doi.org/10.5194/os-2021-66">
            https://doi.org/10.5194/os-2021-66
          </a>
        </p>
    </div>
  </div>


  <div class="row">
    <div class="col-md-12">
      <h2>BibTeX Citations</h2>
    </div>
  </div>

  <div class="row">
    <div class="col-md-12">
      <h3>
        Soontiens, <em>et al</em>, 2016,
        Storm surges in the Strait of Georgia simulated with a regional model
      </h3>
    </div>
  </div>
  <div class="row">
    <div class="col-md-8 col-md-offset-1">
      <pre>
@article{"Soontiens-etal-2016,
    author = "Soontiens, N. and Allen, S. and Latornell, D. and
Le Souef, K. and Machuca, I. and Paquin, J.-P. and Lu, Y. and
Thompson, K. and Korabel, V.",
    journal = "Atmosphere-Ocean",
    publisher = "Taylor and Francis",
    title = "Storm surges in the Strait of Georgia simulated with a regional
model",
    year = "2016",
    volume = "54",
    number = "1",
    pages = "1-21",
    url = "https://dx.doi.org/10.1080/07055900.2015.1108899",
    abstract = "The Strait of Georgia is a large, semi-enclosed body
of water between Vancouver Island and the mainland of British Columbia
connected to the Pacific Ocean via Juan de Fuca Strait at the south and
Johnstone Strait at the north. During the winter months, coastal communities
along the Strait of Georgia are at risk of flooding caused by storm surges,
a natural hazard that can occur when a strong storm coincides with high tide.
This investigation produces storm surge hindcasts using a three-dimensional
numerical ocean model for the Strait of Georgia and the surrounding bodies
of water (Juan de Fuca Strait, Puget Sound, and Johnstone Strait)
collectively known as the Salish Sea. The numerical model employs the
Nucleus for European Modelling of the Ocean architecture in a regional
configuration. The model is evaluated through comparisons of tidal elevation
harmonics and storm surge with observations. Important forcing factors
contributing to storm surges are assessed. It is shown that surges entering
the domain from the Pacific Ocean make the most significant contribution
to surge amplitude within the Strait of Georgia. Comparisons between
simulations and high-resolution and low-resolution atmospheric forcing
further emphasize that remote forcing is the dominant factor in surge
amplitudes in this region. In addition, local wind patterns caused a slight
increase in surge amplitude on the mainland side of the Strait of Georgia
compared with Vancouver Island coastal areas during a major wind storm on
15 December 2006. Generally, surge amplitudes are found to be greater within
the Strait of Georgia than in Juan de Fuca Strait.",
    doi = "10.1080/07055900.2015.1108899",
}
      </pre>
    </div>
  </div>

  <div class="row">
    <div class="col-md-12">
      <h3>
        Moore-Maley, <em>et al</em>, 2016,
        Locally-driven interannual variability of near-surface pH and ΩA in the Strait of Georgia
      </h3>
    </div>
  </div>
  <div class="row">
    <div class="col-md-8 col-md-offset-1">
      <pre>
@article {Moore-Maley-etal-2016,
    author = "Moore-Maley, Ben L. and Allen, Susan E. and Ianson, Debby",
    title = "Locally driven interannual variability of near-surface pH and ΩA
in the Strait of Georgia",
    journal = "Journal of Geophysical Research: Oceans",
    year = "2016",
    volume = "121",
    number = "3",
    pages = "1600--1625",
    issn = "2169-9291",
    url = "https://dx.doi.org/10.1002/2015JC011118",
    keywords = "Biogeochemical cycles, processes, and modeling, Carbon cycling,
Estuarine processes, Marginal and semi-enclosed seas, Ecosystems, structure,
dynamics, and modeling, acidification, estuarine, ecosystem, modeling, shellfish,
rivers",
    abstract = "Declines in mean ocean pH and aragonite saturation state (ΩA)
driven by anthropogenic CO2 emissions have raised concerns regarding the trends
of pH and ΩA in estuaries. Low pH and ΩA can be harmful to a variety of marine
organisms, especially those with calcium carbonate shells, and so may threaten
the productive ecosystems and commercial fisheries found in many estuarine
environments. The Strait of Georgia is a large, temperate, productive estuarine
system with numerous wild and aquaculture shellfish and finfish populations.
We determine the seasonality and variability of near-surface pH and ΩA in the
Strait using a one-dimensional, biophysical, mixing layer model. We further
evaluate the sensitivity of these quantities to local wind, freshwater, and
cloud forcing by running the model over a wide range of scenarios using
12 years of observations. Near-surface pH and ΩA demonstrate strong seasonal
cycles characterized by low pH, aragonite-undersaturated waters in winter
and high pH, aragonite-supersaturated waters in summer. The aragonite
saturation horizon generally lies at ∼20 m depth except in winter and during
strong Fraser River freshets when it shoals to the surface. Periods of strong
interannual variability in pH and aragonite saturation horizon depth arise in
spring and summer. We determine that at different times of year, each of wind
speed, freshwater flux, and cloud fraction are the dominant drivers of this
variability. These results establish the mechanisms behind the emerging
observations of highly variable near-surface carbonate chemistry in the
Strait.",
    doi = "10.1002/2015JC011118",
}
      </pre>
    </div>
  </div>

  <div class="row">
    <div class="col-md-12">
      <h3>
        Soontiens and Allen, 2017,
        Modelling sensitivities to mixing and advection in a sill-basin estuarine system
      </h3>
    </div>
  </div>
  <div class="row">
    <div class="col-md-8 col-md-offset-1">
      <pre>
@article{Soontiens-Allen-2017,
    author = "Soontiens, N. and Allen, S.",
    title = "Modelling sensitivities to mixing and advection in a sill-basin
estuarine system",
    journal = "Ocean Modelling",
    year = "2017",
    volume = "112",
    number = "",
    pages = "17--32",
    issn = "1463-5003",
    url = "https://dx.doi.org/10.1002/2015JC011118",
    keywords = "Hollingsworth instability, Vertical mixing, Deep water renewal,
Turbulence closures, Advection schemes, NEMO"
    abstract = "This study investigates the sensitivity of a high
resolution regional ocean model to several choices in mixing and advection.
The oceanographic process examined is a deep water renewal event in the
Juan de Fuca Strait–Strait of Georgia sill-basin estuarine system located on
the west coast of North America. Previous observational work has shown that the
timing of the renewal events is linked to the spring/neap tidal cycle, and in
turn, is sensitive to the amount of vertical mixing induced by tidal currents
interacting with sills and complicated bathymetry. It is found that the model’s
representation of deep water renewal is relatively insensitive to several
mixing choices, including the vertical turbulence closure and direction of
lateral mixing. No significant difference in deep or intermediate salinity was
found between cases that used k−ϵk−ϵ versus k−ωk−ω closures and isoneutral
versus horizontal lateral mixing. Modifications that had a stronger effect
included those that involved advection such as modifying the salinity of the
open boundary conditions which supply the source waters for the renewal event.
The strongest impact came from the removal of the Hollingsworth instability,
a kinetic energy sink in the energy-enstrophy discretization of the momentum
equations. A marked improvement to the salinity of the deep water renewal
suggests that the removal of the Hollingsworth instability will correct a fresh
drift in the deep and intermediate waters in an operational version of this
model.",
    doi = "10.1002/2015JC011118",
}
      </pre>
    </div>
  </div>

  <div class="row">
    <div class="col-md-12">
      <h3>
        Olson, <em>et al</em>, 2020,
        Assessment of Nutrient Supply by a Tidal Jet in the Northern Strait of Georgia Based on a Biogeochemical Model
      </h3>
    </div>
  </div>
  <div class="row">
    <div class="col-md-8 col-md-offset-1">
      <pre>
@article{Olson-etal-2020,
    author = "Olson, E. M. and S. E. Allen and V. Do and M. Dunphy and D. Ianson",
    title = "Assessment of Nutrient Supply by a Tidal Jet in the
Northern Strait of Georgia Based on a Biogeochemical Model",
    journal = "Journal of Geophysical Research: Oceans",
    year = "2020",
    url = "https://dx.doi.org/10.1029/2019JC015766",
    keywords = "nitrate, tidal jet, Discovery Passage, Strait of Georgia,
biogeochemical model, new production",
    abstract = "We present a coupled three-dimensional biological-physical model for
the Salish Sea and evaluate it by comparison to nitrate, silicate, and chlorophyll
observations. It accurately reproduces nitrate concentrations with Willmott skill
scores, root mean squared error, and bias ranging from 0.84–0.95, 4.02–6.5 μM,
and −2.33–1.84 μM, respectively, compared to three independent discrete sample
data sets. A prominent feature of the model output is a tidal jet emanating from
Discovery Passage producing a downstream plume of elevated surface nitrate.
The signal is present from April to September, when surface nitrate is otherwise
drawn down. It has a weak but statistically significant correlation to
Discovery Passage tidal velocity (R=0.37, p<0.01). Within the turbulent jet and
associated plume, the average rate of vertical nitrate supply due to mixing and
advection across a depth of roughly 6 m is 0.46 μmol m−2 s−1 between May 15, 2015,
and August 20, 2015, compared to 0.10 μmol m−2 s−1 for the northern Strait of Georgia
as a whole. Close to Discovery Passage, where velocities and shear are strongest,
the majority of the vertical nitrate flux is due to mixing. As velocities weaken
downstream, vertical advection becomes more important relative to mixing, but vertical
velocities also decrease. The tidal pulses out of Discovery Passage drive waves that
contribute net upward nitrate flux as far south as Cape Lazo, 40 km away. The nitrate
supply drives new production, consistent with existing observations. Similar dynamics
have been described in many other tidally influenced coastal systems.",
    doi = "10.1029/2019JC015766",
}
      </pre>
    </div>
  </div>

  <div class="row">
    <div class="col-md-12">
      <h3>
        Jarníková, <em>et al</em>, 2021. 
        A clustering approach to determine biophysical provinces and physical drivers of 
        productivity dynamics in a complex coastal sea. 
      </h3>
    </div>
  </div>
  <div class="row">
    <div class="col-md-8 col-md-offset-1">
      <pre>
@article{Jarnikova-etal-2021,
    author = "Jarníková, T., Olson, E. M., Allen, S. E., Ianson, D., and Suchy, K. D.",
    title = "A clustering approach to determine biophysical provinces and physical 
drivers of productivity dynamics in a complex coastal sea",
    journal = "Ocean Sci. Discuss.",
    year = "2021",
    url = "https://doi.org/10.5194/os-2021-66",
    abstract = "The balance between ocean mixing and stratification influences 
primary productivity through light limitation and nutrient supply in the 
euphotic ocean. Here, we apply a hierarchical clustering algorithm 
(Ward's method) to four factors relating to stratification and depth-integrated 
phytoplankton biomass extracted from a biophysical regional ocean model of the 
Salish Sea to assess spatial co-occurrence. Running the clustering algorithm on 
four years of model output, we identify distinct regions of the model domain that 
exhibit contrasting wind and freshwater input dynamics, as well as regions of 
varying watercolumn-averaged vertical eddy diffusivity and halocline depth regimes. 
The spatial regionalizations in physical variables are similar in all four 
analyzed years. We also find distinct interannually consistent biological zones. 
In the Northern Strait of Georgia and Juan de Fuca Strait, a deeper winter 
halocline and episodic summer mixing coincide with higher summer diatom abundance, 
while in the Fraser River stratified Central Strait of Georgia, shallower 
haloclines and stronger summer stratification coincide with summer flagellate 
abundance. Cluster based model results and evaluation suggest that the 
Juan de Fuca Strait supports more biomass than previously thought. Our approach 
elucidates probable physical mechanisms controlling phytoplankton abundance and 
composition. It also demonstrates a simple, powerful technique for finding 
structure in large datasets and determining boundaries of biophysical provinces.",
    doi = "10.5194/os-2021-66",
}
      </pre>
    </div>
  </div>
</div>
