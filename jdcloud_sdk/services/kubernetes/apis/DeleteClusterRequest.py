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


class DeleteClusterRequest(JDCloudRequest):
    """
    删除集群，以及集群的所有node节点，网络，云盘等所有资源。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteClusterRequest, self).__init__(
            '/regions/{regionId}/clusters/{clusterId}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteClusterParameters(object):

    def __init__(self,regionId, clusterId, ):
        """
        :param regionId: 地域 ID
        :param clusterId: 集群 ID
        """

        self.regionId = regionId
        self.clusterId = clusterId
        self.routeTableId = None

    def setRouteTableId(self, routeTableId):
        """
        :param routeTableId: (Optional) 替换路由表id
        """
        self.routeTableId = routeTableId

