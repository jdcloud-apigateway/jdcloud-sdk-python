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


class VolumeMount(object):

    def __init__(self, category=None, autoDelete=None, mountPath=None, readOnly=None, cloudDisk=None, fsType=None):
        """
        :param category: (Optional) 环境变量名称
        :param autoDelete: (Optional) 自动删除，删除容器时自动删除此volume
        :param mountPath: (Optional) 容器内的挂载目录
        :param readOnly: (Optional) 只读，默认false；只针对data volume有效，root volume为false
        :param cloudDisk: (Optional) 云硬盘规格
        :param fsType: (Optional) 指定volume文件系统类型，目前支持[xfs, ext4]
        """

        self.category = category
        self.autoDelete = autoDelete
        self.mountPath = mountPath
        self.readOnly = readOnly
        self.cloudDisk = cloudDisk
        self.fsType = fsType
