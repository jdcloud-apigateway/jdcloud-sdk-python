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


class UranusColumnSaveOrUpdate(object):

    def __init__(self, fieldSort=None, fieldEnName=None, fieldCnName=None, fieldType=None, fieldLen=None, filedAccuracy=None, isPartition=None):
        """
        :param fieldSort: (Optional) 序号
        :param fieldEnName: (Optional) 字段英文名称
        :param fieldCnName: (Optional) 字段中文名称
        :param fieldType: (Optional) 字段类型
        :param fieldLen: (Optional) 字段长度 当字段类型为 bigdecimal 类型时配合字段精度一起使用
        :param filedAccuracy: (Optional) 字段精度
        :param isPartition: (Optional) 是否是分区字段(y/n)
        """

        self.fieldSort = fieldSort
        self.fieldEnName = fieldEnName
        self.fieldCnName = fieldCnName
        self.fieldType = fieldType
        self.fieldLen = fieldLen
        self.filedAccuracy = filedAccuracy
        self.isPartition = isPartition
