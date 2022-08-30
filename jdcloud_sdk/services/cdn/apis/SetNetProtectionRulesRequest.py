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


class SetNetProtectionRulesRequest(JDCloudRequest):
    """
    设置网络防护层规则
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetNetProtectionRulesRequest, self).__init__(
            '/netProtectionRules', 'POST', header, version)
        self.parameters = parameters


class SetNetProtectionRulesParameters(object):

    def __init__(self,):
        """
        """

        self.srcNewConnLimitEnable = None
        self.dstNewConnLimitEnable = None
        self.datagramRangeMin = None
        self.datagramRangeMax = None
        self.dstNewConnLimitValue = None
        self.srcNewConnLimitValue = None
        self.geoBlack = None
        self.ipBlack = None
        self.ipWhite = None

    def setSrcNewConnLimitEnable(self, srcNewConnLimitEnable):
        """
        :param srcNewConnLimitEnable: (Optional) 源新建连接限速，取值on,off，其中on开启，off关闭
        """
        self.srcNewConnLimitEnable = srcNewConnLimitEnable

    def setDstNewConnLimitEnable(self, dstNewConnLimitEnable):
        """
        :param dstNewConnLimitEnable: (Optional) 目的新建连接，取值on,off，其中on开启，off关闭
        """
        self.dstNewConnLimitEnable = dstNewConnLimitEnable

    def setDatagramRangeMin(self, datagramRangeMin):
        """
        :param datagramRangeMin: (Optional) 报文最小长度（包最小长度）,取值：1-1500
        """
        self.datagramRangeMin = datagramRangeMin

    def setDatagramRangeMax(self, datagramRangeMax):
        """
        :param datagramRangeMax: (Optional) 报文最大长度（包最大长度）,取值：1-1500
        """
        self.datagramRangeMax = datagramRangeMax

    def setDstNewConnLimitValue(self, dstNewConnLimitValue):
        """
        :param dstNewConnLimitValue: (Optional) 目的新建连接限速值，取值：0-4294967295
        """
        self.dstNewConnLimitValue = dstNewConnLimitValue

    def setSrcNewConnLimitValue(self, srcNewConnLimitValue):
        """
        :param srcNewConnLimitValue: (Optional) 源新建连接限速值，取值：0-4294967295
        """
        self.srcNewConnLimitValue = srcNewConnLimitValue

    def setGeoBlack(self, geoBlack):
        """
        :param geoBlack: (Optional) 地域黑名单（GEO IP拦截）
        """
        self.geoBlack = geoBlack

    def setIpBlack(self, ipBlack):
        """
        :param ipBlack: (Optional) ip 黑名单
        """
        self.ipBlack = ipBlack

    def setIpWhite(self, ipWhite):
        """
        :param ipWhite: (Optional) ip 白名单
        """
        self.ipWhite = ipWhite

