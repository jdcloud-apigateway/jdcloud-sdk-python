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


class DmsHistorySql(object):

    def __init__(self, sql=None, user=None, status=None, createTime=None, spendTime=None, message=None, database=None):
        """
        :param sql: (Optional) 执行sql内容。
        :param user: (Optional) 执行用户。
        :param status: (Optional) 执行状态
        :param createTime: (Optional) 创建时间，格式为：YYYY-MM-DD HH:mm:ss。
        :param spendTime: (Optional) 执行花费时间，单位ms。
        :param message: (Optional) 执行消息。
        :param database: (Optional) 数据库名称。
        """

        self.sql = sql
        self.user = user
        self.status = status
        self.createTime = createTime
        self.spendTime = spendTime
        self.message = message
        self.database = database