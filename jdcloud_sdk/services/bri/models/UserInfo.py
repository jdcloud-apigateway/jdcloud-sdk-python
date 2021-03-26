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


class UserInfo(object):

    def __init__(self, pin=None, updateTime=None, createTime=None, userType=None, balanceAmount=None, totalCallAmount=None, totalBuyAmount=None, resourceAmount=None, following=None):
        """
        :param pin: (Optional) 用户pin
        :param updateTime: (Optional) 更新时间, yyyy-mm-dd hh:mm:ss格式
        :param createTime: (Optional) 创建时间, yyyy-mm-dd hh:mm:ss格式
        :param userType: (Optional) 用户类型
        :param balanceAmount: (Optional) 剩余调用量
        :param totalCallAmount: (Optional) 累计调用量
        :param totalBuyAmount: (Optional) 总购买量
        :param resourceAmount: (Optional) 资源包数量
        :param following: (Optional) 跟踪描述
        """

        self.pin = pin
        self.updateTime = updateTime
        self.createTime = createTime
        self.userType = userType
        self.balanceAmount = balanceAmount
        self.totalCallAmount = totalCallAmount
        self.totalBuyAmount = totalBuyAmount
        self.resourceAmount = resourceAmount
        self.following = following
