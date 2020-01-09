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


class CreateAlarmSpec(object):

    def __init__(self, clientToken, product, resourceOption, ruleName, ruleOption, autoScalingPolicyId=None, baseContact=None, dimension=None, enabled=None, noticeOption=None, ruleType=None, tags=None, webHookOption=None):
        """
        :param autoScalingPolicyId: (Optional) 弹性伸缩组Id。注：仅ag\asg产品线内部使用
        :param baseContact: (Optional) 告警通知联系人
        :param clientToken:  幂等性校验参数,最长36位,若两个请求clientToken相等，则返回第一次创建的规则id，只创建一次规则
        :param dimension: (Optional) 资源维度，可用的维度请使用 describeProductsForAlarm接口查询
        :param enabled: (Optional) 是否启用, 1表示启用规则，0表示禁用规则，默认为1
        :param noticeOption: (Optional) 通知策略
        :param product:  资源类型, 可用的资源类型列表请使用 describeProductsForAlarm接口查询。
        :param resourceOption:  
        :param ruleName:  规则名称，规则名称，最大长度42个字符，只允许中英文、数字、''-''和"_"
        :param ruleOption:  
        :param ruleType: (Optional) 规则类型, 默认为resourceMonitor
        :param tags: (Optional) 资源维度，指定监控数据实例的维度标签,如resourceId=id。(请确认资源的监控数据带有该标签，否则规则会报数据不足)
        :param webHookOption: (Optional) 
        """

        self.autoScalingPolicyId = autoScalingPolicyId
        self.baseContact = baseContact
        self.clientToken = clientToken
        self.dimension = dimension
        self.enabled = enabled
        self.noticeOption = noticeOption
        self.product = product
        self.resourceOption = resourceOption
        self.ruleName = ruleName
        self.ruleOption = ruleOption
        self.ruleType = ruleType
        self.tags = tags
        self.webHookOption = webHookOption
