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
    绑定ssh密钥对。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AttachKeypairRequest, self).__init__(
            '/regions/{regionId}/keypairs/{keyName}:attach', 'POST', header, version)
        self.parameters = parameters


class AttachKeypairParameters(object):

    def __init__(self, regionId, keyName, instanceIds, passWordAuth):
        """
        :param regionId: 地域ID
        :param keyName: 密钥名称
        :param instanceIds: 虚机Id
        :param passWordAuth: 密码授权，绑定密钥后，根据此参数决定是否使用密码登录，"yes"为使用，"no"为不使用

        """

        self.regionId = regionId
        self.keyName = keyName
        self.instanceIds = instanceIds
        self.passWordAuth = passWordAuth
