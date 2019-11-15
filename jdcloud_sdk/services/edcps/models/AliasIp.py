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


class AliasIp(object):

    def __init__(self, instanceId=None, region=None, az=None, subnetId=None, secondaryCidrId=None, aliasIpId=None, cidr=None):
        """
        :param instanceId: (Optional) 实例ID
        :param region: (Optional) 地域
        :param az: (Optional) 可用区
        :param subnetId: (Optional) 子网ID
        :param secondaryCidrId: (Optional) 次要cidr ID
        :param aliasIpId: (Optional) 别名IP ID
        :param cidr: (Optional) cidr段
        """

        self.instanceId = instanceId
        self.region = region
        self.az = az
        self.subnetId = subnetId
        self.secondaryCidrId = secondaryCidrId
        self.aliasIpId = aliasIpId
        self.cidr = cidr