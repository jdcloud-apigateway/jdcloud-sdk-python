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


class FunctionCatalogVo(object):

    def __init__(self, functionCatalogName=None, functionCatalogId=None, hasChildren=None, children=None):
        """
        :param functionCatalogName: (Optional) 分类目录名称
        :param functionCatalogId: (Optional) 分类目录id
        :param hasChildren: (Optional) 是否有子目录
        :param children: (Optional) 子目录
        """

        self.functionCatalogName = functionCatalogName
        self.functionCatalogId = functionCatalogId
        self.hasChildren = hasChildren
        self.children = children
