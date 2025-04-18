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


class ManageHubStoragePartitionListRequest(JDCloudRequest):
    """
    列出分区存储详情
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(ManageHubStoragePartitionListRequest, self).__init__(
            '/regions/{regionId}/apps/{appName}/manageHubStoragePartitionList', 'GET', header, version)
        self.parameters = parameters


class ManageHubStoragePartitionListParameters(object):

    def __init__(self,regionId, appName, companyCode, database, table, pageSize, pageNum):
        """
        :param regionId: 地域ID
        :param appName: 应用名称
        :param companyCode: 租户code
        :param database: 数据库名称
        :param table: 表名称
        :param pageSize: 分页大小
        :param pageNum: 页码
        """

        self.regionId = regionId
        self.appName = appName
        self.companyCode = companyCode
        self.database = database
        self.table = table
        self.pageSize = pageSize
        self.pageNum = pageNum

