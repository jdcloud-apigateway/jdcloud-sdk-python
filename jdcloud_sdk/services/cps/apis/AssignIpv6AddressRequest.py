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


class AssignIpv6AddressRequest(JDCloudRequest):
    """
    申请IPv6地址
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AssignIpv6AddressRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:assignIpv6Address', 'POST', header, version)
        self.parameters = parameters


class AssignIpv6AddressParameters(object):

    def __init__(self, regionId, instanceId, subnetId):
        """
        :param regionId: 地域ID，可调用接口（describeRegiones）获取云物理服务器支持的地域
        :param instanceId: 云物理服务器ID
        :param subnetId: 子网ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.clientToken = None
        self.ipv6Address = None
        self.subnetId = subnetId

    def setClientToken(self, clientToken):
        """
        :param clientToken: (Optional) 由客户端生成，用于保证请求的幂等性，长度不能超过36个字符；<br/>
如果多个请求使用了相同的clientToken，只会执行第一个请求，之后的请求直接返回第一个请求的结果<br/>

        """
        self.clientToken = clientToken

    def setIpv6Address(self, ipv6Address):
        """
        :param ipv6Address: (Optional) IPv6地址
        """
        self.ipv6Address = ipv6Address

