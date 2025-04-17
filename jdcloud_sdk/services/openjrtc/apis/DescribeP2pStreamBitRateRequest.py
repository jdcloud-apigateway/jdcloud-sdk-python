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


class DescribeP2pStreamBitRateRequest(JDCloudRequest):
    """
    查询用户端到端推流码率

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeP2pStreamBitRateRequest, self).__init__(
            '/describeP2pStreamBitRate', 'GET', header, version)
        self.parameters = parameters


class DescribeP2pStreamBitRateParameters(object):

    def __init__(self,appId, userRoomId, userId, kind, type, joinTime, ):
        """
        :param appId: 应用ID
        :param userRoomId: 业务接入方定义的且在JRTC系统内注册过的用户房间号
        :param userId: 业务接入方定义的且在JRTC系统内注册过的用户id
        :param kind: audio/video
        :param type: producer 发布流 consumer 订阅流
        :param joinTime: 加入时间 UTC格式
        """

        self.appId = appId
        self.userRoomId = userRoomId
        self.userId = userId
        self.kind = kind
        self.type = type
        self.joinTime = joinTime
        self.leaveTime = None
        self.fromUserId = None
        self.period = None

    def setLeaveTime(self, leaveTime):
        """
        :param leaveTime: (Optional) 离开时间 UTC格式
        """
        self.leaveTime = leaveTime

    def setFromUserId(self, fromUserId):
        """
        :param fromUserId: (Optional) 业务接入方定义的且在JRTC系统内注册过的用户id type=consumer时选择发送端用户id切换码率
        """
        self.fromUserId = fromUserId

    def setPeriod(self, period):
        """
        :param period: (Optional) 粒度 支持 1m 1h 1d
        """
        self.period = period

