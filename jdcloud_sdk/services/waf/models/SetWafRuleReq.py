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


class SetWafRuleReq(object):

    def __init__(self, id, wafInstanceId, domain, ruleName, matchAction, redirection, conditions, ):
        """
        :param id:  规则id,新增时传0
        :param wafInstanceId:  WAF实例id
        :param domain:  域名
        :param ruleName:  规则名称
        :param matchAction:  匹配动作, 拦截:forbidden,redirect 人机识别:verify@jscookie,verify@captcha,verify@rdtcookie 观察:notice
        :param redirection:  跳转地址，matchAction为redirect时必须为当前实例下的域名的url，forbidden时为自定义页面名称
        :param conditions:  条件集
        """

        self.id = id
        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.ruleName = ruleName
        self.matchAction = matchAction
        self.redirection = redirection
        self.conditions = conditions
