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


class DelSubDeviceWithCoreRequest(JDCloudRequest):
    """
    删除子设备
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(DelSubDeviceWithCoreRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/products/{productKey}/edges/{edgeName}:delSubDevice', 'POST', header, version)
        self.parameters = parameters


class DelSubDeviceWithCoreParameters(object):

    def __init__(self, regionId, instanceId, edgeName, productKey, ):
        """
        :param regionId: 地域ID
        :param instanceId: IoTCore实例编号
        :param edgeName: Edge名称
        :param productKey: Edge对应的产品key
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.edgeName = edgeName
        self.productKey = productKey
        self.delDevices = None

    def setDelDevices(self, delDevices):
        """
        :param delDevices: (Optional) 设备名称
        """
        self.delDevices = delDevices

