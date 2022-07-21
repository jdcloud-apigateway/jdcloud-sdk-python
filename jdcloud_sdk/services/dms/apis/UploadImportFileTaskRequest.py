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


class UploadImportFileTaskRequest(JDCloudRequest):
    """
    上传文件
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UploadImportFileTaskRequest, self).__init__(
            '/regions/{regionId}/importFileTask:upload', 'POST', header, version)
        self.parameters = parameters


class UploadImportFileTaskParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        """

        self.regionId = regionId
        self.taskId = None
        self.chunkNumber = None
        self.identifier = None
        self.file = None

    def setTaskId(self, taskId):
        """
        :param taskId: (Optional) 上传文件任务id
        """
        self.taskId = taskId

    def setChunkNumber(self, chunkNumber):
        """
        :param chunkNumber: (Optional) 上传文件分片号
        """
        self.chunkNumber = chunkNumber

    def setIdentifier(self, identifier):
        """
        :param identifier: (Optional) 分片文件MD5
        """
        self.identifier = identifier

    def setFile(self, file):
        """
        :param file: (Optional) 分片文件
        """
        self.file = file
