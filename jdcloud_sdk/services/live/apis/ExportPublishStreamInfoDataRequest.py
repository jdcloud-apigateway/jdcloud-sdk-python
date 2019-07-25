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


class ExportPublishStreamInfoDataRequest(JDCloudRequest):
    """
    导出推流监控数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ExportPublishStreamInfoDataRequest, self).__init__(
            '/exportPublishStreamInfoData', 'GET', header, version)
        self.parameters = parameters


class ExportPublishStreamInfoDataParameters(object):

    def __init__(self, domainName, appName, streamName, startTime, ):
        """
        :param domainName: 推流域名
        :param appName: 应用名称
        :param streamName: 流名称
        :param startTime: 起始时间
- UTC时间
  格式:yyyy-MM-dd'T'HH:mm:ss'Z'
  示例:2018-10-21T10:00:00Z

        """

        self.domainName = domainName
        self.appName = appName
        self.streamName = streamName
        self.startTime = startTime
        self.endTime = None

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 结束时间:
- UTC时间
  格式:yyyy-MM-dd'T'HH:mm:ss'Z'
  示例:2018-10-21T10:00:00Z
- 为空,默认为当前时间，查询时间跨度不超过1天

        """
        self.endTime = endTime

