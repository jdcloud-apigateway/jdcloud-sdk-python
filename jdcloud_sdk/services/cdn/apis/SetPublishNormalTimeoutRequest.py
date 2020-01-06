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


class SetPublishNormalTimeoutRequest(JDCloudRequest):
    """
    设置推流中断超时时间
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetPublishNormalTimeoutRequest, self).__init__(
            '/liveDomain/{domain}/publishNormalTimeout', 'POST', header, version)
        self.parameters = parameters


class SetPublishNormalTimeoutParameters(object):

    def __init__(self, domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.timeout = None

    def setTimeout(self, timeout):
        """
        :param timeout: (Optional) 超时时间应介于0s到3600s之间
        """
        self.timeout = timeout
