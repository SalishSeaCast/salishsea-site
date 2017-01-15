## Copyright 2013-2016 The Salish Sea MEOPAR Contributors
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
  SalishSeaCast NEMO Model
</%block>

<div class="container">
  <div class="row">
    <div class="col-md-12">
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
        modelling architecture the Salish Sea model will be used to evaluate
        storm surge risk in coastal communities.
        Long term goals include data assimilation from the VENUS network and a coupled
        biogeochemical modelling component.
      </p>

      <h3>Results</h3>
      <p>Our results are available in a number of formats:</p>
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

      <h3>Domain</h3>
      <img class="img-responsive center-block"
           src="${request.static_path('salishsea_site:static/img/SalishSeaImage.png')}"
           alt="SalishSeaCast NEMO Model Domain">

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
        Under revision for <em>Ocean Modelling</em>)
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
          <a href="https://www.mercurial-scm.org/">Mercurial</a>
          version control repositories for code,
          documentation 
          (including the source files for this site),
          and analyses of model results.
          The contents of those repositories and their development history is accessible at 
          <a href="https://bitbucket.org/salishsea/">https://bitbucket.org/salishsea/</a>.
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
        <li><a href="https://ca.linkedin.com/in/jie-liu-0a93a5ab">Jie Liu</a></li>
        <li><a href="http://www.nancysoontiens.com">Nancy Soontiens</a> (emeritus)</li>
        <li>Kate Le Souëf (emeritus)</li>
        <li>Idalia Machuca (emeritus)</li>
        <li>Muriel Dunn (emeritus)</li>
        <li>James Petrie (emeritus)</li>
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
        <ul>
          <li>Keith Thompson, Dalhousie University</li>
          <li>Vasily Korabel, Dalhousie University</li>
          <li>Youyu Lu, Fisheries and Oceans Canada</li>
          <li>J-P Paquin, Dalhousie University</li>
          <li>Fatemeh Chegini, Dalhousie University</li>
          <li>Luc Fillion, Environment Canada</li>
          <li>Kao-Shen Chung, Environment Canada</li>
          <li>Weiguang Chang, Environment Canada</li>
          <li>Jim Christian, Environment Canada</li>
          <li>Olivier Riche, Environment Canada</li>
        </ul>
      </p>
      <p>
        and with many other researchers,
        including:
        <ul>
          <li>Mike Foreman, Fisheries and Oceans Canada</li>
          <li>Charles Hannah, Fisheries and Oceans Canada</li>
          <li>Debby Ianson, Fisheries and Oceans Canada</li>
          <li>Diane Masson, Fisheries and Oceans Canada</li>
          <li>John Morrison, Fisheries and Oceans Canada</li>
          <li>Paul Myers, University of Alberta</li>
          <li>Angelica Pena, Fisheries and Oceans Canada</li>
          <li>Neil Swart, Environment Canada</li>
          <li>Pramod Thupaki, Fisheries and Oceans Canada</li>
        </ul>
      </p>
    </div>
  </div>
</div>
