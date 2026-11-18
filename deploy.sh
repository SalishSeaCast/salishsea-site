#!/usr/bin/env bash

# Copyright 2014 – present by the Mesoscale Ocean and Atmospheric Dynamics (MOAD) group
# in the Department of Earth, Ocean, and Atmospheric Sciences
# at The University of British Columbia
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

# SPDX-License-Identifier: Apache-2.0


# Deploy changes to site by pulling revisions from GitHub, updating Pixi environment, and restarting app server

APP_REPO=/SalishSeaCast/salishsea-site
GIT=/usr/bin/git

cd ${APP_REPO}
echo $(pwd)
GIT_SSH_COMMAND='ssh -i ~/.ssh/salishsea-site-deployment_id_rsa -o IdentitiesOnly=yes' ${GIT} pull
echo "Updating environment"
source.env
pixi run supervisorctl --configuration supervisord-prod.ini shutdown
pixi install --frozen
echo "Restarting app"
pixi run supervisord --configuration supervisord-prod.ini
