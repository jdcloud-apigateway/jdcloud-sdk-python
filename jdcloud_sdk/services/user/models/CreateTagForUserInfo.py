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


class CreateTagForUserInfo(object):

    def __init__(self, label, labelValue=None):
        """
        :param label:  用户特征标签键，打标签前需确定好是否已经允许打此标签键
        :param labelValue: (Optional) 用户特征标签值，范围[0，1000]
        """

        self.label = label
        self.labelValue = labelValue
