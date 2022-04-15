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


class Ipv6Info(object):

    def __init__(self, vpcId=None, subnetId=None, instanceType=None, ipv6Address=None, createdTime=None):
        """
        :param vpcId: (Optional) 绑定资源所在私有网络的id
        :param subnetId: (Optional) 绑定资源所在子网的id
        :param instanceType: (Optional) 绑定资源的类型
        :param ipv6Address: (Optional) 绑定资源所拥有的ipv6的地址
        :param createdTime: (Optional) ip绑定资源创建时间
        """

        self.vpcId = vpcId
        self.subnetId = subnetId
        self.instanceType = instanceType
        self.ipv6Address = ipv6Address
        self.createdTime = createdTime
