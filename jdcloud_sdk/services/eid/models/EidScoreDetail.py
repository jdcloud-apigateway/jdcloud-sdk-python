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


class EidScoreDetail(object):

    def __init__(self, riskTag=None, riskCode=None, riskClass=None):
        """
        :param riskTag: (Optional) 风险类型，对应riskCode的中文描述
        :param riskCode: (Optional) 风险类型编码，101-正常设备，其它标签参考标签列表
        :param riskClass: (Optional) 风险分类，对应riskCode的分类
        """

        self.riskTag = riskTag
        self.riskCode = riskCode
        self.riskClass = riskClass
