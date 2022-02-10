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


class SetExtraCacheTimeRequest(JDCloudRequest):
    """
    设置异常码缓存时间
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetExtraCacheTimeRequest, self).__init__(
            '/domain/{domain}/extraCacheTime:set', 'POST', header, version)
        self.parameters = parameters


class SetExtraCacheTimeParameters(object):

    def __init__(self, domain,):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.httpCode = None
        self.cacheTime = None

    def setHttpCode(self, httpCode):
        """
        :param httpCode: (Optional) 异常状态码 ["4xx","400", "401",  "402", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417",  "5xx","500", "501", "502", "503", "504", "505"]中的其中一个
        """
        self.httpCode = httpCode

    def setCacheTime(self, cacheTime):
        """
        :param cacheTime: (Optional) 缓存时间(单位:秒)
        """
        self.cacheTime = cacheTime

