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


class JtlasPageSearchTablePrivilegesRequest(JDCloudRequest):
    """
    检索表权限
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(JtlasPageSearchTablePrivilegesRequest, self).__init__(
            '/regions/{regionId}/apps/{appName}/jtlasPageSearchTablePrivileges', 'POST', header, version)
        self.parameters = parameters


class JtlasPageSearchTablePrivilegesParameters(object):

    def __init__(self,regionId, appName, database, tableName, pageNum, pageSize):
        """
        :param regionId: 地域ID
        :param appName: 应用名称
        :param database: 数据库（工作空间编码）
        :param tableName: 表名称
        :param pageNum: 分页参数-页码
        :param pageSize: 分页参数-页数
        """

        self.regionId = regionId
        self.appName = appName
        self.database = database
        self.tableName = tableName
        self.privilegeTypes = None
        self.pageNum = pageNum
        self.pageSize = pageSize

    def setPrivilegeTypes(self, privilegeTypes):
        """
        :param privilegeTypes: (Optional) 权限类型
        """
        self.privilegeTypes = privilegeTypes

