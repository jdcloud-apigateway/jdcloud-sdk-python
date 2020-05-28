# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class DeviceQueryRequest(JDCloudRequest):
    """
    查询单个设备详细信息
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(DeviceQueryRequest, self).__init__(
            '/regions/{regionId}/coreinstances/{instanceId}/device:query', 'GET', header, version)
        self.parameters = parameters


class DeviceQueryParameters(object):

    def __init__(self, regionId, instanceId, deviceId):
        """
        :param regionId: 区域id
        :param instanceId: 实例Id
        :param deviceId: 设备ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.deviceId = deviceId

