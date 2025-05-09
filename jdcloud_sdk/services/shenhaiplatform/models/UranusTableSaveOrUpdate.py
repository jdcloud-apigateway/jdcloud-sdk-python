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


class UranusTableSaveOrUpdate(object):

    def __init__(self, tableEnName, columns, tableCnName=None, owner=None, manager=None, partitions=None, isPartition=None, updateTable=None, storageType=None, fieldDelim=None, lineDelim=None, bucketCols=None, bucketNum=None):
        """
        :param tableEnName:  表英文名称
        :param tableCnName: (Optional) 表中文名
        :param owner: (Optional) 负责人
        :param manager: (Optional) 协助人
        :param columns:  表的普通字段信息
        :param partitions: (Optional) 表的分区字段信息
        :param isPartition: (Optional) 0 非分区表 1 分区表
        :param updateTable: (Optional) 0 新建表 1 修改表
        :param storageType: (Optional) 表存储格式
        :param fieldDelim: (Optional) 表字段分隔符（只有TEXTFILE类型表需要该字段）
        :param lineDelim: (Optional) 表行分隔符（只有TEXTFILE类型表需要该字段）
        :param bucketCols: (Optional) 分桶字段
        :param bucketNum: (Optional) 分桶字段
        """

        self.tableEnName = tableEnName
        self.tableCnName = tableCnName
        self.owner = owner
        self.manager = manager
        self.columns = columns
        self.partitions = partitions
        self.isPartition = isPartition
        self.updateTable = updateTable
        self.storageType = storageType
        self.fieldDelim = fieldDelim
        self.lineDelim = lineDelim
        self.bucketCols = bucketCols
        self.bucketNum = bucketNum
