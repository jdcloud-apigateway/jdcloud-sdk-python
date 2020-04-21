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


class AssociateRouteTableRequest(JDCloudRequest):
    """
    路由表绑定子网接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AssociateRouteTableRequest, self).__init__(
            '/regions/{regionId}/routeTables/{routeTableId}:associateRouteTable', 'POST', header, version)
        self.parameters = parameters


class AssociateRouteTableParameters(object):

    def __init__(self, regionId, routeTableId, subnetIds):
        """
        :param regionId: Region ID
        :param routeTableId: RouteTable ID
        :param subnetIds: 路由表要绑定的子网ID列表, subnet已被其他路由表绑定时，自动解绑。路由表绑定的子网属性要相同，或者都是标准子网，或者都是相同边缘可用区的边缘子网。
        """

        self.regionId = regionId
        self.routeTableId = routeTableId
        self.subnetIds = subnetIds

