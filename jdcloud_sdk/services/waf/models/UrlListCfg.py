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


class UrlListCfg(object):

    def __init__(self, id=None, updateTime=None, disable=None, matchOp=None, val=None, atCfg=None, skipRuleId=None):
        """
        :param id: (Optional) 序号id
        :param updateTime: (Optional) 规则更新时间，秒级时间戳, 0 表示历史数据无记录
        :param disable: (Optional) 0-使用中 1-禁用
        :param matchOp: (Optional) 0-5 7-8 完全匹配0  前缀匹配1 包含2 正则3 大于4 后缀5 不等于7 不包含8
        :param val: (Optional) val
        :param atCfg: (Optional) action配置
        :param skipRuleId: (Optional) 白名单不检查指定Web防护规则id, 多个逗号分隔
        """

        self.id = id
        self.updateTime = updateTime
        self.disable = disable
        self.matchOp = matchOp
        self.val = val
        self.atCfg = atCfg
        self.skipRuleId = skipRuleId