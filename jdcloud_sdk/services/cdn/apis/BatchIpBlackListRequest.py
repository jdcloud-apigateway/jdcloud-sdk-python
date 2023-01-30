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


class BatchIpBlackListRequest(JDCloudRequest):
    """
    批量添加域名ip黑名单
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(BatchIpBlackListRequest, self).__init__(
            '/batchIpBlackList', 'POST', header, version)
        self.parameters = parameters


class BatchIpBlackListParameters(object):

    def __init__(self,):
        """
        """

        self.operateDomainRange = None
        self.domains = None
        self.ipList = None
        self.forbidTime = None
        self.action = None

    def setOperateDomainRange(self, operateDomainRange):
        """
        :param operateDomainRange: (Optional) 可选值。表示域名操作范围，可指定为all代表操作该账号下全量域名,全量域名个数应<=单次可批量操作的域名个数(默认50)
        """
        self.operateDomainRange = operateDomainRange

    def setDomains(self, domains):
        """
        :param domains: (Optional) 可选值。待操作的域名列表,个数默认限制50个。注意operateDomainRange和domains至少指定一个参数。operateDomainRange为all时该参数不生效.
        """
        self.domains = domains

    def setIpList(self, ipList):
        """
        :param ipList: (Optional) ip列表。最多50个
        """
        self.ipList = ipList

    def setForbidTime(self, forbidTime):
        """
        :param forbidTime: (Optional) 封禁时长，单位分钟。默认1440
        """
        self.forbidTime = forbidTime

    def setAction(self, action):
        """
        :param action: (Optional) forbid or resume.代表封禁和解封。
        """
        self.action = action

