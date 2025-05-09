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


class GravityParticleJobMonitorJobDispatchTrendRequest(JDCloudRequest):
    """
    将作业按趋势进行数据量的统计
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(GravityParticleJobMonitorJobDispatchTrendRequest, self).__init__(
            '/regions/{regionId}/apps/{appName}/gravityParticleJobMonitorJobDispatchTrend', 'GET', header, version)
        self.parameters = parameters


class GravityParticleJobMonitorJobDispatchTrendParameters(object):

    def __init__(self,regionId, appName, dimType, slot):
        """
        :param regionId: 地域ID
        :param appName: 应用名称
        :param dimType: 统计维度：job作业，inst实例
        :param slot: 统计范围天数
        """

        self.regionId = regionId
        self.appName = appName
        self.isMine = None
        self.dimType = dimType
        self.slot = slot

    def setIsMine(self, isMine):
        """
        :param isMine: (Optional) 是否统计本人作业
        """
        self.isMine = isMine

