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


class JtlasSearchTableLineageRequest(JDCloudRequest):
    """
    查询表血缘
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(JtlasSearchTableLineageRequest, self).__init__(
            '/regions/{regionId}/apps/{appName}/jtlasSearchTableLineage', 'POST', header, version)
        self.parameters = parameters


class JtlasSearchTableLineageParameters(object):

    def __init__(self,regionId, appName, direction, edgeType, nodeId, ):
        """
        :param regionId: 地域ID
        :param appName: 应用名称
        :param direction: 方向
        :param edgeType: 边类型
        :param nodeId: 
        """

        self.regionId = regionId
        self.appName = appName
        self.direction = direction
        self.edgeType = edgeType
        self.nodeId = nodeId
        self.depth = None

    def setDepth(self, depth):
        """
        :param depth: (Optional) 检索深度
        """
        self.depth = depth

