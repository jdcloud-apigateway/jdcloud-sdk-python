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


class LoginRequest(JDCloudRequest):
    """
    rds，drds登录实例
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(LoginRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:login', 'POST', header, version)
        self.parameters = parameters


class LoginParameters(object):

    def __init__(self, regionId,instanceId,):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: rds，drds的实例id。
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.dbType = None
        self.addrMode = None
        self.dbUser = None
        self.dbPassword = None

    def setDbType(self, dbType):
        """
        :param dbType: (Optional) 数据源源类型，CDS("CDS", 1), MYSQL("MYSQL", 2), ORACLE("ORACLE", 3), SQLSERVER("SQLSERVER", 4), CDSMYSQL("CDSMYSQL", 5), CDSORACLE("CDSORACLE", 6), CDSSQLSERVER("CDSSQLSERVER", 7), DATACENTER("DATACENTER", 8), HBASE("Hbase",9),MONGODB("MongoDb",10),ES("ES",11), MYSQL_INS("MYSQL_INS",12), DRDS_INS("DRDS_INS",13)。
        """
        self.dbType = dbType

    def setAddrMode(self, addrMode):
        """
        :param addrMode: (Optional) CLASSIC("CLASSIC", 0), RDS("RDS", 1), ECS("ECS", 2), VPC("VPC", 3), 当前只支持rds模式。
        """
        self.addrMode = addrMode

    def setDbUser(self, dbUser):
        """
        :param dbUser: (Optional) 数据库用户名。
        """
        self.dbUser = dbUser

    def setDbPassword(self, dbPassword):
        """
        :param dbPassword: (Optional) 数据库用户密码。
        """
        self.dbPassword = dbPassword

