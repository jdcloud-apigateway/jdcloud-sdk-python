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


class SetIpbanReq(object):

    def __init__(self, wafInstanceId, domain, ipbanMode, action, ):
        """
        :param wafInstanceId:  WAF实例id
        :param domain:  域名
        :param ipbanMode:  防护模式 1宽松模式，2正常模式，3严格模式
        :param action:  动作配置
        """

        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.ipbanMode = ipbanMode
        self.action = action
