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


class QueryDomainLogRequest(JDCloudRequest):
    """
    查询日志
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryDomainLogRequest, self).__init__(
            '/domain/{domain}/log', 'GET', header, version)
        self.parameters = parameters


class QueryDomainLogParameters(object):

    def __init__(self,domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.startTime = None
        self.endTime = None
        self.interval = None
        self.logType = None
        self.pageSize = None
        self.pageNumber = None

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询起始时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2018-10-21T10:00:00Z
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询截止时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2018-10-21T10:00:00Z
        """
        self.endTime = endTime

    def setInterval(self, interval):
        """
        :param interval: (Optional) 时间间隔，取值(hour，day，fiveMin)，不传默认小时。
        """
        self.interval = interval

    def setLogType(self, logType):
        """
        :param logType: (Optional) 日志类型，取值(log，zip,gz)，不传默认gz。
        """
        self.logType = logType

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页面大小，默认值10
        """
        self.pageSize = pageSize

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 分页页数，默认值1
        """
        self.pageNumber = pageNumber

