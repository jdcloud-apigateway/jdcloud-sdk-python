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


class OperationProvider(object):

    def __init__(self, id=None, provider=None, networkOperator=None, ccProvider=None, ezIpType=None):
        """
        :param id: (Optional) 资源id
        :param provider: (Optional) 公网IP的线路
        :param networkOperator: (Optional) 公网IP的计费类型
        :param ccProvider: (Optional) 底层真实provider
        :param ezIpType: (Optional) 所属用户类型
        """

        self.id = id
        self.provider = provider
        self.networkOperator = networkOperator
        self.ccProvider = ccProvider
        self.ezIpType = ezIpType