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


class InvoiceTemplate(object):

    def __init__(self, invoiceType=None, invoiceTitle=None, invoiceContent=None, taxId=None, company=None, phone=None, bank=None, account=None, address=None, email=None, mediumType=None):
        """
        :param invoiceType: (Optional) 发票类型:[个人增值税普通发票-Personal_VAT_Ordinary_Invoice,企业增值税专用发票-Enterprise_VAT_Special_Invoice,企业增值税普通发票-Enterprise_VAT_Ordinary_Invoice]
        :param invoiceTitle: (Optional) 发票抬头
        :param invoiceContent: (Optional) 开票内容（按类别开票/按明细开票）
        :param taxId: (Optional) 纳税人识别码（发票类型为企业增值税专用发票和企业增值税普通发票时必填）
        :param company: (Optional) 单位名称（发票类型为企业增值税专用发票时必填）
        :param phone: (Optional) 注册电话（发票类型为个人增值税普通发票和企业增值税普通发票时作为收票人手机号）
        :param bank: (Optional) 开户银行（发票类型为企业增值税专用发票时必填）
        :param account: (Optional) 银行账户（发票类型为企业增值税专用发票时必填）
        :param address: (Optional) 注册地址（发票类型为企业增值税专用发票时必填）
        :param email: (Optional) 邮箱
        :param mediumType: (Optional) [电子-electronic]
        """

        self.invoiceType = invoiceType
        self.invoiceTitle = invoiceTitle
        self.invoiceContent = invoiceContent
        self.taxId = taxId
        self.company = company
        self.phone = phone
        self.bank = bank
        self.account = account
        self.address = address
        self.email = email
        self.mediumType = mediumType
