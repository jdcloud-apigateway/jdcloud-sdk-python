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


class ModifyInstanceAttributeRequest(JDCloudRequest):
    """
    修改云主机部分信息，包括名称、描述。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyInstanceAttributeRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:modifyInstanceAttribute', 'POST', header, version)
        self.parameters = parameters


class ModifyInstanceAttributeParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域ID
        :param instanceId: 云主机ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.name = None
        self.description = None
        self.hostname = None
        self.metadata = None
        self.userdata = None

    def setName(self, name):
        """
        :param name: (Optional) 名称，不为空且只允许中文、数字、大小写字母、英文下划线（_）、中划线（-）及点（.），不能以（.）作为首尾，长度为2~128个字符
        """
        self.name = name

    def setDescription(self, description):
        """
        :param description: (Optional) 描述，<a href="http://docs.jdcloud.com/virtual-machines/api/general_parameters">参考公共参数规范</a>。
        """
        self.description = description

    def setHostname(self, hostname):
        """
        :param hostname: (Optional) 云主机hostname，若不指定hostname，则hostname默认使用云主机名称name，但是会以RFC 952和RFC 1123命名规范做一定转义
Windows Server系统：长度为2-15个字符，允许大小写字母、数字或连字符（-）。不能以连字符（-）开头或结尾，不能连续使用连字符（-），也不能全部使用数字。不支持点号（.）。
Linux系统：长度为2-64个字符，允许支持多个点号，点之间为一段，每段允许使用大小写字母、数字或连字符（-），但不能连续使用点号（.）或连字符（-），不能以点号（.）或连字符（-）开头或结尾。
hostname修改后，重启云主机hostname生效

        """
        self.hostname = hostname

    def setMetadata(self, metadata):
        """
        :param metadata: (Optional) 用户自定义元数据信息，key-value 键值对总数量不超过40，其中更新和新增键值对总数量不超过20对，删除的键值对总数量不超过20对。不区分大小写。
如key已有认为是更新value；如key不存在认为是新增键值对；如key后面有连字符(-)，比如key-，则删除此key。

        """
        self.metadata = metadata

    def setUserdata(self, userdata):
        """
        :param userdata: (Optional) 元数据信息，目前只支持传入一个key为"launch-script"，表示首次启动脚本。value为base64格式。
launch-script：linux系统支持bash和python，编码前须分别以 #!/bin/bash 和 #!/usr/bin/env python 作为内容首行;
launch-script：windows系统支持bat和powershell，编码前须分别以 <cmd></cmd> 和 <powershell></powershell> 作为内容首、尾行。

        """
        self.userdata = userdata

