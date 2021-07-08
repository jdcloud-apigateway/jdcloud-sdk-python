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


class AddLiveStreamDomainTranslateRequest(JDCloudRequest):
    """
    添加域名翻译配置
- 添加域名级别的翻译模板配置
- 一个域名最多可绑定一个翻译模板
- 重新推流后生效

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddLiveStreamDomainTranslateRequest, self).__init__(
            '/translateDomains:config', 'POST', header, version)
        self.parameters = parameters


class AddLiveStreamDomainTranslateParameters(object):

    def __init__(self, publishDomain, template):
        """
        :param publishDomain: 直播的推流域名
        :param template: 翻译模版
- 取值范围: 系统标准翻译模板, 用户自定义翻译模板
- 系统标准翻译模板
  system-zh-en (中译英)
  system-en-zh (英译中)

        """

        self.publishDomain = publishDomain
        self.template = template

