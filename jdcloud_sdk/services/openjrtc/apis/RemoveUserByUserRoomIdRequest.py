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


class RemoveUserByUserRoomIdRequest(JDCloudRequest):
    """
    移除房间内人员

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(RemoveUserByUserRoomIdRequest, self).__init__(
            '/removeUserByUserRoomId/{appId}', 'POST', header, version)
        self.parameters = parameters


class RemoveUserByUserRoomIdParameters(object):

    def __init__(self,appId, ):
        """
        :param appId: 应用ID
        """

        self.appId = appId
        self.userRoomId = None
        self.userIds = None

    def setUserRoomId(self, userRoomId):
        """
        :param userRoomId: (Optional) 业务接入方定义的且在JRTC系统内注册过的房间号
        """
        self.userRoomId = userRoomId

    def setUserIds(self, userIds):
        """
        :param userIds: (Optional) 接入方定义的userId列表,最多支持20个userId
        """
        self.userIds = userIds

