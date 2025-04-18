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


class UranusTaskFlowUpdateRequest(JDCloudRequest):
    """
    工作流更新
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(UranusTaskFlowUpdateRequest, self).__init__(
            '/regions/{regionId}/apps/{appName}/uranusTaskFlowUpdate', 'POST', header, version)
        self.parameters = parameters


class UranusTaskFlowUpdateParameters(object):

    def __init__(self,regionId, appName, flowName, catalogCode, flowCode, ):
        """
        :param regionId: 地域ID
        :param appName: 应用名称
        :param flowName: 工作流名称
        :param catalogCode: 工作流所属目录
        :param flowCode: 工作流code
        """

        self.regionId = regionId
        self.appName = appName
        self.flowName = flowName
        self.flowDesc = None
        self.catalogCode = catalogCode
        self.workers = None
        self.flowCode = flowCode
        self.manager = None

    def setFlowDesc(self, flowDesc):
        """
        :param flowDesc: (Optional) 工作流描述
        """
        self.flowDesc = flowDesc

    def setWorkers(self, workers):
        """
        :param workers: (Optional) 工作流协同人
        """
        self.workers = workers

    def setManager(self, manager):
        """
        :param manager: (Optional) 负责人
        """
        self.manager = manager

