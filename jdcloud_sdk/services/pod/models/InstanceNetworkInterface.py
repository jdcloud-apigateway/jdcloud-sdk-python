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


class InstanceNetworkInterface(object):

    def __init__(self, networkInterfaceId=None, macAddress=None, vpcId=None, subnetId=None, description=None, securityGroups=None, sanityCheck=None, primaryIp=None, secondaryIps=None, ipv6Addresses=None, ipv6AddressesInfo=None):
        """
        :param networkInterfaceId: (Optional) 弹性网卡ID
        :param macAddress: (Optional) 以太网地址
        :param vpcId: (Optional) 虚拟网络ID
        :param subnetId: (Optional) 子网ID
        :param description: (Optional) 描述
        :param securityGroups: (Optional) 安全组列表
        :param sanityCheck: (Optional) 源和目标IP地址校验，取值为0或者1
        :param primaryIp: (Optional) 网卡主IP
        :param secondaryIps: (Optional) 
        :param ipv6Addresses: (Optional) 网卡IPv6地址
        :param ipv6AddressesInfo: (Optional) ipv6地址信息
        """

        self.networkInterfaceId = networkInterfaceId
        self.macAddress = macAddress
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.description = description
        self.securityGroups = securityGroups
        self.sanityCheck = sanityCheck
        self.primaryIp = primaryIp
        self.secondaryIps = secondaryIps
        self.ipv6Addresses = ipv6Addresses
        self.ipv6AddressesInfo = ipv6AddressesInfo
