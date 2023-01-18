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


class ExecCreateRequest(JDCloudRequest):
    """
    创建 exec

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ExecCreateRequest, self).__init__(
            '/regions/{regionId}/pods/{podId}/containers/{containerName}:execCreate', 'POST', header, version)
        self.parameters = parameters


class ExecCreateParameters(object):

    def __init__(self,regionId, podId, containerName, command, ):
        """
        :param regionId: Region ID
        :param podId: Pod ID
        :param containerName: container name
        :param command: 执行的命令
        """

        self.regionId = regionId
        self.podId = podId
        self.containerName = containerName
        self.command = command
        self.tty = None

    def setTty(self, tty):
        """
        :param tty: (Optional) 执行命令是否分配tty。默认不分配
        """
        self.tty = tty

