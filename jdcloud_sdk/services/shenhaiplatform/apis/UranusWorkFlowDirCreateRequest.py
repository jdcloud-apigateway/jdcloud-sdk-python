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


class UranusWorkFlowDirCreateRequest(JDCloudRequest):
    """
    创建文件夹
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(UranusWorkFlowDirCreateRequest, self).__init__(
            '/regions/{regionId}/apps/{appName}/uranusWorkFlowDirCreate', 'POST', header, version)
        self.parameters = parameters


class UranusWorkFlowDirCreateParameters(object):

    def __init__(self,regionId, appName, flowCode, ):
        """
        :param regionId: 地域ID
        :param appName: 应用名称
        :param flowCode: 任务流Code
        """

        self.regionId = regionId
        self.appName = appName
        self.fileType = None
        self.isJarManagement = None
        self.fileCode = None
        self.parentCode = None
        self.fileName = None
        self.flowCode = flowCode
        self.relativePath = None
        self.isUpload = None

    def setFileType(self, fileType):
        """
        :param fileType: (Optional) 文件类型
        """
        self.fileType = fileType

    def setIsJarManagement(self, isJarManagement):
        """
        :param isJarManagement: (Optional) 是否spark-jar的管理模块,spark-jar操作hdfs通过字段区分
        """
        self.isJarManagement = isJarManagement

    def setFileCode(self, fileCode):
        """
        :param fileCode: (Optional) 文件Code
        """
        self.fileCode = fileCode

    def setParentCode(self, parentCode):
        """
        :param parentCode: (Optional) 父节点 Code
        """
        self.parentCode = parentCode

    def setFileName(self, fileName):
        """
        :param fileName: (Optional) 文件名称
        """
        self.fileName = fileName

    def setRelativePath(self, relativePath):
        """
        :param relativePath: (Optional) 文件夹上传的时候文件的相对路径属性
        """
        self.relativePath = relativePath

    def setIsUpload(self, isUpload):
        """
        :param isUpload: (Optional) 是否上传完成 0 上传取消 1 上传完成
        """
        self.isUpload = isUpload

