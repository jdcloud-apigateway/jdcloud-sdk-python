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


class UpdateRuleRequest(JDCloudRequest):
    """
    更新规则。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateRuleRequest, self).__init__(
            '/zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id}', 'PATCH', header, version)
        self.parameters = parameters


class UpdateRuleParameters(object):

    def __init__(self,zone_id, ruleset_id, rule_id, ):
        """
        :param zone_id: 
        :param ruleset_id: 
        :param rule_id: 
        """

        self.zone_id = zone_id
        self.ruleset_id = ruleset_id
        self.rule_id = rule_id
        self.enabled = None
        self.description = None
        self.expression = None
        self.action = None
        self.action_parameters = None
        self.ratelimit = None
        self.logging = None
        self.position = None
        self.id = None
        self.version = None
        self.last_updated = None
        self.ref = None

    def setEnabled(self, enabled):
        """
        :param enabled: (Optional) 是否开启规则，有效值true/false。
        """
        self.enabled = enabled

    def setDescription(self, description):
        """
        :param description: (Optional) 规则的描述。
        """
        self.description = description

    def setExpression(self, expression):
        """
        :param expression: (Optional) 表达式。
        """
        self.expression = expression

    def setAction(self, action):
        """
        :param action: (Optional) 当表达式匹配时，采取的措施。有效值block（阻止）/challenge（交互式质询）/js_challenge（JS质询）/managed_challenge（托管质询）/log（记录）/rewrite/skip（跳过）。
        """
        self.action = action

    def setAction_parameters(self, action_parameters):
        """
        :param action_parameters: (Optional) 
        """
        self.action_parameters = action_parameters

    def setRatelimit(self, ratelimit):
        """
        :param ratelimit: (Optional) 
        """
        self.ratelimit = ratelimit

    def setLogging(self, logging):
        """
        :param logging: (Optional) 
        """
        self.logging = logging

    def setPosition(self, position):
        """
        :param position: (Optional) 
        """
        self.position = position

    def setId(self, id):
        """
        :param id: (Optional) 规则标识。
        """
        self.id = id

    def setVersion(self, version):
        """
        :param version: (Optional) 规则版本。
        """
        self.version = version

    def setLast_updated(self, last_updated):
        """
        :param last_updated: (Optional) 最近更新时间。
        """
        self.last_updated = last_updated

    def setRef(self, ref):
        """
        :param ref: (Optional) 规则引用（默认是规则标识）。
        """
        self.ref = ref
