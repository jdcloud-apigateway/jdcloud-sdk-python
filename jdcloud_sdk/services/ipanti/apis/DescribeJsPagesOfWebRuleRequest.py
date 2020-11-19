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


class DescribeJsPagesOfWebRuleRequest(JDCloudRequest):
    """
    查询网站类规则允许插入JS指纹的页面
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeJsPagesOfWebRuleRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/webRules/{webRuleId}/jsPages', 'GET', header, version)
        self.parameters = parameters


class DescribeJsPagesOfWebRuleParameters(object):

    def __init__(self, regionId, instanceId, webRuleId, ):
        """
        :param regionId: 区域 ID, 高防不区分区域, 传 cn-north-1 即可
        :param instanceId: 高防实例 Id
        :param webRuleId: 网站规则 Id
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.webRuleId = webRuleId
        self.pageNumber = None
        self.pageSize = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小, 默认为10, 取值范围[10, 100]
        """
        self.pageSize = pageSize

