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


class ReturnPolicyQuery(object):

    def __init__(self, id=None, deptId=None, distributorType=None, returnType=None, returnPolicyId=None, returnPolicyName=None, itemId=None, itemName=None, returnRuleType=None, productId=None, productType=None, circleType=None, circleName=None, circleFlag=None, circleValue=None, condition=None, conditionRemark=None, returnRatio=None, status=None, createTime=None, createUser=None, updateTime=None, updateUser=None, yn=None, itemNameLike=None, pageIndex=None, pageSize=None, offset=None):
        """
        :param id: (Optional) ID
        :param deptId: (Optional) 部门ID
        :param distributorType: (Optional) 渠道商类型
        :param returnType: (Optional) 返还类型
        :param returnPolicyId: (Optional) 返还政策主ID
        :param returnPolicyName: (Optional) 返还政策主名称
        :param itemId: (Optional) 项目编码
        :param itemName: (Optional) 项目名称
        :param returnRuleType: (Optional) 返还依据类型
        :param productId: (Optional) 产品ID
        :param productType: (Optional) 产品类型（多个产品类型，分开）
        :param circleType: (Optional) 周期类型
        :param circleName: (Optional) 周期名称
        :param circleFlag: (Optional) 指定周期标识
        :param circleValue: (Optional) 周期值
        :param condition: (Optional) 条件
        :param conditionRemark: (Optional) 说明
        :param returnRatio: (Optional) 返还比例
        :param status: (Optional) 状态
        :param createTime: (Optional) 创建时间
        :param createUser: (Optional) 创建人
        :param updateTime: (Optional) 修改时间
        :param updateUser: (Optional) 修改人
        :param yn: (Optional) 是否删除0未删除,1已删除
        :param itemNameLike: (Optional) 项目名称
        :param pageIndex: (Optional) 当前页序号
        :param pageSize: (Optional) 每页结果数量
        :param offset: (Optional) 
        """

        self.id = id
        self.deptId = deptId
        self.distributorType = distributorType
        self.returnType = returnType
        self.returnPolicyId = returnPolicyId
        self.returnPolicyName = returnPolicyName
        self.itemId = itemId
        self.itemName = itemName
        self.returnRuleType = returnRuleType
        self.productId = productId
        self.productType = productType
        self.circleType = circleType
        self.circleName = circleName
        self.circleFlag = circleFlag
        self.circleValue = circleValue
        self.condition = condition
        self.conditionRemark = conditionRemark
        self.returnRatio = returnRatio
        self.status = status
        self.createTime = createTime
        self.createUser = createUser
        self.updateTime = updateTime
        self.updateUser = updateUser
        self.yn = yn
        self.itemNameLike = itemNameLike
        self.pageIndex = pageIndex
        self.pageSize = pageSize
        self.offset = offset
