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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class DescribeConsumerAllTopicsRequest(JDCloudRequest):
    """
    消费者订阅过的topic列表，用于重置消费位点
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeConsumerAllTopicsRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/consumerGroups/{consumerGroup}/allTopics', 'GET', header, version)
        self.parameters = parameters


class DescribeConsumerAllTopicsParameters(object):

    def __init__(self,regionId, instanceId, consumerGroup, ):
        """
        :param regionId: 区域ID
        :param instanceId: 实例id
        :param consumerGroup: 消费组名称
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.consumerGroup = consumerGroup
        self.topicFilter = None

    def setTopicFilter(self, topicFilter):
        """
        :param topicFilter: (Optional) topic的过滤条件
        """
        self.topicFilter = topicFilter

