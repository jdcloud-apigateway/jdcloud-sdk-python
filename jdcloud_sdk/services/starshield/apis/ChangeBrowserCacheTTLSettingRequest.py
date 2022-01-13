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


class ChangeBrowserCacheTTLSettingRequest(JDCloudRequest):
    """
    浏览器缓存TTL（以秒为单位）指定星盾缓存资源将在访问者的计算机上保留多长时间。星盾将遵守服务器指定的任何更长时间。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ChangeBrowserCacheTTLSettingRequest, self).__init__(
            '/zones/{zone_identifier}/settings$$browser_cache_ttl', 'PATCH', header, version)
        self.parameters = parameters


class ChangeBrowserCacheTTLSettingParameters(object):

    def __init__(self, zone_identifier, ):
        """
        :param zone_identifier: 
        """

        self.zone_identifier = zone_identifier
        self.value = None

    def setValue(self, value):
        """
        :param value: (Optional) 该设置的有效值
        """
        self.value = value
