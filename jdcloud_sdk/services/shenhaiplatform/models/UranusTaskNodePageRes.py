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


class UranusTaskNodePageRes(object):

    def __init__(self, taskCode=None, taskName=None, jobType=None, jobTypeDesc=None, jobChildType=None, jobChildTypeDesc=None, flowCode=None, flowName=None, manager=None, nodeName=None, nodeIcon=None, fileCode=None, nodeTypeName=None, taskNodeChangeResList=None, gravityStatus=None, gravityStatusDesc=None, createdTime=None, modifiedTime=None):
        """
        :param taskCode: (Optional) 节点Code
        :param taskName: (Optional) 节点名称
        :param jobType: (Optional) 作业类型
        :param jobTypeDesc: (Optional) 作业类型描述
        :param jobChildType: (Optional) 子节点类型
        :param jobChildTypeDesc: (Optional) 子节点类型描述
        :param flowCode: (Optional) 流程唯一code
        :param flowName: (Optional) 流程名称
        :param manager: (Optional) 负责人
        :param nodeName: (Optional) 节点名称
        :param nodeIcon: (Optional) 节点图标
        :param fileCode: (Optional) 文件code
        :param nodeTypeName: (Optional) 节点类型名称
        :param taskNodeChangeResList: (Optional) 发布变更状态
        :param gravityStatus: (Optional) 作业状态
        :param gravityStatusDesc: (Optional) 作业状态描述
        :param createdTime: (Optional) 创建时间
        :param modifiedTime: (Optional) 修改时间
        """

        self.taskCode = taskCode
        self.taskName = taskName
        self.jobType = jobType
        self.jobTypeDesc = jobTypeDesc
        self.jobChildType = jobChildType
        self.jobChildTypeDesc = jobChildTypeDesc
        self.flowCode = flowCode
        self.flowName = flowName
        self.manager = manager
        self.nodeName = nodeName
        self.nodeIcon = nodeIcon
        self.fileCode = fileCode
        self.nodeTypeName = nodeTypeName
        self.taskNodeChangeResList = taskNodeChangeResList
        self.gravityStatus = gravityStatus
        self.gravityStatusDesc = gravityStatusDesc
        self.createdTime = createdTime
        self.modifiedTime = modifiedTime
