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


class CustomPage(object):

    def __init__(self, id=None, name=None, content=None, updateTime=None, status=None):
        """
        :param id: (Optional) 自定义页面Id
        :param name: (Optional) 自定义页面名称
        :param content: (Optional) 自定义页面内容
        :param updateTime: (Optional) 更新时间
        :param status: (Optional) approving: 审批中, refused: 审批不通过, approved: 审批通过
        """

        self.id = id
        self.name = name
        self.content = content
        self.updateTime = updateTime
        self.status = status