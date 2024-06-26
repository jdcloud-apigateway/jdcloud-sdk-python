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


class DescribeCustomizedConfigurationsRequest(JDCloudRequest):
    """
    查询个性化配置列表详情
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeCustomizedConfigurationsRequest, self).__init__(
            '/regions/{regionId}/customizedConfigurations/', 'GET', header, version)
        self.parameters = parameters


class DescribeCustomizedConfigurationsParameters(object):

    def __init__(self,regionId, ):
        """
        :param regionId: Region ID
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1, 取值范围：[1,∞), 页码超过总页数时, 显示最后一页
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为20，取值范围：[10,100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) customizedConfigurationIds - 个性化配置ID，支持多个
customizedConfigurationNames - 个性化配置名称，支持多个

        """
        self.filters = filters

