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


class DmsInstance(object):

    def __init__(self, dbType=None, dataSource=None, instanceInfo=None):
        """
        :param dbType: (Optional) 数据库类型，CDS("CDS", 1), MYSQL("MYSQL", 2), ORACLE("ORACLE", 3), SQLSERVER("SQLSERVER", 4), CDSMYSQL("CDSMYSQL", 5), CDSORACLE("CDSORACLE", 6), CDSSQLSERVER("CDSSQLSERVER", 7), DATACENTER("DATACENTER", 8), HBASE("Hbase",9),MONGODB("MongoDb",10),ES("ES",11), MYSQL_INS("MYSQL_INS",12), DRDS_INS("DRDS_INS",13), STARDB_INS("STARDB_INS",14), STARDB_PROXY_INS("STARDB_PROXY_INS",15);。
        :param dataSource: (Optional) 数据源详情。
        :param instanceInfo: (Optional) 从RDS，DRDS获取的数据源详情。
        """

        self.dbType = dbType
        self.dataSource = dataSource
        self.instanceInfo = instanceInfo
