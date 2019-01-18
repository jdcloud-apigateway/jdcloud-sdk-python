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


class DescribeLiveStreamPublishListRequest(JDCloudRequest):
    """
    查看域名下推流记录
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeLiveStreamPublishListRequest, self).__init__(
            '/streams/{publishDomain}/publishList', 'GET', header, version)
        self.parameters = parameters


class DescribeLiveStreamPublishListParameters(object):

    def __init__(self, publishDomain, startTime, ):
        """
        :param publishDomain: 推流域名
        :param startTime: 起始时间
        """

        self.publishDomain = publishDomain
        self.pageNum = None
        self.pageSize = None
        self.appName = None
        self.streamName = None
        self.startTime = startTime
        self.endTime = None

    def setPageNum(self, pageNum):
        """
        :param pageNum: (Optional) 页码；默认为1；取值范围[1, 100000]
        """
        self.pageNum = pageNum

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；默认为10；取值范围[10, 100]
        """
        self.pageSize = pageSize

    def setAppName(self, appName):
        """
        :param appName: (Optional) 直播流所属应用名称
        """
        self.appName = appName

    def setStreamName(self, streamName):
        """
        :param streamName: (Optional) 直播流名称
        """
        self.streamName = streamName

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 结束时间
        """
        self.endTime = endTime
