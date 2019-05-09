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


class CreateDatabaseRequest(JDCloudRequest):
    """
    创建一个数据库。 为了实例的管理和数据恢复，RDS对用户权限进行了限制，用户仅能通过控制台或本接口创建数据库
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateDatabaseRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/databases', 'POST', header, version)
        self.parameters = parameters


class CreateDatabaseParameters(object):

    def __init__(self, regionId, instanceId, dbName, characterSetName):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param dbName: 数据库名，数据库名称的限制请参考[帮助中心文档](../../../documentation/Database-and-Cache-Service/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
        :param characterSetName: 数据库的字符集名，当前支持的字符集请查看[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.dbName = dbName
        self.characterSetName = characterSetName

