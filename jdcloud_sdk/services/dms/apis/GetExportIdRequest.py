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


class GetExportIdRequest(JDCloudRequest):
    """
    生成表结构数据导出下载Id
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetExportIdRequest, self).__init__(
            '/regions/{regionId}/console:getExportId', 'POST', header, version)
        self.parameters = parameters


class GetExportIdParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        """

        self.regionId = regionId
        self.dataSourceId = None
        self.dbName = None
        self.charset = None
        self.exportTypeEnum = None
        self.exportFileTypeEnum = None
        self.exportContentTypeEnum = None
        self.tableFilters = None

    def setDataSourceId(self, dataSourceId):
        """
        :param dataSourceId: (Optional) 数据源id
        """
        self.dataSourceId = dataSourceId

    def setDbName(self, dbName):
        """
        :param dbName: (Optional) 数据库名称
        """
        self.dbName = dbName

    def setCharset(self, charset):
        """
        :param charset: (Optional) 导出文件字符编码
        """
        self.charset = charset

    def setExportTypeEnum(self, exportTypeEnum):
        """
        :param exportTypeEnum: (Optional) 导出方式，SYNC("SYNC", 0), ASYNC("ASYNC", 1)，当前只支持SYNC导出;
        """
        self.exportTypeEnum = exportTypeEnum

    def setExportFileTypeEnum(self, exportFileTypeEnum):
        """
        :param exportFileTypeEnum: (Optional) 导出文件格式，CSV("CSV", 0), SQL("SQL", 1);
        """
        self.exportFileTypeEnum = exportFileTypeEnum

    def setExportContentTypeEnum(self, exportContentTypeEnum):
        """
        :param exportContentTypeEnum: (Optional) 导出内容，DATA("DATA", 0), STRUCT("STRUCT", 1), STRUCT_DATA("STRUCT_DATA", 2);
        """
        self.exportContentTypeEnum = exportContentTypeEnum

    def setTableFilters(self, tableFilters):
        """
        :param tableFilters: (Optional) 查询条件。
        """
        self.tableFilters = tableFilters

