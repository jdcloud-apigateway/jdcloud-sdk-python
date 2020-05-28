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


class FunctionCallRecordVo(object):

    def __init__(self, code=None, deviceId=None, displayName=None, funcKey=None, inParams=None, message=None, messageId=None, outParams=None, reqTimestamp=None, respTimestamp=None):
        """
        :param code: (Optional) 响应码
        :param deviceId: (Optional) 设备标识id
        :param displayName: (Optional) 方法名称
        :param funcKey: (Optional) 方法key
        :param inParams: (Optional) 方法调用参数 json格式
        :param message: (Optional) 响应消息
        :param messageId: (Optional) 消息id
        :param outParams: (Optional) 方法调用响应 json格式
        :param reqTimestamp: (Optional) 请求时间
        :param respTimestamp: (Optional) 响应时间
        """

        self.code = code
        self.deviceId = deviceId
        self.displayName = displayName
        self.funcKey = funcKey
        self.inParams = inParams
        self.message = message
        self.messageId = messageId
        self.outParams = outParams
        self.reqTimestamp = reqTimestamp
        self.respTimestamp = respTimestamp
