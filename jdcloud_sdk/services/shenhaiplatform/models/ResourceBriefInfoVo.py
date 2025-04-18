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


class ResourceBriefInfoVo(object):

    def __init__(self, resourceCode=None, resourceName=None, resourceType=None, relativePath=None, mountPath=None):
        """
        :param resourceCode: (Optional) 资源code
        :param resourceName: (Optional) 资源名称
        :param resourceType: (Optional) 资源类型
        :param relativePath: (Optional) 资源文件相对路径
        :param mountPath: (Optional) 资源文件挂载路径
        """

        self.resourceCode = resourceCode
        self.resourceName = resourceName
        self.resourceType = resourceType
        self.relativePath = relativePath
        self.mountPath = mountPath
