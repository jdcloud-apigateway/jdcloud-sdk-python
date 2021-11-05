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


class ChangeWebApplicationFirewallWAFSettingRequest(JDCloudRequest):
    """
    WAF检查对您网站的HTTP请求。它检查GET和POST请求，并应用规则来帮助从合法的网站访问者中过滤出非法流量。星盾 WAF 检查网站地址或 URL 以检测任何不正常的东西。
如果星盾 WAF确定了可疑的用户行为。那么 WAF 将用一个页面 "挑战 "网络访客，要求他们成功提交验证码以继续其行动。
如果挑战失败，行动将被停止。这意味着 星盾 的 WAF 将在任何被识别为非法的流量到达您的源网络服务器之前将其阻止。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ChangeWebApplicationFirewallWAFSettingRequest, self).__init__(
            '/zones/{zone_identifier}/settings$$waf', 'PATCH', header, version)
        self.parameters = parameters


class ChangeWebApplicationFirewallWAFSettingParameters(object):

    def __init__(self, zone_identifier, ):
        """
        :param zone_identifier: 
        """

        self.zone_identifier = zone_identifier
        self.value = None

    def setValue(self, value):
        """
        :param value: (Optional) on - 开启；off - 关闭
        """
        self.value = value

