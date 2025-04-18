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


class UranusTaskFlowTreeReq(object):

    def __init__(self, keyWord=None, catalogCode=None, flowCode=None, searchType=None):
        """
        :param keyWord: (Optional) 关键字查询
        :param catalogCode: (Optional) 目录code
        :param flowCode: (Optional) 工作流code
        :param searchType: (Optional) 查询过滤条件  all 全部、recent 最近使用、join 参数、collection 收藏
        """

        self.keyWord = keyWord
        self.catalogCode = catalogCode
        self.flowCode = flowCode
        self.searchType = searchType
