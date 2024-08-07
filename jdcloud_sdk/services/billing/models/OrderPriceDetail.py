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


class OrderPriceDetail(object):

    def __init__(self, price=None, priceScale4=None, discount=None, discountedPrice=None, afterFavorablePrice=None, erasePrice=None, originalPrice=None, resourceId=None, appCode=None, serviceCode=None, site=None, region=None, az=None, billingType=None, timeSpan=None, timeUnit=None, networkOperator=None, formula=None, favorableInfo=None, priceSnapShot=None, pin=None, taskId=None, startTime=None, endTime=None, processType=None, sourceId=None, refundPrice=None, cashRefundPrice=None, balanceRefundPrice=None, couponRefundPrice=None, refundOrderList=None, billingItemPriceList=None):
        """
        :param price: (Optional) 原价(6位，原价为每个计费项原价之和)
        :param priceScale4: (Optional) 原价(6位，与price一致，兼容之前4位原价保留字段)
        :param discount: (Optional) 折扣金额（6位，折扣金额为每个计费项折扣金额之和）
        :param discountedPrice: (Optional) 应付金额（2位，应付金额=折扣后金额舍位保留2位小数)
        :param afterFavorablePrice: (Optional) 折扣后金额（6位，折扣后金额为每个计费项折扣后金额之和)
        :param erasePrice: (Optional) 抹零金额（6位，抹零金额=折扣后金额-应付金额)
        :param originalPrice: (Optional) 订单原价 包年时 一年原价为12个月价格，totalPrice为10个月价格
        :param resourceId: (Optional) 资源id
        :param appCode: (Optional) 业务线
        :param serviceCode: (Optional) 产品线
        :param site: (Optional) 站点  0:主站  其他:专有云
        :param region: (Optional) 地域
        :param az: (Optional) 可用区
        :param billingType: (Optional) 计费类型1:按配置2:按用量3:包年包月4:一次性5:抢占式
        :param timeSpan: (Optional) 时长
        :param timeUnit: (Optional) 时长类型 1:小时2:天3:月4:年 5:周
        :param networkOperator: (Optional) 网络类型 0:non1:非BGP2:BGP
        :param formula: (Optional) 配置信息
        :param favorableInfo: (Optional) FavorableInfo转成json后的字符串
        :param priceSnapShot: (Optional) 价格快照
        :param pin: (Optional) 用户pin
        :param taskId: (Optional) 自然单列表
        :param startTime: (Optional) 开始时间
        :param endTime: (Optional) 结束时间
        :param processType: (Optional) 变配明细（1-升配补差价，2-降配延时，3-临时升配，9-降配退款）
        :param sourceId: (Optional) 交易单模块sourceId
        :param refundPrice: (Optional) 资源退款金额
        :param cashRefundPrice: (Optional) 资源现金退款金额
        :param balanceRefundPrice: (Optional) 资源余额退款金额
        :param couponRefundPrice: (Optional) 资源代金券退款金额
        :param refundOrderList: (Optional) 退款订单列表
        :param billingItemPriceList: (Optional) 计费项价格列表
        """

        self.price = price
        self.priceScale4 = priceScale4
        self.discount = discount
        self.discountedPrice = discountedPrice
        self.afterFavorablePrice = afterFavorablePrice
        self.erasePrice = erasePrice
        self.originalPrice = originalPrice
        self.resourceId = resourceId
        self.appCode = appCode
        self.serviceCode = serviceCode
        self.site = site
        self.region = region
        self.az = az
        self.billingType = billingType
        self.timeSpan = timeSpan
        self.timeUnit = timeUnit
        self.networkOperator = networkOperator
        self.formula = formula
        self.favorableInfo = favorableInfo
        self.priceSnapShot = priceSnapShot
        self.pin = pin
        self.taskId = taskId
        self.startTime = startTime
        self.endTime = endTime
        self.processType = processType
        self.sourceId = sourceId
        self.refundPrice = refundPrice
        self.cashRefundPrice = cashRefundPrice
        self.balanceRefundPrice = balanceRefundPrice
        self.couponRefundPrice = couponRefundPrice
        self.refundOrderList = refundOrderList
        self.billingItemPriceList = billingItemPriceList
