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


class ServiceUserLink(object):

    def __init__(self, uuid=None, userPin=None, userName=None, userPhone=None, company=None, address=None, desc=None, createTime=None, userLevel=None, userMaster=None, status=None):
        """
        :param uuid: (Optional) 用户唯一标识
        :param userPin: (Optional) 用户Pin
        :param userName: (Optional) 用户名称
        :param userPhone: (Optional) 用户电话
        :param company: (Optional) 用户公司
        :param address: (Optional) 用户地址
        :param desc: (Optional) 用户描述
        :param createTime: (Optional) 注册时间
        :param userLevel: (Optional) 用户等级
        :param userMaster: (Optional) 管理者UserPin
        :param status: (Optional) 用户状态
        """

        self.uuid = uuid
        self.userPin = userPin
        self.userName = userName
        self.userPhone = userPhone
        self.company = company
        self.address = address
        self.desc = desc
        self.createTime = createTime
        self.userLevel = userLevel
        self.userMaster = userMaster
        self.status = status
