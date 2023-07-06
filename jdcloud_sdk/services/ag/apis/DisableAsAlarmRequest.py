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


class DisableAsAlarmRequest(JDCloudRequest):
    """
    禁用告警任务
- 所有参数取值为字符串类型的都严格区分大小写
- 伸缩功能开启或者关闭的情况下，都支持调用此接口

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DisableAsAlarmRequest, self).__init__(
            '/regions/{regionId}/asAlarms/{asAlarmId}:disable', 'POST', header, version)
        self.parameters = parameters


class DisableAsAlarmParameters(object):

    def __init__(self,regionId, asAlarmId):
        """
        :param regionId: 地域ID
        :param asAlarmId: 告警任务ID
        """

        self.regionId = regionId
        self.asAlarmId = asAlarmId

