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


class CreatePolicyInfo(object):

    def __init__(self, name, content, description=None):
        """
        :param name:  策略名，支持4~64位的字母，数字以及-和_, 以字母开头
        :param description: (Optional) 描述，0~256个字符
        :param content:  策略文档，最多6144个字符
        """

        self.name = name
        self.description = description
        self.content = content
