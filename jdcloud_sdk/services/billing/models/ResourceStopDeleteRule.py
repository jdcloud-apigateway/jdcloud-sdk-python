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


class ResourceStopDeleteRule(object):

    def __init__(self, site, appCode, ruleType, arrearStop, arrearStopDelayHours, arrearDelete, arrearDeleteDelayHours, expireStop, expireStopDelayHours, expireDelete, expireDeleteDelayHours, arrearDeleteType, expireDeleteType, flowArrearStop, flowArrearStopDelayHours, flowArrearDelete, flowArrearDeleteDelayHours, flowArrearDeleteType, pin=None, serviceCode=None, clientType=None):
        """
        :param site:  站点
        :param appCode:  产品线
        :param pin: (Optional) pin
        :param ruleType:  规则类型 1：试用规则 2、用户产品规则 3：用户规则 4：产品规则 5：通用规则 6：用户等级产品规则
        :param serviceCode: (Optional) 产品
        :param arrearStop:  按配置欠费是否停服  1：欠费需要停服 0：欠费不需要停服
        :param arrearStopDelayHours:  按配置欠费停服延后时长(0：立即停服  n：n几小时后停服)
        :param arrearDelete:  按配置欠费停服是否释放资源  1：需要释放资源 0：不需要释放资源
        :param arrearDeleteDelayHours:  按配置欠费停服释放资源延后时长(0：立即释放资源 n：n几小时后释放资源)
        :param expireStop:  到期是否停服  1：到期需要停服 0：到期不需要停服
        :param expireStopDelayHours:  到期停服延后时长(0：立即停服  n：n几小时后停服)
        :param expireDelete:  到期停服是否释放资源  1：需要释放资源 0：不需要释放资源
        :param expireDeleteDelayHours:  到期停服释放资源延后时长(0：立即释放资源  n：n几小时后释放资源)
        :param arrearDeleteType:  按配置欠费释放类型 1：释放资源  2：释放数据
        :param expireDeleteType:  到期释放类型 1：释放资源  2：释放数据
        :param flowArrearStop:  按用量欠费是否停服  1：欠费需要停服 0：欠费不需要停服
        :param flowArrearStopDelayHours:  按用量欠费停服延后时长
        :param flowArrearDelete:  按用量欠费停服是否释放资源  1：需要释放资源 0：不需要释放资源
        :param flowArrearDeleteDelayHours:  按用量欠费停服释放资源延后时长
        :param flowArrearDeleteType:  按用量欠费释放类型 1：释放资源  2：释放数据
        :param clientType: (Optional) 客户级别 1-普通客户 2-VIP客户
        """

        self.site = site
        self.appCode = appCode
        self.pin = pin
        self.ruleType = ruleType
        self.serviceCode = serviceCode
        self.arrearStop = arrearStop
        self.arrearStopDelayHours = arrearStopDelayHours
        self.arrearDelete = arrearDelete
        self.arrearDeleteDelayHours = arrearDeleteDelayHours
        self.expireStop = expireStop
        self.expireStopDelayHours = expireStopDelayHours
        self.expireDelete = expireDelete
        self.expireDeleteDelayHours = expireDeleteDelayHours
        self.arrearDeleteType = arrearDeleteType
        self.expireDeleteType = expireDeleteType
        self.flowArrearStop = flowArrearStop
        self.flowArrearStopDelayHours = flowArrearStopDelayHours
        self.flowArrearDelete = flowArrearDelete
        self.flowArrearDeleteDelayHours = flowArrearDeleteDelayHours
        self.flowArrearDeleteType = flowArrearDeleteType
        self.clientType = clientType