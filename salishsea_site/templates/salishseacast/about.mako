## Copyright 2014-2019 The Salish Sea MEOPAR Contributors
## and The University of British Columbia
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

<%inherit file="../site.mako"/>

<%block name="title">
  SalishSeaCast NEMO Model
</%block>

<div class="container">
  <div class="row">
    <div class="col-md-10 col-md-offset-1">
      <h1>SalishSeaCast NEMO Model</h1>

      <h2>About the Project</h2>
      <p>
        The Salish Sea is home to a large population of Canadians living in coastal communities
        at risk to ocean related hazards.
        There is an ongoing need to assess the impact of these hazards on human and
        marine environments through a multidisciplinary approach involving Canadian oceanographers,
        biologists,
        and social scientists.
        The Marine Environmental Observation Prediction and Response network
        (<a href="http://meopar.ca/">MEOPAR</a>)
        provides a platform to accelerate this type of research.
      </p>
      <p>
        The Salish Sea MEOPAR project team is developing a three-dimensional ocean model
        for the Strait of Georgia and Salish Sea.
        Using the
        <a href="http://www.nemo-ocean.eu/">NEMO</a>
        modelling architecture, the Salish Sea model will be used to evaluate
        storm surge risk in coastal communities.
        Long term goals include data assimilation from the VENUS network and a coupled
        biogeochemical modelling component.
      </p>

      <h3>Model Domain</h3>
      <p>
         The region covered by the model includes the Straight of Georgia, Straight of Juan de Fuca, Johnstone Strait, Fraser River, and other connecting waterways.
      </p>
      <img class="img-responsive center-block"
           src="${request.static_path('salishsea_site:static/img/SalishSeaImage.png')}"
           alt="SalishSeaCast NEMO Model Domain">

      <h3>Results</h3>
      <p>
        Our model results include storm surge alerts and the region's atmospheric and marine conditions. They are available in a number of formats:
      </p>
      <ul>
        <li>
          Our Storm Surge forecast:
          <a href=${request.route_url('storm_surge.forecast')}>${request.route_url('storm_surge.forecast')}</a>
        </li>
        <li>
          A more general storm surge portal:
          <a href=${request.route_url('storm_surge.portal')}>${request.route_url('storm_surge.portal')}</a>
        </li>
        <li>
          You can subscribe to our storm surge atom feed for Vancouver:
          <a href=${request.route_url('storm_surge.alert.feed', filename='pmv.xml')}>
            ${request.route_url('storm_surge.alert.feed', filename='pmv.xml')}
          </a>
        </li>
        <li>
          Static plots of our results are:
          <a href=${request.route_url('results.index')}>${request.route_url('results.index')}</a>
        </li>
        <li>
          Animations on ocean viewer:
          <a href="http://oceanviewer.org">http://oceanviewer.org/</a>
        </li>
        <li>
          Full access to our nowcast results in numerous formats via an ERDDAP server:
          <a href=${request.erddap_url}>${request.erddap_url}</a>
        </li>
      </ul>

      <h3>Evaluation</h3>
      <p>
        <strong>General evaluation:</strong> as a
        <a href=${request.static_path('salishsea_site:static/pdf/model_evaluation_summary.pdf')}>slide presentation</a>
      </p>
      <p>
        <strong>Storm surge:</strong>
        The Salish Sea model's ability to calculate tides and sea surface height was evaluated
        by hindcasting storm surge events that occurred between 2002 and 2011.
        (Soontiens, N., Allen, S., Latornell, D., Le Souef, K., Machuca, I., Paquin, J.-P.,
        Lu, Y., Thompson, K., Korabel, V., 2016.
        Storm surges in the Strait of Georgia simulated with a regional model.
        <em>Atmosphere-Ocean</em> <strong>54</strong> 1-21.
        <a href="https://dx.doi.org/10.1080/07055900.2015.1108899">https://dx.doi.org/10.1080/07055900.2015.1108899</a>)
      </p>
      <p>
        <strong>Mixing in San Juan/Gulf Islands:</strong>
        The sensitivity of the deep water renewal into the Strait of Georgia and of fresh water
        pulses into Juan de Fuca Strait to modelling choices affecting both turbulence and
        advection has been determined.
        (Soontiens, N. and Allen, S.
        Modelling sensitivities to mixing and advection in a sill-basin estuarine system.
        <em>Ocean Modelling</em>, <strong>112</strong>, 17-32.
        <a href="https://dx.doi.org/10.1016/j.ocemod.2017.02.008" title="Link to paper via DOI">
          https://dx.doi.org/10.1016/j.ocemod.2017.02.008
        </a>
      </p>

      <h2>Project Resources</h2>
      <ul>
        <li>
          The main project documentation site is at
          <a href="https://salishsea-meopar-docs.readthedocs.io/en/latest/">
            https://salishsea-meopar-docs.readthedocs.io/en/latest/
          </a>.
        </li>
        <li>
          The project team maintains a set of
          <a href="https://git-scm.com/">Git</a>
          version control repositories for code,
          documentation
          (including the source files for this site),
          and analyses of model results.
          The contents of those repositories and their development history is accessible at
          <a href="https://github.com/SalishSeaCast">https://github.com/SalishSeaCast</a>.
        </li>
      </ul>

      <h2>Project Team and Collaborators</h2>
      <p>
        The Salish Sea NEMO Model project is lead by
        <a href="https://www.eoas.ubc.ca/~sallen/">Susan Allen</a>
        in the Department of Earth, Ocean, and Atmospheric Sciences
        at the University of British Columbia.
        Other team members:
      </p>
      <ul>
        <li><a href="https://www.eoas.ubc.ca/~eolson/">Elise Olson</a></li>
        <li>Michael Dunphy</li>
        <li>Doug Latornell</li>
        <li><a href="http://www.eoas.ubc.ca/about/grad/B.Moore-Maley.html">Ben Moore-Maley</a></li>
        <li>Tereza Jarníková</li>
        <li><a href="http://www.nancysoontiens.com">Nancy Soontiens</a> (emeritus)</li>
        <li>Kate Le Souëf (emeritus)</li>
        <li><a href="https://ca.linkedin.com/in/jie-liu-0a93a5ab">Jie Liu</a> (emeritus)</li>
        <li>Idalia Machuca (emeritus)</li>
        <li>Muriel Dunn (emeritus)</li>
        <li>James Petrie (emeritus)</li>
        <li>Giorgio Sgarbi (emeritus)</li>
        <li>Vicky Do (emeritus)</li>
      </ul>
      <p>
        The team collaborates with other
        <a href="http://meopar.ca/">MEOPAR</a>
        funded research teams at UBC:
      </p>
      <ul>
        <li>
          The observations team in EOAS lead by
          <a href="https://www.eoas.ubc.ca/~rich/research.html">Rich Pawlowicz</a>:
          <ul>
            <li>Mark Halverson</li>
            <li>Romain Di Costanzo</li>
            <li>Chuning Wang (emeritus)</li>
          </ul>
        </li>
        <li>
          The impacts and indictors of marine hazards team in the UBC School of Community and Regional Planning lead by
          <a href="https://sites.google.com/site/stephanieechang1/home">Stephanie Chang</a>:
          <ul>
            <li>Jackie Yip</li>
            <li>Rebecca Chaster</li>
            <li>Ashley Lowcock</li>
            <li>Michelle Marteleira</li>
            <li>Greg Oulahen</li>
            <li>Shona van Zijll de jong (emeritus)</li>
            <li>Christopher Carter (emeritus)</li>
          </ul>
        </li>
      </ul>
      <p>
        We also collaborate with
        <a href="http://meopar.ca/">MEOPAR</a>
        researchers and
        <a href="http://www.nemo-ocean.eu/">NEMO</a>
        users across Canada:
      </p>
      <ul>
        <li>Keith Thompson, Dalhousie University</li>
        <li>Vasily Korabel, Dalhousie University</li>
        <li>Youyu Lu, Fisheries and Oceans Canada</li>
        <li>J-P Paquin, Environment and Climate Change, Canada</li>
        <li>Fatemeh Chegini, Dalhousie University</li>
        <li>Luc Fillion, Environment Canada</li>
        <li>Kao-Shen Chung, Environment Canada</li>
        <li>Weiguang Chang, Environment Canada</li>
        <li>Jim Christian, Environment Canada</li>
        <li>Olivier Riche, Environment Canada</li>
      </ul>
      <p>
        Much of our evaluation data, some of our funding, and access to computing
        resources for our daily runs comes from <a href="http://www.oceannetworks.ca/">Ocean Networks Canada (ONC)</a>
        Our contacts with ONC include:
      </p>
      <ul>
        <li> Richard Dewey, Associate Director, Science</li>
        <li> Steve Mihaly, Senior Staff Scientist</li>
        <li> Mike Morley, Data Manager</li>
        <li> Akash Sastri, Senior Staff Scientist</li>
        <li> Lu Guan, Junior Staff Scientist</li>
        <li> Dwight Owens, User Engagement</li>
        <li> Leslie Elliot, Communications Manager</li>
      </ul>
      <p>
        Other funders include:
      </p>
      <ul>
        <li> <a href="https://www.psf.ca/">Pacific Salmon Foundation</a></li>
        <li> <a href="http://www.metrovancouver.org/">Metro Vancouver</a></li>
      </ul>
      <p>
        We collaborate with many other researchers,
        including:
      </p>
      <ul>
        <li>Hayley Dosser, Hakai Foundation</li>
        <li>Michael Dunphy, Fisheries and Oceans Canada</li>
        <li>Mike Foreman, Fisheries and Oceans Canada</li>
        <li>Charles Hannah, Fisheries and Oceans Canada</li>
        <li>Debby Ianson, Fisheries and Oceans Canada</li>
        <li>Diane Masson, Fisheries and Oceans Canada</li>
        <li>Parker MacCready, University of Washington</li>
        <li>John Morrison, Fisheries and Oceans Canada</li>
        <li>Paul Myers, University of Alberta</li>
        <li>Angelica Pena, Fisheries and Oceans Canada</li>
        <li>Greg Smith, Enivironment and Climate Change, Canada
        <li>Neil Swart, Environment  and Climate Change, Canada</li>
        <li>Pramod Thupaki, Hakai Foundation</li>
      </ul>
    </div>
  </div>
</div>
