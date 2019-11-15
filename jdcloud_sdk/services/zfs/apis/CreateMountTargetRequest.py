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


class CreateMountTargetRequest(JDCloudRequest):
    """
    - 为一个文件系统创建一个挂载目标。通过这个挂载目标,你可以挂载将一个文件系统挂载到主机实例上。
- 创建一个挂载目标，为这个挂载目标分配一个Id

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateMountTargetRequest, self).__init__(
            '/regions/{regionId}/mountTargets', 'POST', header, version)
        self.parameters = parameters


class CreateMountTargetParameters(object):

    def __init__(self, regionId, fileSystemId, subnetId, vpcId, clientToken):
        """
        :param regionId: 地域ID
        :param fileSystemId: 创建挂载目标的文件系统
        :param subnetId: 子网id
        :param vpcId: vpcId
        :param clientToken: 幂等性参数(只支持数字、大小写字母，且不能超过64字符)
        """

        self.regionId = regionId
        self.fileSystemId = fileSystemId
        self.subnetId = subnetId
        self.vpcId = vpcId
        self.securityGroupId = None
        self.clientToken = clientToken

    def setSecurityGroupId(self, securityGroupId):
        """
        :param securityGroupId: (Optional) 安全组id
        """
        self.securityGroupId = securityGroupId

