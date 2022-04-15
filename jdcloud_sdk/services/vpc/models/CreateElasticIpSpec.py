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


class CreateElasticIpSpec(object):

    def __init__(self, maxCount, elasticIpSpec, elasticIpAddress=None, userTags=None, ipType=None, resourceGroupId=None, dryRun=None):
        """
        :param maxCount:  购买弹性ip数量；取值范围：[1,100]
        :param elasticIpAddress: (Optional) 指定弹性ip地址进行创建，当申请创建多个弹性ip时，必须为空
        :param elasticIpSpec:  弹性ip规格
        :param userTags: (Optional) 用户标签
        :param ipType: (Optional) 弹性ip类型，取值：standard(标准公网IP)，edge(边缘公网IP)，默认为standard
        :param resourceGroupId: (Optional) 资源所属资源组ID
        :param dryRun: (Optional) 预检标识，默认false，dryRun为true时只作检查，不做变更
        """

        self.maxCount = maxCount
        self.elasticIpAddress = elasticIpAddress
        self.elasticIpSpec = elasticIpSpec
        self.userTags = userTags
        self.ipType = ipType
        self.resourceGroupId = resourceGroupId
        self.dryRun = dryRun
