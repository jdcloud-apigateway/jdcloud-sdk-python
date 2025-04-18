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


class GpdrAfreshAddLogVo(object):

    def __init__(self, id=None, etlJob=None, cstJobName=None, taskId=None, txDate=None, planExeTime=None, jobStatus=None, startTime=None, endTime=None, afreshAddId=None):
        """
        :param id: (Optional) 查询补数跟踪记录id
        :param etlJob: (Optional) 作业名
        :param cstJobName: (Optional) 客户作业名称
        :param taskId: (Optional) 补数任务ID
        :param txDate: (Optional) 数据日期
        :param planExeTime: (Optional) 计划执行时间
        :param jobStatus: (Optional) 任务状态
        :param startTime: (Optional) 任务开始运行时间
        :param endTime: (Optional) 任务开始运行时间
        :param afreshAddId: (Optional) 补数任务ID
        """

        self.id = id
        self.etlJob = etlJob
        self.cstJobName = cstJobName
        self.taskId = taskId
        self.txDate = txDate
        self.planExeTime = planExeTime
        self.jobStatus = jobStatus
        self.startTime = startTime
        self.endTime = endTime
        self.afreshAddId = afreshAddId
