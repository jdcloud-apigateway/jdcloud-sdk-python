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


class DisassociateElasticIpsRequest(JDCloudRequest):
    """
    解绑NAT网关上的公网IP接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DisassociateElasticIpsRequest, self).__init__(
            '/regions/{regionId}/natGateways/{natGatewayId}:disassociateElasticIps', 'POST', header, version)
        self.parameters = parameters


class DisassociateElasticIpsParameters(object):

    def __init__(self,regionId, natGatewayId, elasticIpIds, ):
        """
        :param regionId: Region ID
        :param natGatewayId: natGateway ID
        :param elasticIpIds: 公网IP ID，当为弹性公网IP时，为elasticIpId。
        """

        self.regionId = regionId
        self.natGatewayId = natGatewayId
        self.elasticIpIds = elasticIpIds
        self.deleteElasticIp = None

    def setDeleteElasticIp(self, deleteElasticIp):
        """
        :param deleteElasticIp: (Optional) 解绑后是否删除公网IP，取值范围：true、false,默认为false.true表示解绑公网IP时删除该公网IP;false表示解绑公网IP时不删除公网IP
        """
        self.deleteElasticIp = deleteElasticIp

