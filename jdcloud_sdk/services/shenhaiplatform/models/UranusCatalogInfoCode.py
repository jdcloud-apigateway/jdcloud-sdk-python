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


class UranusCatalogInfoCode(object):

    def __init__(self, catalogCode, unrealId=None, catalogName=None, catalogType=None, parentCode=None, childrenNum=None):
        """
        :param unrealId: (Optional) 前端排序唯一ID
        :param catalogCode:  目录code
        :param catalogName: (Optional) 目录名称
        :param catalogType: (Optional) 0：非叶子目录， 1：叶子目录
        :param parentCode: (Optional) 父目录code
        :param childrenNum: (Optional) 子节点数量
        """

        self.unrealId = unrealId
        self.catalogCode = catalogCode
        self.catalogName = catalogName
        self.catalogType = catalogType
        self.parentCode = parentCode
        self.childrenNum = childrenNum
