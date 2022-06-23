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


class CreateDataFlowRequest(JDCloudRequest):
    """
    创建数据变更工单
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateDataFlowRequest, self).__init__(
            '/regions/{regionId}/dataFlow:create', 'POST', header, version)
        self.parameters = parameters


class CreateDataFlowParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        """

        self.regionId = regionId
        self.dataSourceId = None
        self.dbName = None
        self.taskPlanTypeEnum = None
        self.dbaApproveTypeEnum = None
        self.memo = None
        self.sqlText = None
        self.sqlFileTaskId = None
        self.rollbackSqlText = None
        self.rollbackFileTaskId = None

    def setDataSourceId(self, dataSourceId):
        """
        :param dataSourceId: (Optional) 数据库id
        """
        self.dataSourceId = dataSourceId

    def setDbName(self, dbName):
        """
        :param dbName: (Optional) 数据库名称
        """
        self.dbName = dbName

    def setTaskPlanTypeEnum(self, taskPlanTypeEnum):
        """
        :param taskPlanTypeEnum: (Optional) 执行方式，AUTO("AUTO", 0), BY_CREATOR("BY_CREATOR", 1)
        """
        self.taskPlanTypeEnum = taskPlanTypeEnum

    def setDbaApproveTypeEnum(self, dbaApproveTypeEnum):
        """
        :param dbaApproveTypeEnum: (Optional) DBA审批方式，AUTO("AUTO", 0), MANUAL("MANUAL", 1)
        """
        self.dbaApproveTypeEnum = dbaApproveTypeEnum

    def setMemo(self, memo):
        """
        :param memo: (Optional) 申请原因
        """
        self.memo = memo

    def setSqlText(self, sqlText):
        """
        :param sqlText: (Optional) SQL文本，变更SQL选择文本时，必填
        """
        self.sqlText = sqlText

    def setSqlFileTaskId(self, sqlFileTaskId):
        """
        :param sqlFileTaskId: (Optional) SQL附件导入任务Id
        """
        self.sqlFileTaskId = sqlFileTaskId

    def setRollbackSqlText(self, rollbackSqlText):
        """
        :param rollbackSqlText: (Optional) 回滚SQL文本，选填
        """
        self.rollbackSqlText = rollbackSqlText

    def setRollbackFileTaskId(self, rollbackFileTaskId):
        """
        :param rollbackFileTaskId: (Optional) 回滚SQL附件导入任务Id
        """
        self.rollbackFileTaskId = rollbackFileTaskId

