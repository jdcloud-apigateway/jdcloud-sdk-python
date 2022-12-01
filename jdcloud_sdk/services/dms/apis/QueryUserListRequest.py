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


class QueryUserListRequest(JDCloudRequest):
    """
    用户管理列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryUserListRequest, self).__init__(
            '/management:queryUserList', 'POST', header, version)
        self.parameters = parameters


class QueryUserListParameters(object):

    def __init__(self,):
        """
        """

        self.activeStatus = None
        self.role = None
        self.loginDateStart = None
        self.loginDateEnd = None
        self.username = None
        self.pageNumber = None
        self.pageSize = None

    def setActiveStatus(self, activeStatus):
        """
        :param activeStatus: (Optional) 查询的用户状态(启用(true),禁用(false))
        """
        self.activeStatus = activeStatus

    def setRole(self, role):
        """
        :param role: (Optional) 查询的用户角色,枚举值(Admin("Admin","管理员"),DBA("DBA","DBA"),StructureReadOnly("StructureReadOnly","结构只读"),Normal("Normal","普通用户"))
        """
        self.role = role

    def setLoginDateStart(self, loginDateStart):
        """
        :param loginDateStart: (Optional) 查询的用户登录开始时间(yyyy-MM-dd'T'HH:mm:ss.SSS'Z')
        """
        self.loginDateStart = loginDateStart

    def setLoginDateEnd(self, loginDateEnd):
        """
        :param loginDateEnd: (Optional) 查询的用户登录结束时间(yyyy-MM-dd'T'HH:mm:ss.SSS'Z')
        """
        self.loginDateEnd = loginDateEnd

    def setUsername(self, username):
        """
        :param username: (Optional) 查询用户的用户名称
        """
        self.username = username

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 显示数据的页码，取值范围：[1,∞)。pageNumber为Null时，返回所有数据页码；超过总页数时，无数据。
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页显示的数据条数，用于查询列表的接口。
        """
        self.pageSize = pageSize

