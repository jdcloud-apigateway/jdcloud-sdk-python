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


class JobCommonInfoVo(object):

    def __init__(self, jobName=None, jobDesc=None, manager=None, shareUser=None, lastTxDate=None, lastStatus=None, currentStatusMsg=None, sequenceEndTime=None, sequenceInterval=None, sequenceStartTime=None, triggerType=None, jobId=None, processType=None, exeType=None, relationType=None, schedulerManagerFlag=None, managerFlag=None, cstJobName=None):
        """
        :param jobName: (Optional) 作业编码
        :param jobDesc: (Optional) 作业描述
        :param manager: (Optional) 负责人
        :param shareUser: (Optional) 协作人
        :param lastTxDate: (Optional) 最后运行数据日期
        :param lastStatus: (Optional) 最后运行状态
        :param currentStatusMsg: (Optional) 当前状态信息
        :param sequenceEndTime: (Optional) 小时分钟-结束时间
        :param sequenceInterval: (Optional) 小时分钟-间隔
        :param sequenceStartTime: (Optional) 小时分钟-开始时间
        :param triggerType: (Optional) 触发类型
        :param jobId: (Optional) 作业ID
        :param processType: (Optional) 处理类型
        :param exeType: (Optional) 执行类型
        :param relationType: (Optional) 关联类型
        :param schedulerManagerFlag: (Optional) 调度负责人标识
        :param managerFlag: (Optional) 负责人标识标志
        :param cstJobName: (Optional) 作业名称
        """

        self.jobName = jobName
        self.jobDesc = jobDesc
        self.manager = manager
        self.shareUser = shareUser
        self.lastTxDate = lastTxDate
        self.lastStatus = lastStatus
        self.currentStatusMsg = currentStatusMsg
        self.sequenceEndTime = sequenceEndTime
        self.sequenceInterval = sequenceInterval
        self.sequenceStartTime = sequenceStartTime
        self.triggerType = triggerType
        self.jobId = jobId
        self.processType = processType
        self.exeType = exeType
        self.relationType = relationType
        self.schedulerManagerFlag = schedulerManagerFlag
        self.managerFlag = managerFlag
        self.cstJobName = cstJobName
