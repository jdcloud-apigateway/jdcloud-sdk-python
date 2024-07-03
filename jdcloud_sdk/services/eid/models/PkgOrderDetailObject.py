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


class PkgOrderDetailObject(object):

    def __init__(self, pin=None, packageType=None, specs=None, payTime=None, status=None, totalFee=None, favorableFee=None, balanceFee=None, actualFee=None):
        """
        :param pin: (Optional) 用户pin
        :param packageType: (Optional) 产品名称
        :param specs: (Optional) 规格
        :param payTime: (Optional) 下单时间, yyyy-mm-dd hh:mm:ss格式
        :param status: (Optional) 订单状态：PAID - 支付,PRE-PAID - 预支付
        :param totalFee: (Optional) 订单金额
        :param favorableFee: (Optional) 代金券
        :param balanceFee: (Optional) 余额
        :param actualFee: (Optional) 实付总金额
        """

        self.pin = pin
        self.packageType = packageType
        self.specs = specs
        self.payTime = payTime
        self.status = status
        self.totalFee = totalFee
        self.favorableFee = favorableFee
        self.balanceFee = balanceFee
        self.actualFee = actualFee
