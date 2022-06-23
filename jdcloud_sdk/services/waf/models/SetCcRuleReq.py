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


class SetCcRuleReq(object):

    def __init__(self, wafInstanceId, domain, ruleName, uri, detectPeriod, singleIpLimit, blockType, blockTime, matchType=None, redirection=None, dimension=None, dmvalue=None):
        """
        :param wafInstanceId:  WAF实例id
        :param domain:  域名
        :param ruleName:  规则名称
        :param uri:  uri以/开头
        :param matchType: (Optional) 精确匹配0  前缀匹配1 包含匹配2 后缀匹配5
        :param detectPeriod:  检测周期，单位是秒，[30~600]
        :param singleIpLimit:  ip访问次数，[1~9999999]
        :param blockType:  阻断类型 1:302跳转到指定页面 2:验证码 3:拦截返回自定义页面 4:js跳转 5:观察 6:重定向
        :param blockTime:  block 持续时间，单位为分钟 [1~24*60]
        :param redirection: (Optional) blockType 为3 时，为自定义页面名称，缺省为default
        :param dimension: (Optional) cc 统计维度，ip或cookie
        :param dmvalue: (Optional) cookiename, 只有当 dimension 为 cookie 时才有效
        """

        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.ruleName = ruleName
        self.uri = uri
        self.matchType = matchType
        self.detectPeriod = detectPeriod
        self.singleIpLimit = singleIpLimit
        self.blockType = blockType
        self.blockTime = blockTime
        self.redirection = redirection
        self.dimension = dimension
        self.dmvalue = dmvalue
