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


class SetHeaderReq(object):

    def __init__(self, wafInstanceId, domain, headers, iswhite=None, skipRuleId=None):
        """
        :param wafInstanceId:  
        :param domain:  域名
        :param iswhite: (Optional) 0表示黑名单，1表示白名单
        :param skipRuleId: (Optional) 白名单不检查指定Web防护规则id, 多个逗号分隔
        :param headers:  header配置
        """

        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.iswhite = iswhite
        self.skipRuleId = skipRuleId
        self.headers = headers
