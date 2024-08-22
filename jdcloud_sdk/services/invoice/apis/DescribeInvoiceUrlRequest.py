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


class DescribeInvoiceUrlRequest(JDCloudRequest):
    """
    获取电子发票下载地址
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(DescribeInvoiceUrlRequest, self).__init__(
            '/regions/{regionId}/invoice:downloadurl', 'POST', header, version)
        self.parameters = parameters


class DescribeInvoiceUrlParameters(object):

    def __init__(self,regionId, ):
        """
        :param regionId: 地域编码，参考OpenAPI公共说明
        """

        self.regionId = regionId
        self.businessId = None
        self.ivcCode = None
        self.ivcNo = None
        self.wid = None

    def setBusinessId(self, businessId):
        """
        :param businessId: (Optional) 订单号或者申请单号
        """
        self.businessId = businessId

    def setIvcCode(self, ivcCode):
        """
        :param ivcCode: (Optional) 发票代码
        """
        self.ivcCode = ivcCode

    def setIvcNo(self, ivcNo):
        """
        :param ivcNo: (Optional) 发票号码
        """
        self.ivcNo = ivcNo

    def setWid(self, wid):
        """
        :param wid: (Optional) 商品编号
        """
        self.wid = wid

