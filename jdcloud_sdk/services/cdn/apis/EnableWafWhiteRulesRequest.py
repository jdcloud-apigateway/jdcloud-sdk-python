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


class EnableWafWhiteRulesRequest(JDCloudRequest):
    """
    启用WAF白名单
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(EnableWafWhiteRulesRequest, self).__init__(
            '/domain/{domain}/wafWhiteRule:enable', 'POST', header, version)
        self.parameters = parameters


class EnableWafWhiteRulesParameters(object):

    def __init__(self,domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.ids = None
        self.ruleType = None

    def setIds(self, ids):
        """
        :param ids: (Optional) 
        """
        self.ids = ids

    def setRuleType(self, ruleType):
        """
        :param ruleType: (Optional) 
        """
        self.ruleType = ruleType

