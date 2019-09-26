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


class DescribePoliciesRequest(JDCloudRequest):
    """
    查询策略列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribePoliciesRequest, self).__init__(
            '/policies', 'GET', header, version)
        self.parameters = parameters


class DescribePoliciesParameters(object):

    def __init__(self, ):
        """
        """

        self.pageNumber = None
        self.pageSize = None
        self.keyword = None
        self.queryType = None
        self.sort = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码，默认1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认50，取值范围[10, 100]
        """
        self.pageSize = pageSize

    def setKeyword(self, keyword):
        """
        :param keyword: (Optional) 关键字
        """
        self.keyword = keyword

    def setQueryType(self, queryType):
        """
        :param queryType: (Optional) 策略类型：0-全部（默认），1-系统策略，2-自定义策略
        """
        self.queryType = queryType

    def setSort(self, sort):
        """
        :param sort: (Optional) 排序规则：0-创建时间顺序排序，1-创建时间倒序排序
        """
        self.sort = sort

