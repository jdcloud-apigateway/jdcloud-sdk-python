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


class UranusUploaderReq(object):

    def __init__(self, flowCode, fileType=None, isJarManagement=None, fileCode=None, parentCode=None, fileName=None, relativePath=None, isUpload=None):
        """
        :param fileType: (Optional) 文件类型
        :param isJarManagement: (Optional) 是否spark-jar的管理模块,spark-jar操作hdfs通过字段区分
        :param fileCode: (Optional) 文件Code
        :param parentCode: (Optional) 父节点 Code
        :param fileName: (Optional) 文件名称
        :param flowCode:  任务流Code
        :param relativePath: (Optional) 文件夹上传的时候文件的相对路径属性
        :param isUpload: (Optional) 是否上传完成 0 上传取消 1 上传完成
        """

        self.fileType = fileType
        self.isJarManagement = isJarManagement
        self.fileCode = fileCode
        self.parentCode = parentCode
        self.fileName = fileName
        self.flowCode = flowCode
        self.relativePath = relativePath
        self.isUpload = isUpload
