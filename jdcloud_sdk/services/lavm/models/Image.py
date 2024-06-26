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


class Image(object):

    def __init__(self, imageType=None, description=None, imageName=None, imageId=None, platform=None, architecture=None, osType=None, createdTime=None, icon=None, imageState=None, systemDiskSize=None):
        """
        :param imageType: (Optional) 镜像类型
        :param description: (Optional) 描述信息
        :param imageName: (Optional) 镜像名称
        :param imageId: (Optional) 镜像ID
        :param platform: (Optional) 镜像的操作系统平台名称
        :param architecture: (Optional) 操作系统架构, 可选值：x86_64、arm64。

        :param osType: (Optional) 镜像的操作系统类型
        :param createdTime: (Optional) 镜像创建时间
        :param icon: (Optional) 镜像icon url
        :param imageState: (Optional) 镜像状态。参考 [镜像状态](https://docs.jdcloud.com/virtual-machines/api/image_status)。
        :param systemDiskSize: (Optional) 镜像系统盘大小。
        """

        self.imageType = imageType
        self.description = description
        self.imageName = imageName
        self.imageId = imageId
        self.platform = platform
        self.architecture = architecture
        self.osType = osType
        self.createdTime = createdTime
        self.icon = icon
        self.imageState = imageState
        self.systemDiskSize = systemDiskSize
