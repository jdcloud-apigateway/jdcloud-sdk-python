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


class ModifyMirrorSessionSpec(object):

    def __init__(self, mirrorSessionName=None, description=None, mirrorResourceDestination=None, vni=None, priority=None, mirrorFilterId=None):
        """
        :param mirrorSessionName: (Optional) 镜像名称，只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符
        :param description: (Optional) 描述,允许输入UTF-8编码下的全部字符，不超过256字符
        :param mirrorResourceDestination: (Optional) 镜像目的
        :param vni: (Optional) VXLAN ID，1-16777215
        :param priority: (Optional) 镜像会话优先级，1-32768
        :param mirrorFilterId: (Optional) 
        """

        self.mirrorSessionName = mirrorSessionName
        self.description = description
        self.mirrorResourceDestination = mirrorResourceDestination
        self.vni = vni
        self.priority = priority
        self.mirrorFilterId = mirrorFilterId