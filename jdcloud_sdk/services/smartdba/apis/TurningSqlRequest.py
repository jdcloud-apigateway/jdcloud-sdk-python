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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class TurningSqlRequest(JDCloudRequest):
    """
    SQL优化
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(TurningSqlRequest, self).__init__(
            '/regions/{regionId}/instance/{instanceGid}/tuningSql', 'POST', header, version)
        self.parameters = parameters


class TurningSqlParameters(object):

    def __init__(self, regionId,instanceGid,):
        """
        :param regionId: 地域代码
        :param instanceGid: 实例ID
        """

        self.regionId = regionId
        self.instanceGid = instanceGid
        self.database = None
        self.sql = None

    def setDatabase(self, database):
        """
        :param database: (Optional) 数据库名
        """
        self.database = database

    def setSql(self, sql):
        """
        :param sql: (Optional) SQL语句
        """
        self.sql = sql

