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


class JtlasTableUnderSpecifiedUserReq(object):

    def __init__(self, database, principalName, fuzzyName=None):
        """
        :param database:  数据库（工作空间编码）
        :param principalName:  账户信息
        :param fuzzyName: (Optional) 表名称
        """

        self.database = database
        self.principalName = principalName
        self.fuzzyName = fuzzyName
