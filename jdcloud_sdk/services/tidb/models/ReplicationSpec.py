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


class ReplicationSpec(object):

    def __init__(self, startTS=None, replicationObjects=None, targetType=None, targetIP=None, targetPort=None, targetComment=None, targetUser=None, targetPassword=None, kafkaTopic=None, kafkaVersion=None, kafkaProtocol=None):
        """
        :param startTS: (Optional) 复制的起始时间戳
        :param replicationObjects: (Optional) 要复制的对象列表
        :param targetType: (Optional) 目标实例类型
        :param targetIP: (Optional) 目标实例IP
        :param targetPort: (Optional) 目标实例端口
        :param targetComment: (Optional) 目标实例备注说明
        :param targetUser: (Optional) 目标类型为TiDB或MySQL时，连接目标实例的用户名
        :param targetPassword: (Optional) 目标类型为TiDB或MySQL时，连接目标实例的密码
        :param kafkaTopic: (Optional) Kafka的Topic
        :param kafkaVersion: (Optional) Kafka的版本
        :param kafkaProtocol: (Optional) 消息的格式
        """

        self.startTS = startTS
        self.replicationObjects = replicationObjects
        self.targetType = targetType
        self.targetIP = targetIP
        self.targetPort = targetPort
        self.targetComment = targetComment
        self.targetUser = targetUser
        self.targetPassword = targetPassword
        self.kafkaTopic = kafkaTopic
        self.kafkaVersion = kafkaVersion
        self.kafkaProtocol = kafkaProtocol
