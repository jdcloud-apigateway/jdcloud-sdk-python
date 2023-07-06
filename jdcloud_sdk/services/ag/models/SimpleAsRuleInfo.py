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


class SimpleAsRuleInfo(object):

    def __init__(self, adjustmentType=None, adjustmentValue=None, asAlarms=None, asCrons=None):
        """
        :param adjustmentType: (Optional) 伸缩调整方式，取值范围：[`Number`,`Percentage`,`Total`]
- `Number`：增加或减少指定数量的实例
- `Percentage`：增加或减少指定百分比的实例
- `Total`：将当前伸缩组的实例数量调整到指定数量

        :param adjustmentValue: (Optional) 伸缩的调整值，负数表示减少，正数表示增加
- `adjustmentType`为`Number`时，取值范围：[`-300` ~ `300`]
- `adjustmentType`为`Percentage`时，单位为百分比，取值范围：[`-100` ~ `10000`]
- `adjustmentType`为`Total`时，取值范围：[`0` ~ `100000`]

        :param asAlarms: (Optional) 关联的告警任务列表
        :param asCrons: (Optional) 关联的定时任务列表
        """

        self.adjustmentType = adjustmentType
        self.adjustmentValue = adjustmentValue
        self.asAlarms = asAlarms
        self.asCrons = asCrons
