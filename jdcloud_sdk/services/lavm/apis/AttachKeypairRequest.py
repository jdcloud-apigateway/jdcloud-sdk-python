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


class AttachKeypairRequest(JDCloudRequest):
    """
    
为云主机实例绑定密钥。

详细操作说明请参考帮助文档：[绑定密钥](https://docs.jdcloud.com/cn/virtual-machines/bind-keypair)

## 接口说明
- 只支持为 linux 云主机实例绑定密钥。
- 每台云主机实例只支持绑定一个密钥。如果云主机绑定的密钥被删除了，那么该云主机还可以再次绑定密钥。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AttachKeypairRequest, self).__init__(
            '/regions/{regionId}/keypairs/{keyName}:attach', 'POST', header, version)
        self.parameters = parameters


class AttachKeypairParameters(object):

    def __init__(self,regionId, keyName, instanceIds, passwordAuth):
        """
        :param regionId: 地域ID。
        :param keyName: 密钥名称。
        :param instanceIds: 要绑定的云主机Id列表。
        :param passwordAuth: 绑定密钥后，根据此参数决定是否允许使用密码登录。可选范围：
`yes`：允许SSH密码登录。
`no`：禁止SSH密码登录。

        """

        self.regionId = regionId
        self.keyName = keyName
        self.instanceIds = instanceIds
        self.passwordAuth = passwordAuth

