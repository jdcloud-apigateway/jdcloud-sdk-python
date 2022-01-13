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


class UpgradeEngineVersionRequest(JDCloudRequest):
    """
    升级引擎版本，例如从5.7.21 升级到5.7.24，仅支持MySQL
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpgradeEngineVersionRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:upgradeEngineVersion', 'POST', header, version)
        self.parameters = parameters


class UpgradeEngineVersionParameters(object):

    def __init__(self, regionId, instanceId, upgradeSchedule, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param upgradeSchedule: 计划开始升级的时间，1：立即开始升级，2：维护时间窗口升级，0：取消升级
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.upgradeSchedule = upgradeSchedule
        self.newVersion = None

    def setNewVersion(self, newVersion):
        """
        :param newVersion: (Optional) 升级到的新版本，默认为当前实例可升级到的最新版本
        """
        self.newVersion = newVersion
