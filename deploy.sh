#!/usr/bin/env bash

# Copyright 2014-2019 The Salish Sea MEOPAR Contributors
# and The University of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Deploy changes to site by pulling changesets from Bitbucket and restarting app server

APP_REPO=/SalishSeaCast/salishsea-site
APP_ENV=/SalishSeaCast/salishsea-site-env
HG=/usr/local/bin/hg

cd ${APP_REPO}
echo $(pwd)
${HG} pull --ssh "ssh -i ~/.ssh/salishsea-site-deployment_id_rsa" --update
echo "Restarting app"
${APP_ENV}/bin/circusctl --endpoint tcp://127.0.0.1:7777 restart web
