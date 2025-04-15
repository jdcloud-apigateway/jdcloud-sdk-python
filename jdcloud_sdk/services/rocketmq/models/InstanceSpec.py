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


class InstanceSpec(object):

    def __init__(self, vpcId, subnetId, instanceVersion, instanceName, azId, instanceClassSpec, extension=None, cpuArch=None, opsTags=None, userTags=None):
        """
        :param vpcId:  私有网络vpcId
        :param subnetId:  子网subnetId
        :param instanceVersion:  rocketmq版本，[5.1.3]
        :param instanceName:  rocketmq集群名称，不可为空，只支持大小写字母、数字、英文下划线或者中划线，以字母开头且不能超过32位
        :param azId:  可用区
        :param instanceClassSpec:  集群规格配置
        :param extension: (Optional) 扩展配置
        :param cpuArch: (Optional) 支持的cpu架构类型, 创建时选择，不选默认创建x86架构的实例
        :param opsTags: (Optional) 用于标识资源分类的Tag键值对
        :param userTags: (Optional) 用于标识资源分类的Tag键值对
        """

        self.vpcId = vpcId
        self.subnetId = subnetId
        self.instanceVersion = instanceVersion
        self.instanceName = instanceName
        self.azId = azId
        self.instanceClassSpec = instanceClassSpec
        self.extension = extension
        self.cpuArch = cpuArch
        self.opsTags = opsTags
        self.userTags = userTags
