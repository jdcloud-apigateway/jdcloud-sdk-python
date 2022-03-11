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


class UserNumInfo(object):

    def __init__(self, appId=None, appName=None, userRoomId=None, number=None, duration=None, createTime=None):
        """
        :param appId: (Optional) 应用ID
        :param appName: (Optional) 应用名称
        :param userRoomId: (Optional) 业务接入方定义的且在JRTC系统内注册过的房间号
        :param number: (Optional) 房间在线人数
        :param duration: (Optional) 持续时长-minute
        :param createTime: (Optional) 创建时间UTC
        """

        self.appId = appId
        self.appName = appName
        self.userRoomId = userRoomId
        self.number = number
        self.duration = duration
        self.createTime = createTime