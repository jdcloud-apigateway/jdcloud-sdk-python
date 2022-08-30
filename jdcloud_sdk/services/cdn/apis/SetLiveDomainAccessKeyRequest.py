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


class SetLiveDomainAccessKeyRequest(JDCloudRequest):
    """
    设置URL鉴权
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetLiveDomainAccessKeyRequest, self).__init__(
            '/liveDomain/{domain}/accesskeyConfig', 'POST', header, version)
        self.parameters = parameters


class SetLiveDomainAccessKeyParameters(object):

    def __init__(self,domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.accesskeyType = None
        self.accesskeyKey = None
        self.authLifeTime = None

    def setAccesskeyType(self, accesskeyType):
        """
        :param accesskeyType: (Optional) url鉴权开启1关闭0
        """
        self.accesskeyType = accesskeyType

    def setAccesskeyKey(self, accesskeyKey):
        """
        :param accesskeyKey: (Optional) url鉴权开启时必传
        """
        self.accesskeyKey = accesskeyKey

    def setAuthLifeTime(self, authLifeTime):
        """
        :param authLifeTime: (Optional) 开启时默认值为300s,关闭时为0
        """
        self.authLifeTime = authLifeTime

