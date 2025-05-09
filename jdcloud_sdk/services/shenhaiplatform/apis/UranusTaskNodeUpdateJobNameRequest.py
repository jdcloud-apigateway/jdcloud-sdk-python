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


class UranusTaskNodeUpdateJobNameRequest(JDCloudRequest):
    """
    任务单节点-更新作业名称
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(UranusTaskNodeUpdateJobNameRequest, self).__init__(
            '/regions/{regionId}/apps/{appName}/uranusTaskNodeUpdateJobName', 'POST', header, version)
        self.parameters = parameters


class UranusTaskNodeUpdateJobNameParameters(object):

    def __init__(self,regionId, appName, taskName, taskNodeId, taskCode, manager, flowCode, ):
        """
        :param regionId: 地域ID
        :param appName: 应用名称
        :param taskName: 节点名称
        :param taskNodeId: 任务类型
        :param taskCode: 节点CODE
        :param manager: 负责人
        :param flowCode: 工作流Code
        """

        self.regionId = regionId
        self.appName = appName
        self.taskName = taskName
        self.childrenCode = None
        self.parentCode = None
        self.taskDesc = None
        self.taskNodeId = taskNodeId
        self.taskCode = taskCode
        self.manager = manager
        self.taskData = None
        self.nodeName = None
        self.nodeTypeName = None
        self.nodeIcon = None
        self.flowCode = flowCode
        self.fileCode = None
        self.jobName = None
        self.isUranus = None
        self.isCurrentFlow = None
        self.parent = None
        self.haveChildren = None
        self.cooperator = None

    def setChildrenCode(self, childrenCode):
        """
        :param childrenCode: (Optional) 子节点code List
        """
        self.childrenCode = childrenCode

    def setParentCode(self, parentCode):
        """
        :param parentCode: (Optional) 父节点code List
        """
        self.parentCode = parentCode

    def setTaskDesc(self, taskDesc):
        """
        :param taskDesc: (Optional) 节点描述
        """
        self.taskDesc = taskDesc

    def setTaskData(self, taskData):
        """
        :param taskData: (Optional) 节点数据 以下前端需要用到的数据
        """
        self.taskData = taskData

    def setNodeName(self, nodeName):
        """
        :param nodeName: (Optional) 节点名称 以下前端需要用到的数据
        """
        self.nodeName = nodeName

    def setNodeTypeName(self, nodeTypeName):
        """
        :param nodeTypeName: (Optional) 节点类型
        """
        self.nodeTypeName = nodeTypeName

    def setNodeIcon(self, nodeIcon):
        """
        :param nodeIcon: (Optional) 节点图标 以下前端需要用到的数据
        """
        self.nodeIcon = nodeIcon

    def setFileCode(self, fileCode):
        """
        :param fileCode: (Optional) 脚本文件的业务Code
        """
        self.fileCode = fileCode

    def setJobName(self, jobName):
        """
        :param jobName: (Optional) 作业名称
        """
        self.jobName = jobName

    def setIsUranus(self, isUranus):
        """
        :param isUranus: (Optional) 是否工作流任务
        """
        self.isUranus = isUranus

    def setIsCurrentFlow(self, isCurrentFlow):
        """
        :param isCurrentFlow: (Optional) 是否当前工作流任务
        """
        self.isCurrentFlow = isCurrentFlow

    def setParent(self, parent):
        """
        :param parent: (Optional) 给前端用到的
        """
        self.parent = parent

    def setHaveChildren(self, haveChildren):
        """
        :param haveChildren: (Optional) 是否有子任务依赖前端用到
        """
        self.haveChildren = haveChildren

    def setCooperator(self, cooperator):
        """
        :param cooperator: (Optional) 协作人
        """
        self.cooperator = cooperator

