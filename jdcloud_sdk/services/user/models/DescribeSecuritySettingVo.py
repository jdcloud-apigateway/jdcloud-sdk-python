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


class DescribeSecuritySettingVo(object):

    def __init__(self, pin=None, loginName=None, jdPin=None, nickName=None, jdLogin=None, loginType=None, mfaStatus=None, sopStatus=None, sopType=None, ipProtect=None, userDevice=None, contactCheck=None, openBinds=None, phone=None, email=None):
        """
        :param pin: (Optional) 账号pin
        :param loginName: (Optional) 云账号
        :param jdPin: (Optional) 京东pin
        :param nickName: (Optional) 账号昵称
        :param jdLogin: (Optional) 京东登录
        :param loginType: (Optional) null
        :param mfaStatus: (Optional) 是否开启mfa
        :param sopStatus: (Optional) null
        :param sopType: (Optional) null
        :param ipProtect: (Optional) null
        :param userDevice: (Optional) null
        :param contactCheck: (Optional) 添加联系人是否校验0否1校验
        :param openBinds: (Optional) 三方账号
        :param phone: (Optional) 手机
        :param email: (Optional) 邮箱
        """

        self.pin = pin
        self.loginName = loginName
        self.jdPin = jdPin
        self.nickName = nickName
        self.jdLogin = jdLogin
        self.loginType = loginType
        self.mfaStatus = mfaStatus
        self.sopStatus = sopStatus
        self.sopType = sopType
        self.ipProtect = ipProtect
        self.userDevice = userDevice
        self.contactCheck = contactCheck
        self.openBinds = openBinds
        self.phone = phone
        self.email = email
