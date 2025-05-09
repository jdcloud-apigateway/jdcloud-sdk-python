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


class DlqMessage(object):

    def __init__(self, msgId=None, topic=None, tags=None, key=None, storeTime=None, bornTime=None, reconsumeTimes=None, originalMsgId=None):
        """
        :param msgId: (Optional) 客户端生成的消息id（消费失败的msgId，前端展示这个）
        :param topic: (Optional) topic名称（原来topic的名称）
        :param tags: (Optional) 消息tag
        :param key: (Optional) 消息key
        :param storeTime: (Optional) 消息的存储时间
        :param bornTime: (Optional) 消息的产生时间
        :param reconsumeTimes: (Optional) 总消费次数
        :param originalMsgId: (Optional) 原消息offsetId
        """

        self.msgId = msgId
        self.topic = topic
        self.tags = tags
        self.key = key
        self.storeTime = storeTime
        self.bornTime = bornTime
        self.reconsumeTimes = reconsumeTimes
        self.originalMsgId = originalMsgId
