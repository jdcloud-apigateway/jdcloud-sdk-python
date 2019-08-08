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


class QueryServersRequest(JDCloudRequest):
    """
    查询后端服务器列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryServersRequest, self).__init__(
            '/regions/{regionId}/serverGroups/{serverGroupId}/servers', 'GET', header, version)
        self.parameters = parameters


class QueryServersParameters(object):

    def __init__(self, regionId, serverGroupId, ):
        """
        :param regionId: 地域ID，可调用接口（describeRegiones）获取云物理服务器支持的地域
        :param serverGroupId: 服务器组ID
        """

        self.regionId = regionId
        self.serverGroupId = serverGroupId
        self.pageNumber = None
        self.pageSize = None
        self.listenerId = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；默认为20；取值范围[20, 100]
        """
        self.pageSize = pageSize

    def setListenerId(self, listenerId):
        """
        :param listenerId: (Optional) 监听器Id
        """
        self.listenerId = listenerId

    def setFilters(self, filters):
        """
        :param filters: (Optional) serverId - 后端服务器ID，精确匹配，支持多个

        """
        self.filters = filters
