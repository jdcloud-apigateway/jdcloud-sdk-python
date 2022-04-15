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


class DisassociateElasticIpRequest(JDCloudRequest):
    """
    给网卡解绑弹性Ip接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DisassociateElasticIpRequest, self).__init__(
            '/regions/{regionId}/networkInterfaces/{networkInterfaceId}:disassociateElasticIp', 'POST', header, version)
        self.parameters = parameters


class DisassociateElasticIpParameters(object):

    def __init__(self, regionId,networkInterfaceId,):
        """
        :param regionId: Region ID
        :param networkInterfaceId: networkInterface ID
        """

        self.regionId = regionId
        self.networkInterfaceId = networkInterfaceId
        self.elasticIpId = None
        self.elasticIpAddress = None

    def setElasticIpId(self, elasticIpId):
        """
        :param elasticIpId: (Optional) 指定解绑的弹性Ip Id
        """
        self.elasticIpId = elasticIpId

    def setElasticIpAddress(self, elasticIpAddress):
        """
        :param elasticIpAddress: (Optional) 指定解绑的弹性Ip地址
        """
        self.elasticIpAddress = elasticIpAddress

