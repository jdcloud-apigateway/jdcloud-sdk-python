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


class ModifyTaskRequest(JDCloudRequest):
    """
    修改任务状态
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(ModifyTaskRequest, self).__init__(
            '/regions/{regionId}/task/{taskId}', 'PATCH', header, version)
        self.parameters = parameters


class ModifyTaskParameters(object):

    def __init__(self, regionId,taskId,progress, success, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》]
        :param taskId: Task ID
        :param progress: 
        :param success: 
        """

        self.regionId = regionId
        self.taskId = taskId
        self.progress = progress
        self.startTime = None
        self.endTime = None
        self.success = success
        self.errorMessage = None

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 
        """
        self.endTime = endTime

    def setErrorMessage(self, errorMessage):
        """
        :param errorMessage: (Optional) 
        """
        self.errorMessage = errorMessage

