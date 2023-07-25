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


class SetElasticIpStatusRequest(JDCloudRequest):
    """
    设置NAT网关已绑定的公网IP状态接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetElasticIpStatusRequest, self).__init__(
            '/regions/{regionId}/natGateways/{natGatewayId}:setElasticIpStatus', 'POST', header, version)
        self.parameters = parameters


class SetElasticIpStatusParameters(object):

    def __init__(self,regionId, natGatewayId, elasticIpIds, status):
        """
        :param regionId: Region ID
        :param natGatewayId: natGateway ID
        :param elasticIpIds: 公网IP列表
        :param status: 公网ip状态，取值范围：online、offline。online表示将NAT绑定的公网IP上线，上线后公网IP可正常转发流量;offline表示将NAT绑定的公网IP下线，下线后，公网IP将不再接受新建连接，已有连接将继续转发流量，从而实现公网IP平滑下线。已下线的公网IP不会自动从NAT网关解绑，如需解绑请执行解绑操作
        """

        self.regionId = regionId
        self.natGatewayId = natGatewayId
        self.elasticIpIds = elasticIpIds
        self.status = status

