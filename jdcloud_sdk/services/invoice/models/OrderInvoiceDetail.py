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


class OrderInvoiceDetail(object):

    def __init__(self, invoiceAmount=None, orderNumber=None, status=None):
        """
        :param invoiceAmount: (Optional) 开票金额
        :param orderNumber: (Optional) 订单号
        :param status: (Optional) 订单对应发票状态,(1 2 3 4 8 10表示有发票,5 6 7 9表示没有发票 9 退票)1:已申请 2:处理中 3:已开票 4:已邮寄 5:已驳回 6:已作废 7:已取消 8:退票中 9:已退票 10:退票驳回
        """

        self.invoiceAmount = invoiceAmount
        self.orderNumber = orderNumber
        self.status = status
