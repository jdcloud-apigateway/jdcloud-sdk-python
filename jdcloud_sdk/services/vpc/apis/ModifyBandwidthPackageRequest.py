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


class ModifyBandwidthPackageRequest(JDCloudRequest):
    """
    
修改共享带宽包信息，包括带宽上限及共享带宽包名称、描述信息。

## 接口说明

- 如共享带宽包中的弹性公网 IP 有单独限速。共享带宽包的带宽上限值不能低于其包含任一弹性公网IP的带宽上限值。

- 欠费或到期的共享带宽包资源不支持修改带宽上限。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyBandwidthPackageRequest, self).__init__(
            '/regions/{regionId}/bandwidthPackages/{bandwidthPackageId}', 'PATCH', header, version)
        self.parameters = parameters


class ModifyBandwidthPackageParameters(object):

    def __init__(self, regionId,bandwidthPackageId,):
        """
        :param regionId: Region ID
        :param bandwidthPackageId: 共享带宽包ID
        """

        self.regionId = regionId
        self.bandwidthPackageId = bandwidthPackageId
        self.bandwidthMbps = None
        self.name = None
        self.description = None

    def setBandwidthMbps(self, bandwidthMbps):
        """
        :param bandwidthMbps: (Optional) 共享带宽包带宽上限，取值范围200-5000，单位为Mbps，且不能低于共享带宽包内公网IP带宽上限
        """
        self.bandwidthMbps = bandwidthMbps

    def setName(self, name):
        """
        :param name: (Optional) 名称，只支持中文、数字、大小写字母、英文下划线“_”及中划线“-”，且长度不超过32个字符
        """
        self.name = name

    def setDescription(self, description):
        """
        :param description: (Optional) 描述，长度不超过256个字符
        """
        self.description = description
