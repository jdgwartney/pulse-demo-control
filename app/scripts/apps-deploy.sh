#!/bin/bash
#
# Copyright 2016 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
set -x
stack_id=e9c7a15b-180a-42bb-becb-40fed055f4bc
app_id=ae0a0232-a545-4250-99a3-5243d9b2c570
instance_ids="36bacec9-63e1-4739-b63c-0720dd05ef01 a92758a2-6512-4da9-913e-d7df8820a152"

aws opsworks create-deployment --stack-id $stack_id --app-id $app_id --command "{\"Name\":\"deploy\"}" --instance-ids $instance_ids

