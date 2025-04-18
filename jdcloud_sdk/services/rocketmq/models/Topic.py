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


class Topic(object):

    def __init__(self, topic=None, topicType=None, description=None, createTime=None, queueNums=None):
        """
        :param topic: (Optional) topic名称
        :param topicType: (Optional) 消息类型
        :param description: (Optional) 描述
        :param createTime: (Optional) 创建时间
        :param queueNums: (Optional) 分区数
        """

        self.topic = topic
        self.topicType = topicType
        self.description = description
        self.createTime = createTime
        self.queueNums = queueNums
