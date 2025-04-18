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


class JtlasWarehouseTable(object):

    def __init__(self, id=None, projectCode=None, database=None, tableName=None, tableAlias=None, tableType=None, creator=None, metaType=None, createTime=None, lastModifyTime=None, location=None, inputFormat=None, outputFormat=None, userDefineTags=None, collectPersons=None, clickCount=None, latestPartition=None, columns=None, privileges=None, params=None, bucketCols=None, bucketNum=None):
        """
        :param id: (Optional) 表id
        :param projectCode: (Optional) 项目id
        :param database: (Optional) 数据库名称
        :param tableName: (Optional) 表名称
        :param tableAlias: (Optional) 表别名
        :param tableType: (Optional) 表类型：MANAGED_TABLE，EXTERNAL_TABLE
        :param creator: (Optional) 创建人
        :param metaType: (Optional) 元数据类型：HIVE，MYSQL
        :param createTime: (Optional) 创建时间
        :param lastModifyTime: (Optional) 最后修改时间
        :param location: (Optional) 表存储路径
        :param inputFormat: (Optional) 输入格式
        :param outputFormat: (Optional) 输出格式
        :param userDefineTags: (Optional) 用户打标
        :param collectPersons: (Optional) 负责人
        :param clickCount: (Optional) 点击数
        :param latestPartition: (Optional) 最近一次分区
        :param columns: (Optional) 
        :param privileges: (Optional) 
        :param params: (Optional) 表信息额外参数
        :param bucketCols: (Optional) 分桶字段
        :param bucketNum: (Optional) 分桶个数
        """

        self.id = id
        self.projectCode = projectCode
        self.database = database
        self.tableName = tableName
        self.tableAlias = tableAlias
        self.tableType = tableType
        self.creator = creator
        self.metaType = metaType
        self.createTime = createTime
        self.lastModifyTime = lastModifyTime
        self.location = location
        self.inputFormat = inputFormat
        self.outputFormat = outputFormat
        self.userDefineTags = userDefineTags
        self.collectPersons = collectPersons
        self.clickCount = clickCount
        self.latestPartition = latestPartition
        self.columns = columns
        self.privileges = privileges
        self.params = params
        self.bucketCols = bucketCols
        self.bucketNum = bucketNum
