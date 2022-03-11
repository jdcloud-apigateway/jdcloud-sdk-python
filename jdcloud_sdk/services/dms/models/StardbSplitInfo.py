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


class StardbSplitInfo(object):

    def __init__(self, splitType=None, tableSplitCount=None, columnNames=None, splitDateBegin=None, splitDateEnd=None):
        """
        :param splitType: (Optional) 切分方式，"MODULO：取模, "HASH"：哈希, "DB_TABLE"：分库分表, "YYYYMMDD","YYYYMM","MM","MMDD"
        :param tableSplitCount: (Optional) 切分表数量,表切分方式为哈希取模时必需
        :param columnNames: (Optional) 切分列名称，第一项为切分表的列（必需），第二项为切分库的列（非必需)
        :param splitDateBegin: (Optional) 起始时间，切分方式为时间时必需，格式为20220125
        :param splitDateEnd: (Optional) 结束时间，切分方式为时间时必需，格式为20220125
        """

        self.splitType = splitType
        self.tableSplitCount = tableSplitCount
        self.columnNames = columnNames
        self.splitDateBegin = splitDateBegin
        self.splitDateEnd = splitDateEnd