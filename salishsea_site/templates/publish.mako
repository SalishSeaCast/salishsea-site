<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width initial-scale=1">

  <title>
    <%block name="title">Salish Sea</%block>
  </title>
</head>

<body>
  <h1 id="top">${results_date.format('dddd, D MMMM YYYY')} — Salish Sea Storm Surge ${run_type.title()}</h1>

  <h3 id="${plot_title.replace(' ', '-').lower()}">
    ${plot_title}
    <a class="headerlink" href="#${plot_title.replace(' ', '-').lower()}" title="Permalink to this headline">¶</a>
  </h3>
  <img class="img-responsive"
    src="${request.static_url(
            '/results/nowcast-sys/figures/{run_type}/{run_dmy}/{svg_file}_{run_dmy}.svg'
            .format(run_type=run_type, svg_file=svg_file, run_dmy=run_date.format('DDMMMYY').lower()))}"
    alt="${plot_title} image">
</body>
</html>
