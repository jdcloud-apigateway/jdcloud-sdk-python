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


class SendRecord(object):

    def __init__(self, sendNumber=None, smsContent=None, contentLength=None, chargeCount=None, packageType=None, sendTime=None, sendStatus=None):
        """
        :param sendNumber: (Optional) 手机号码
        :param smsContent: (Optional) 短信内容
        :param contentLength: (Optional) 短信字数
        :param chargeCount: (Optional) 折成条数
        :param packageType: (Optional) 短信类型 短信类型，1 通道短信 2 官方短信
        :param sendTime: (Optional) 发送时间
        :param sendStatus: (Optional) 发送状态
        """

        self.sendNumber = sendNumber
        self.smsContent = smsContent
        self.contentLength = contentLength
        self.chargeCount = chargeCount
        self.packageType = packageType
        self.sendTime = sendTime
        self.sendStatus = sendStatus
