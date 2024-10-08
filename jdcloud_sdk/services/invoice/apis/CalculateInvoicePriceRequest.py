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


class CalculateInvoicePriceRequest(JDCloudRequest):
    """
    根据订单信息和总金额计算单个订单金额
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(CalculateInvoicePriceRequest, self).__init__(
            '/regions/{regionId}/calculateInvoicePrice', 'POST', header, version)
        self.parameters = parameters


class CalculateInvoicePriceParameters(object):

    def __init__(self,regionId, ):
        """
        :param regionId: 地域编码，参考OpenAPI公共说明
        """

        self.regionId = regionId
        self.amount = None
        self.orderInfo = None

    def setAmount(self, amount):
        """
        :param amount: (Optional) 预开票总金额（不传则简单计算金额）
        """
        self.amount = amount

    def setOrderInfo(self, orderInfo):
        """
        :param orderInfo: (Optional) 
        """
        self.orderInfo = orderInfo

