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


class ResourceCreateReq(object):

    def __init__(self, resourceName=None, originalName=None, parentCode=None, resourceType=None, relativeEngine=None, uploadMode=None, env=None, managers=None):
        """
        :param resourceName: (Optional) 资源名称（支持中文、字母、数字、下划线，不超过50个字符）
        :param originalName: (Optional) 原始资源名称（上传的原始文件在本地客户端的文件名称）
        :param parentCode: (Optional) 父资源code（目录的根目录的父资源code为ROOT）
        :param resourceType: (Optional) 资源类型（DIRECTORY：目录；JAR：java的jar文件；FILE：其他普通文件；ARCHIVE：其他压缩文件/归档文件）
        :param relativeEngine: (Optional) 关联引擎（默认为JCW）
        :param uploadMode: (Optional) 文件上传方式（默认为本地上传）
        :param env: (Optional) 环境信息（prod：生产环境；dev：开发环境），简单模式默认为prod
        :param managers: (Optional) 负责人
        """

        self.resourceName = resourceName
        self.originalName = originalName
        self.parentCode = parentCode
        self.resourceType = resourceType
        self.relativeEngine = relativeEngine
        self.uploadMode = uploadMode
        self.env = env
        self.managers = managers
