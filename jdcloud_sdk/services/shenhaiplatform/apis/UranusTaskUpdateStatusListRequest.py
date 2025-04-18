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


class UranusTaskUpdateStatusListRequest(JDCloudRequest):
    """
    批量任务单节点-上下线更新
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(UranusTaskUpdateStatusListRequest, self).__init__(
            '/regions/{regionId}/apps/{appName}/uranusTaskUpdateStatusList', 'POST', header, version)
        self.parameters = parameters


class UranusTaskUpdateStatusListParameters(object):

    def __init__(self,regionId, appName, taskCodes, status):
        """
        :param regionId: 地域ID
        :param appName: 应用名称
        :param taskCodes: 任务节点集合
        :param status: 任务节点状态
        """

        self.regionId = regionId
        self.appName = appName
        self.taskCodes = taskCodes
        self.status = status

