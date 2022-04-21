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


class DescribeDedicatedHostsRequest(JDCloudRequest):
    """
    查询专有宿主机列表。<br>
此接口支持分页查询，默认每页20条。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeDedicatedHostsRequest, self).__init__(
            '/regions/{regionId}/dedicatedHosts', 'GET', header, version)
        self.parameters = parameters


class DescribeDedicatedHostsParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；默认为20；取值范围[10, 100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) dedicatedHostId - 专有宿主机ID，精确匹配，支持多个
az - 可用区，精确匹配，支持多个
status - 专有宿主机状态，精确匹配，支持多个，<a href="http://docs.jdcloud.com/dedicated-hosts/api/dh_status">参考专有宿主机状态</a>
name - 专有宿主机名称，模糊匹配，支持单个
dedicatedPoolId - 专有宿主机池ID，精确匹配，支持多个
dedicatedHostType - 专有宿主机机型，精确匹配，支持多个

        """
        self.filters = filters

