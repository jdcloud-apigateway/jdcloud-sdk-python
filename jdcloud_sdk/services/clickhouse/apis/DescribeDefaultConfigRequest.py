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


class DescribeDefaultConfigRequest(JDCloudRequest):
    """
    查询 Clickhouse 推荐规格
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeDefaultConfigRequest, self).__init__(
            '/regions/{regionId}/instances:describeDefaultConfig', 'GET', header, version)
        self.parameters = parameters


class DescribeDefaultConfigParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域代码
        """

        self.regionId = regionId
        self.chNodeClass = None
        self.shardNum = None
        self.replicaNum = None

    def setChNodeClass(self, chNodeClass):
        """
        :param chNodeClass: (Optional) 计算节点规格
        """
        self.chNodeClass = chNodeClass

    def setShardNum(self, shardNum):
        """
        :param shardNum: (Optional) 分片数
        """
        self.shardNum = shardNum

    def setReplicaNum(self, replicaNum):
        """
        :param replicaNum: (Optional) 副本数
        """
        self.replicaNum = replicaNum
