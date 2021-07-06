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


class TacticsItem(object):

    def __init__(self, tacticsType=None, suspiciousRiskConfig=None, abandonRiskConfig=None):
        """
        :param tacticsType: (Optional) 策略类型：1 智能组合,2过载保护,3自有策略,4验证码策略
        :param suspiciousRiskConfig: (Optional) 可疑请求配置
        :param abandonRiskConfig: (Optional) 问题请求配置
        """

        self.tacticsType = tacticsType
        self.suspiciousRiskConfig = suspiciousRiskConfig
        self.abandonRiskConfig = abandonRiskConfig
