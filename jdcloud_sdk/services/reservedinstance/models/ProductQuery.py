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


class ProductQuery(object):

    def __init__(self, id=None, appCode=None, serviceCode=None, reservedInstanceType=None, typeName=None, status=None, createTime=None, updateTime=None, createErp=None):
        """
        :param id: (Optional) ID
        :param appCode: (Optional) 应用编码
        :param serviceCode: (Optional) 产品编码
        :param reservedInstanceType: (Optional) 预留实例类型
        :param typeName: (Optional) 预留实例券类型名称
        :param status: (Optional) 状态 : 1 有效 2 失效
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 修改时间
        :param createErp: (Optional) 创建人
        """

        self.id = id
        self.appCode = appCode
        self.serviceCode = serviceCode
        self.reservedInstanceType = reservedInstanceType
        self.typeName = typeName
        self.status = status
        self.createTime = createTime
        self.updateTime = updateTime
        self.createErp = createErp
