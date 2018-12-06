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


class CmAlarmHistory(object):

    def __init__(self, calculation=None, contactGroups=None, contactPersons=None, deleted=None, enabled=None, id=None, metric=None, metricName=None, namespace=None, namespaceUID=None, noticePeriod=None, noticeTime=None, obj=None, objUID=None, operation=None, period=None, region=None, resourceId=None, rootRuleId=None, ruleId=None, serviceCode=None, tag=None, threshold=None, times=None, value=None):
        """
        :param calculation: (Optional) 统计方法：平均值=avg、最大值=max、最小值=min
        :param contactGroups: (Optional) 
        :param contactPersons: (Optional) 
        :param deleted: (Optional) 该规则是否已经被删除，1表示已经被删除，0表示未删除，被删除的规则，在使用查询规则的接口时，将不会被检索到
        :param enabled: (Optional) 启用禁用 1启用，0禁用
        :param id: (Optional) 规则id
        :param metric: (Optional) 监控项
        :param metricName: (Optional) 规则id监控项名称
        :param namespace: (Optional) 命名空间
        :param namespaceUID: (Optional) 命名空间id
        :param noticePeriod: (Optional) 通知周期 单位：小时
        :param noticeTime: (Optional) 
        :param obj: (Optional) 对象
        :param objUID: (Optional) 对象id
        :param operation: (Optional) >=、>、<、<=、=、！=
        :param period: (Optional) 统计周期（单位：分钟）
        :param region: (Optional) 地域信息
        :param resourceId: (Optional) 此规则所应用的资源id
        :param rootRuleId: (Optional) root rule id
        :param ruleId: (Optional) rule id
        :param serviceCode: (Optional) 报警规则对应的产品
        :param tag: (Optional) 监控项附属信息
        :param threshold: (Optional) 阈值
        :param times: (Optional) 连续多少次后报警
        :param value: (Optional) 报警值
        """

        self.calculation = calculation
        self.contactGroups = contactGroups
        self.contactPersons = contactPersons
        self.deleted = deleted
        self.enabled = enabled
        self.id = id
        self.metric = metric
        self.metricName = metricName
        self.namespace = namespace
        self.namespaceUID = namespaceUID
        self.noticePeriod = noticePeriod
        self.noticeTime = noticeTime
        self.obj = obj
        self.objUID = objUID
        self.operation = operation
        self.period = period
        self.region = region
        self.resourceId = resourceId
        self.rootRuleId = rootRuleId
        self.ruleId = ruleId
        self.serviceCode = serviceCode
        self.tag = tag
        self.threshold = threshold
        self.times = times
        self.value = value
