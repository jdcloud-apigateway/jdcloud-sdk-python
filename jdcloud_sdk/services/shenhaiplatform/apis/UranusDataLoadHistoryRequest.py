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


class UranusDataLoadHistoryRequest(JDCloudRequest):
    """
    数据上传历史任务
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(UranusDataLoadHistoryRequest, self).__init__(
            '/regions/{regionId}/apps/{appName}/uranusDataLoadHistory', 'POST', header, version)
        self.parameters = parameters


class UranusDataLoadHistoryParameters(object):

    def __init__(self,regionId, appName, ):
        """
        :param regionId: 地域ID
        :param appName: 应用名称
        """

        self.regionId = regionId
        self.appName = appName
        self.pageNum = None
        self.pageSize = None
        self.tableName = None
        self.states = None

    def setPageNum(self, pageNum):
        """
        :param pageNum: (Optional) 页号
        """
        self.pageNum = pageNum

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页面容量
        """
        self.pageSize = pageSize

    def setTableName(self, tableName):
        """
        :param tableName: (Optional) 表名
        """
        self.tableName = tableName

    def setStates(self, states):
        """
        :param states: (Optional) 状态过滤: SUBMITTED 已提交、ACCEPTED 等待执行、RUNNING 上传中、FINISHED 成功、FAILED 上传失败、KILLED 终止、UNKNOWN 未知
        """
        self.states = states

