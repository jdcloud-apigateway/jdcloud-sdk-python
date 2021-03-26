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


class OrderVo(object):

    def __init__(self, orderType=None, sourceId=None, timeUnit=None, timeSpan=None, taskId=None, autoRenew=None, renewTimeUnit=None, renewTimeSpan=None, autoPay=None):
        """
        :param orderType: (Optional) 付费类型 NEW - 新购  RESIZE_FORMULA - 变配
        :param sourceId: (Optional) 需要变配的资源ID（变配必传）
        :param timeUnit: (Optional) 购买时长类型, 新购时必传.
MONTH: 按月购买
YEAR: 按年购买

        :param timeSpan: (Optional) 购买时长, 新购时必传.
timeUnit = MONTH 时, 可取值 1-9
timeUnit = YEAR 时, 可取值 1-3

        :param taskId: (Optional) 打包标识，组合购使用，可以为空
        :param autoRenew: (Optional) OPEN-开通自动续费,CLOSE-关闭自动续费,默认关闭
开通自动续费时,renewTimeUnit,renewTimeSpan为必选项

        :param renewTimeUnit: (Optional) 自动续费时间单位(MONTH-月,YEAR-年)
        :param renewTimeSpan: (Optional) 自动续费时长
1. renewTimeUnit=MONTH 时，取值范围 [1,9]
2. renewTimeUnit=YEAR 时，取值范围 [1,3]

        :param autoPay: (Optional) 自动支付标识(SDK下单自动付费时设置为true)
        """

        self.orderType = orderType
        self.sourceId = sourceId
        self.timeUnit = timeUnit
        self.timeSpan = timeSpan
        self.taskId = taskId
        self.autoRenew = autoRenew
        self.renewTimeUnit = renewTimeUnit
        self.renewTimeSpan = renewTimeSpan
        self.autoPay = autoPay
