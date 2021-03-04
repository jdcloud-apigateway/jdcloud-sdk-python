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


class ReceiptRecord(object):

    def __init__(self, receiptCount=None, unReceiptCount=None, receiptRate=None, receiptSuccessCount=None, receiptFailCount=None, receiptSuccessRate=None, startTime=None, endTime=None):
        """
        :param receiptCount: (Optional) 短信回执量
        :param unReceiptCount: (Optional) 短信未回执量
        :param receiptRate: (Optional) 短信回执率
        :param receiptSuccessCount: (Optional) 短信回执成功量
        :param receiptFailCount: (Optional) 短信回执失败量
        :param receiptSuccessRate: (Optional) 短信回执成功率率
        :param startTime: (Optional) 聚合开始时间
        :param endTime: (Optional) 聚合截止时间
        """

        self.receiptCount = receiptCount
        self.unReceiptCount = unReceiptCount
        self.receiptRate = receiptRate
        self.receiptSuccessCount = receiptSuccessCount
        self.receiptFailCount = receiptFailCount
        self.receiptSuccessRate = receiptSuccessRate
        self.startTime = startTime
        self.endTime = endTime