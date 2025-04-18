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


class SyncWsProductOrderReq(object):

    def __init__(self, region=None, billingVersion=None, billingModel=None, az=None, account=None, companyId=None, payPlan=None, autoRenewal=None, purchaseDuration=None, orderUniqueKey=None):
        """
        :param region: (Optional) 
        :param billingVersion: (Optional) 
        :param billingModel: (Optional) 
        :param az: (Optional) 
        :param account: (Optional) 
        :param companyId: (Optional) 
        :param payPlan: (Optional) 
        :param autoRenewal: (Optional) 
        :param purchaseDuration: (Optional) 
        :param orderUniqueKey: (Optional) 
        """

        self.region = region
        self.billingVersion = billingVersion
        self.billingModel = billingModel
        self.az = az
        self.account = account
        self.companyId = companyId
        self.payPlan = payPlan
        self.autoRenewal = autoRenewal
        self.purchaseDuration = purchaseDuration
        self.orderUniqueKey = orderUniqueKey
