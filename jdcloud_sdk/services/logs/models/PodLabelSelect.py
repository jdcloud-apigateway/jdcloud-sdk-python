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


class PodLabelSelect(object):

    def __init__(self, operate=None, podInfo=None, tenant=None, podListStr=None, productName=None, allTenantDistributability=None):
        """
        :param operate: (Optional) 操作类型
        :param podInfo: (Optional) pod详情
        :param tenant: (Optional) 租户
        :param podListStr: (Optional) pod详情数组
        :param productName: (Optional) 产品名
        :param allTenantDistributability: (Optional) 是否所有租户可见
        """

        self.operate = operate
        self.podInfo = podInfo
        self.tenant = tenant
        self.podListStr = podListStr
        self.productName = productName
        self.allTenantDistributability = allTenantDistributability