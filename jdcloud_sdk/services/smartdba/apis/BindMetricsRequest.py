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


class BindMetricsRequest(JDCloudRequest):
    """
    关联实例自定义监控项，每次都要求全量提交
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(BindMetricsRequest, self).__init__(
            '/regions/{regionId}/bindMetrics', 'POST', header, version)
        self.parameters = parameters


class BindMetricsParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域代码
        """

        self.regionId = regionId
        self.metricIds = None
        self.panelType = None
        self.gid = None

    def setMetricIds(self, metricIds):
        """
        :param metricIds: (Optional) 自定义的监控项id数组
        """
        self.metricIds = metricIds

    def setPanelType(self, panelType):
        """
        :param panelType: (Optional) 展示类型，取值为： real_time 表示实时监控页面, monitor 表示性能趋势页面 market 表示监控大盘
        """
        self.panelType = panelType

    def setGid(self, gid):
        """
        :param gid: (Optional) RDS 实例ID，唯一标识一个RDS实例。如果全部实例生效，可以传all
        """
        self.gid = gid

