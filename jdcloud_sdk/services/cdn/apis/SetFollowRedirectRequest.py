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


class SetFollowRedirectRequest(JDCloudRequest):
    """
    设置回源302跳转
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetFollowRedirectRequest, self).__init__(
            '/domain/{domain}/followRedirect', 'POST', header, version)
        self.parameters = parameters


class SetFollowRedirectParameters(object):

    def __init__(self, domain,):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.status = None

    def setStatus(self, status):
        """
        :param status: (Optional) 开关取值[on,off]
        """
        self.status = status

