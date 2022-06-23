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


class CreateImportFileTaskRequest(JDCloudRequest):
    """
    创建导入文件任务
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateImportFileTaskRequest, self).__init__(
            '/regions/{regionId}/importFileTask:create', 'POST', header, version)
        self.parameters = parameters


class CreateImportFileTaskParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        """

        self.regionId = regionId
        self.filename = None
        self.totalSize = None
        self.chunkSize = None
        self.totalChunks = None

    def setFilename(self, filename):
        """
        :param filename: (Optional) 文件名称
        """
        self.filename = filename

    def setTotalSize(self, totalSize):
        """
        :param totalSize: (Optional) 文件总大小
        """
        self.totalSize = totalSize

    def setChunkSize(self, chunkSize):
        """
        :param chunkSize: (Optional) 文件分片大小
        """
        self.chunkSize = chunkSize

    def setTotalChunks(self, totalChunks):
        """
        :param totalChunks: (Optional) 文件分片数
        """
        self.totalChunks = totalChunks

