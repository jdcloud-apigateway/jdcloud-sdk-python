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


class SetBotUsrRuleReq(object):

    def __init__(self, domain, ruleName, detectThrsd, detectPeriod, matchItems, action, id=None, ruleType=None, status=None, ststhrst=None, ststhrstRatio=None, statusDisable=None, dateDisable=None, unit=None, blockTime=None):
        """
        :param id: (Optional) 规则id，新增时为0或不传
        :param domain:  域名
        :param ruleName:  规则名
        :param detectThrsd:  次数阈值，[1-20000]
        :param detectPeriod:  检测时长，秒，[1-20000]
        :param matchItems:  匹配条件集,总长度不能超过4096
        :param action:  动作配置，默认为告警,仅支持1和4和5三种动作
        :param ruleType: (Optional) 规则类型，general-通用规则，advanced-高级规则，evaluate-智能规则 缺省为general
        :param status: (Optional) 响应状态码
        :param ststhrst: (Optional) 状态码数量阀值
        :param ststhrstRatio: (Optional) 状态码比例阀值
        :param statusDisable: (Optional) 响应码功能是否启用
        :param dateDisable: (Optional) 规则生效时间是否启用
        :param unit: (Optional) 统计维度
        :param blockTime: (Optional) 持续时间, 单位分钟，范围[1-24*60]
        """

        self.id = id
        self.domain = domain
        self.ruleName = ruleName
        self.detectThrsd = detectThrsd
        self.detectPeriod = detectPeriod
        self.matchItems = matchItems
        self.action = action
        self.ruleType = ruleType
        self.status = status
        self.ststhrst = ststhrst
        self.ststhrstRatio = ststhrstRatio
        self.statusDisable = statusDisable
        self.dateDisable = dateDisable
        self.unit = unit
        self.blockTime = blockTime
