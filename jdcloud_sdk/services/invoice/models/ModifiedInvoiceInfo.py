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


class ModifiedInvoiceInfo(object):

    def __init__(self, pin=None, invoiceNumber=None, orderNumberList=None, invoiceFee=None, invoiceStatus=None, action=None):
        """
        :param pin: (Optional) pin
        :param invoiceNumber: (Optional) 订单号
        :param orderNumberList: (Optional) 发票对应订单号列表
        :param invoiceFee: (Optional) 发票开票金额
        :param invoiceStatus: (Optional) 发票状态
        :param action: (Optional) 操作行为， 1.退款 2.开票更新
        """

        self.pin = pin
        self.invoiceNumber = invoiceNumber
        self.orderNumberList = orderNumberList
        self.invoiceFee = invoiceFee
        self.invoiceStatus = invoiceStatus
        self.action = action