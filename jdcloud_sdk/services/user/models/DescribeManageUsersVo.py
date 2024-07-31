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


class DescribeManageUsersVo(object):

    def __init__(self, accountDisable=None, activeDeviceType=None, costDay=None, jdPin=None, jdbu=None, networkZone=None, threshold=None, vipInfo=None, userTypeAndName=None, cloudUser=None, userInfo=None):
        """
        :param accountDisable: (Optional) 是否注销
        :param activeDeviceType: (Optional) 登录态认证类型
        :param costDay: (Optional) 计费状态
        :param jdPin: (Optional) 京东pin
        :param jdbu: (Optional) jdbu
        :param networkZone: (Optional) 网络专区
        :param threshold: (Optional) 门槛价格
        :param vipInfo: (Optional) vip标签
        :param userTypeAndName: (Optional) 用户分组和实名名称
        :param cloudUser: (Optional) 企业账号信息
        :param userInfo: (Optional) 用户信息
        """

        self.accountDisable = accountDisable
        self.activeDeviceType = activeDeviceType
        self.costDay = costDay
        self.jdPin = jdPin
        self.jdbu = jdbu
        self.networkZone = networkZone
        self.threshold = threshold
        self.vipInfo = vipInfo
        self.userTypeAndName = userTypeAndName
        self.cloudUser = cloudUser
        self.userInfo = userInfo