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


class RerunTaskVo(object):

    def __init__(self, id=None, jobName=None, cstJobName=None, txDate=None, jobType=None, jobTypeLabel=None, status=None, statusLabel=None, detail=None, submitTime=None, cycle=None, cycleLabel=None, workspaceCode=None, companyCode=None):
        """
        :param id: (Optional) 任务id
        :param jobName: (Optional) 作业编码
        :param cstJobName: (Optional) 作业名称
        :param txDate: (Optional) 数据日期
        :param jobType: (Optional) 作业类型
        :param jobTypeLabel: (Optional) 作业类型-展示
        :param status: (Optional) 提交状态
        :param statusLabel: (Optional) 提交状态-展示
        :param detail: (Optional) 原因
        :param submitTime: (Optional) 提交时间
        :param cycle: (Optional) 运行频率
        :param cycleLabel: (Optional) 运行频率-展示
        :param workspaceCode: (Optional) 工作空间编码
        :param companyCode: (Optional) 租户编码
        """

        self.id = id
        self.jobName = jobName
        self.cstJobName = cstJobName
        self.txDate = txDate
        self.jobType = jobType
        self.jobTypeLabel = jobTypeLabel
        self.status = status
        self.statusLabel = statusLabel
        self.detail = detail
        self.submitTime = submitTime
        self.cycle = cycle
        self.cycleLabel = cycleLabel
        self.workspaceCode = workspaceCode
        self.companyCode = companyCode
