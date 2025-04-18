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


class JobRunHistoryVo(object):

    def __init__(self, etlJob=None, txDate=None, startTime=None, endTime=None, jobStatus=None, jobSessionId=None, runTime=None, returnCode=None, returnMsg=None, createTime=None, isComplement=None, planExecTime=None, applicationId=None):
        """
        :param etlJob: (Optional) 作业名
        :param txDate: (Optional) 数据日期
        :param startTime: (Optional) 运行开始时间
        :param endTime: (Optional) 运行结束时间
        :param jobStatus: (Optional) 运行状态
        :param jobSessionId: (Optional) Session ID
        :param runTime: (Optional) 运行时间
        :param returnCode: (Optional) 返回编码
        :param returnMsg: (Optional) 返回信息
        :param createTime: (Optional) 创建时间
        :param isComplement: (Optional) 是否补数任务
        :param planExecTime: (Optional) 计划执行时间
        :param applicationId: (Optional) 云仓调度作业id
        """

        self.etlJob = etlJob
        self.txDate = txDate
        self.startTime = startTime
        self.endTime = endTime
        self.jobStatus = jobStatus
        self.jobSessionId = jobSessionId
        self.runTime = runTime
        self.returnCode = returnCode
        self.returnMsg = returnMsg
        self.createTime = createTime
        self.isComplement = isComplement
        self.planExecTime = planExecTime
        self.applicationId = applicationId
