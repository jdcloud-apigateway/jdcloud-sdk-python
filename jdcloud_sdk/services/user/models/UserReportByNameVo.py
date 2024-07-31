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


class UserReportByNameVo(object):

    def __init__(self, pin=None, reportName=None, accountAffiliation=None, accountAffiliationCode=None, sellerErp=None):
        """
        :param pin: (Optional) pin
        :param reportName: (Optional) 报备名称
        :param accountAffiliation: (Optional) 财务计收归属：（集团-1、外部-2、云内部-3）
        :param accountAffiliationCode: (Optional) 财务计收归属子属性
        :param sellerErp: (Optional) 销售员erp
        """

        self.pin = pin
        self.reportName = reportName
        self.accountAffiliation = accountAffiliation
        self.accountAffiliationCode = accountAffiliationCode
        self.sellerErp = sellerErp