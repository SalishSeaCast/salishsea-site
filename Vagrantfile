# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrant VM configuration to emulate salishsea-site app
# deployment on skookum.eos.ubc.ca


# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.define "salishsea_site" do |salishsea_site|
    # Ubuntu 14.04 LTS
    salishsea_site.vm.box = "ubuntu/trusty64"
    salishsea_site.vm.provider "virtualbox" do |v|
      v.memory = 1024
    end

    salishsea_site.vm.network :forwarded_port, guest: 80, host: 4567

    config.ssh.forward_agent = true
  end


  # Mount app dev tree in VM
  config.vm.synced_folder ".", "/SalishSeaCast/salishsea-site",
    create: true


  # Provisioning
  config.vm.provision "shell", inline: <<-SHELL
    add-apt-repository -y ppa:mercurial-ppa/releases
    apt-get update

    TIMEZONE=Canada/Pacific
    echo "Set timezone to ${TIMEZONE}"
    timedatectl set-timezone ${TIMEZONE}

    apt-get install -y mg
    apt-get install -y sshfs
    apt-get install -y apache2 libapache2-mod-proxy-html libxml2-dev


    mkdir -p /var/www/html && chgrp vagrant /var/www/html && chmod 775 /var/www/html

    cat << EOF > /etc/apache2/sites-available/salishsea.eos.ubc.ca.conf
<VirtualHost *:80>
    ServerAdmin admin@salishsea.eos.ubc.ca
    ServerName localhost
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    ProxyRequests Off
    ProxyPreserveHost On
    ProxyPass / http://0.0.0.0:6543/
    ProxyPassReverse / http://0.0.0.0:6543/
</VirtualHost>
EOF
    /usr/sbin/a2enmod proxy_http rewrite cache headers
    /usr/sbin/a2ensite salishsea.eos.ubc.ca.conf
    /usr/sbin/a2dissite 000-default.conf
    service apache2 restart


    mkdir -p /results/nowcast-sys
    chown vagrant:vagrant /results
    chown vagrant:vagrant /results/nowcast-sys
    su vagrant -c ' \
      mkdir -p /results/nowcast-sys/figures/bloomcast \
      mkdir -p /results/nowcast-sys/figures/forecast \
      mkdir -p /results/nowcast-sys/figures/forecast2 \
      mkdir -p /results/nowcast-sys/figures/fvcom/forecast \
      mkdir -p /results/nowcast-sys/figures/fvcom/nowcast \
      mkdir -p /results/nowcast-sys/figures/monitoring \
      mkdir -p /results/nowcast-sys/figures/nowcast \
      mkdir -p /results/nowcast-sys/figures/nowcast-agrif \
      mkdir -p /results/nowcast-sys/figures/nowcast-green \
      mkdir -p /results/nowcast-sys/figures/salishsea-site/static/img \
      mkdir -p /results/nowcast-sys/figures/storm-surge/atom \
      mkdir -p /results/nowcast-sys/figures/surface_currents/forecast \
      mkdir -p /results/nowcast-sys/figures/surface_currents/forecast2 \
      mkdir -p /results/nowcast-sys/figures/surface_currents/nowcast-green \
      mkdir -p /results/nowcast-sys/figures/wwatch3/forecast \
      mkdir -p /results/nowcast-sys/figures/wwatch3/forecast2 \
    '
    NOWCAST_SYS=/results/nowcast-sys


    VAGRANT_HOME=/home/vagrant
    MINICONDA_INSTALLER=http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    if [ -d $VAGRANT_HOME/miniconda ]; then
      echo "Miniconda already installed"
    else
      echo "Downloading Miniconda installer from continuum.io"
      su vagrant -c " \
        wget -q $MINICONDA_INSTALLER -O $VAGRANT_HOME/miniconda.sh \
      "
      echo "Installing $VAGRANT_HOME/miniconda"
      su vagrant -c " \
        bash $VAGRANT_HOME/miniconda.sh -b -p $VAGRANT_HOME/miniconda \
      "
    fi

    CONDA_BIN=$VAGRANT_HOME/miniconda/bin
    CONDA=$CONDA_BIN/conda
    touch $VAGRANT_HOME/.bash_aliases && chown vagrant:vagrant $VAGRANT_HOME/.bash_aliases
    su vagrant -c " \
      echo export PATH=$CONDA_BIN:\$PATH > $VAGRANT_HOME/.bash_aliases \
    "


########################################################
# Environment for salishsea-site Pyramid app
########################################################
    SALISHSEACAST=/SalishSeaCast
    mkdir -p ${SALISHSEACAST} && chown vagrant:vagrant ${SALISHSEACAST}
    SALISHSEA_SITE_ENV=${SALISHSEACAST}/salishsea-site-env
    PIP=${SALISHSEA_SITE_ENV}/bin/pip
    if [ -d ${SALISHSEA_SITE_ENV} ]; then
      echo "${SALISHSEA_SITE_ENV} conda env already exists"
    else
      echo "Creating ${SALISHSEA_SITE_ENV} conda env"
      su vagrant -c " \
        $CONDA create --yes \
          --channel conda-forge --channel defaults \
          --prefix ${SALISHSEA_SITE_ENV} \
          pip \
          python=3.6 \
          pyyaml \
          'pyzmq<17.0,>=13.1.0' \
          requests \
      "
      echo "Installing pip packages into ${SALISHSEA_SITE_ENV} conda env"
      su vagrant -c " \
        $PIP install \
          arrow \
          attrs \
          chaussette \
          circus \
          pyramid \
          pyramid-crow \
          pyramid-debugtoolbar \
          pyramid-mako \
          waitress==0.9.0 \
        "
      echo "Installing editable salishsea-site package into ${SALISHSEA_SITE_ENV} conda env"
      su vagrant -c " \
        ${PIP} install --editable ${SALISHSEACAST}/salishsea-site/ \
      "
    fi

    su vagrant -c " \
      echo source activate ${SALISHSEA_SITE_ENV} >> ${VAGRANT_HOME}/.bash_aliases \
    "

    su vagrant -c " \
      ln -s ${SALISHSEACAST}/salishsea_site/salishsea_site/static/img/index_page ${NOWCAST_SYS}/figures/salishsea-site/static/img/ \
    "

    echo "Setting up ${SALISHSEA_SITE_ENV} activate/deactivate hooks that export/unset environment variables"
    su vagrant -c " \
      mkdir -p ${SALISHSEA_SITE_ENV}/etc/conda/activate.d \
      && cat << EOF > ${SALISHSEA_SITE_ENV}/etc/conda/activate.d/envvars.sh
export SALISHSEA_SITE_ENV=${SALISHSEA_SITE_ENV}
export SALISHSEA_SITE=${SALISHSEACAST}/salishsea_site/
export NOWCAST_LOGS=${SALISHSEACAST}/logs/nowcast/
export SENTRY_DSN=
EOF"
    su vagrant -c " \
      mkdir -p ${SALISHSEA_SITE_ENV}/etc/conda/deactivate.d \
      && cat << EOF > ${SALISHSEA_SITE_ENV}/etc/conda/deactivate.d/envvars.sh
unset SALISHSEA_SITE_ENV
unset SALISHSEA_SITE
unset NOWCAST_LOGS
unset SENTRY_DSN
EOF"

  SHELL
end
