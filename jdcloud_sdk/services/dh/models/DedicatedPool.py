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


class DedicatedPool(object):

    def __init__(self, dedicatedPoolId=None, name=None, dedicatedHostType=None, description=None, az=None, capacity=None, supportedInstanceType=None, dedicatedHosts=None, instanceIds=None, createTime=None):
        """
        :param dedicatedPoolId: (Optional) 专有宿主机池ID
        :param name: (Optional) 专有宿主机池名称
        :param dedicatedHostType: (Optional) 专有宿主机池支持的机型
        :param description: (Optional) 专有宿主机池描述
        :param az: (Optional) 有宿主机池选定的AZ列表
        :param capacity: (Optional) 专有宿主机池资源使用信息
        :param supportedInstanceType: (Optional) 专有宿主机支持的云主机实例规格
        :param dedicatedHosts: (Optional) 专有宿主机池下的专有宿主机简要信息
        :param instanceIds: (Optional) 专有宿主机池中的云主机ID列表
        :param createTime: (Optional) 创建时间
        """

        self.dedicatedPoolId = dedicatedPoolId
        self.name = name
        self.dedicatedHostType = dedicatedHostType
        self.description = description
        self.az = az
        self.capacity = capacity
        self.supportedInstanceType = supportedInstanceType
        self.dedicatedHosts = dedicatedHosts
        self.instanceIds = instanceIds
        self.createTime = createTime
