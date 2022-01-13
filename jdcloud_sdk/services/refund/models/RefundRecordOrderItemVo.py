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


class RefundRecordOrderItemVo(object):

    def __init__(self, refundId=None, resourceId=None, resourceName=None, orderNumber=None, orderSubNumber=None, orderItemNumber=None, totalFee=None, discountFee=None, actualFee=None, couponFee=None, balanceFee=None, cashFee=None, couponRefundFee=None, balanceRefundFee=None, cashRefundFee=None, refundFee=None, chooseFlag=None, orderType=None, chargeMode=None, merchantId=None, cashRefundChannel=None, serviceCode=None, appCode=None):
        """
        :param refundId: (Optional) 退款单号
        :param resourceId: (Optional) 资源id
        :param resourceName: (Optional) 资源名称
        :param orderNumber: (Optional) 订单号
        :param orderSubNumber: (Optional) 子订单号
        :param orderItemNumber: (Optional) 订单商品编号
        :param totalFee: (Optional) 总订单金额
        :param discountFee: (Optional) 订单优惠金额
        :param actualFee: (Optional) 实际订单金额
        :param couponFee: (Optional) 优惠券支付金额
        :param balanceFee: (Optional) 余额支付金额
        :param cashFee: (Optional) 现金支付金额
        :param couponRefundFee: (Optional) 代金券退款金额
        :param balanceRefundFee: (Optional) 余额退款金额
        :param cashRefundFee: (Optional) 现金退款金额
        :param refundFee: (Optional) 总退款金额
        :param chooseFlag: (Optional) 选中标记 0-未选中 1-选中
        :param orderType: (Optional) 订单类型 来源于order 1-新购，2-续费，3-配置变更
        :param chargeMode: (Optional) 订单计费类型：来源于order 1-按配置，2-按用量，3-按包年/包月，4-一次性付费
        :param merchantId: (Optional) 台账业务编号
        :param cashRefundChannel: (Optional) 现金退款渠道 1-企业网银，2-个人网银，3-微信支付，4-京东支付，5-线下汇款
        :param serviceCode: (Optional) 产品线
        :param appCode: (Optional) 产品类目
        """

        self.refundId = refundId
        self.resourceId = resourceId
        self.resourceName = resourceName
        self.orderNumber = orderNumber
        self.orderSubNumber = orderSubNumber
        self.orderItemNumber = orderItemNumber
        self.totalFee = totalFee
        self.discountFee = discountFee
        self.actualFee = actualFee
        self.couponFee = couponFee
        self.balanceFee = balanceFee
        self.cashFee = cashFee
        self.couponRefundFee = couponRefundFee
        self.balanceRefundFee = balanceRefundFee
        self.cashRefundFee = cashRefundFee
        self.refundFee = refundFee
        self.chooseFlag = chooseFlag
        self.orderType = orderType
        self.chargeMode = chargeMode
        self.merchantId = merchantId
        self.cashRefundChannel = cashRefundChannel
        self.serviceCode = serviceCode
        self.appCode = appCode