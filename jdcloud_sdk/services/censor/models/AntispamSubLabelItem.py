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


class AntispamSubLabelItem(object):

    def __init__(self, subLabel=None, rate=None, details=None):
        """
        :param subLabel: (Optional) 细分类，详细编码请参考下方对应细分类编码 对照表
        :param rate: (Optional) 置信度分数，0-1之间取值，1为置信度最高，0为置信度最低
        :param details: (Optional) 命中详情说明hitInfos:命中详细信息，针对subLabel的补充说明
        """

        self.subLabel = subLabel
        self.rate = rate
        self.details = details
