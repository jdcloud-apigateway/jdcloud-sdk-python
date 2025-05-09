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


class GpjmListJobInstanceReq(object):

    def __init__(self, pageSize, pageNum, statusList=None, enable=None, cycle=None, processType=None, manager=None, jobName=None, jobType=None, createTimeBefore=None, createTimeAfter=None, startTimeBefore=None, startTimeAfter=None, endTimeAfter=None, endTimeBefore=None, txDate=None, jobChildType=None, cstJobName=None):
        """
        :param pageSize:  页面大小
        :param pageNum:  页码
        :param statusList: (Optional) 运行状态
        :param enable: (Optional) 作业上上线下线状态
        :param cycle: (Optional) 运行周期
        :param processType: (Optional) 处理类型
        :param manager: (Optional) 负责人
        :param jobName: (Optional) 作业名
        :param jobType: (Optional) 任务类型
        :param createTimeBefore: (Optional) 任务创建日期-结束
        :param createTimeAfter: (Optional) 任务创建日期-开始
        :param startTimeBefore: (Optional) 运行开始时间范围
        :param startTimeAfter: (Optional) 运行开始时间范围
        :param endTimeAfter: (Optional) 运行结束时间范围
        :param endTimeBefore: (Optional) 运行结束时间范围
        :param txDate: (Optional) 数据日期
        :param jobChildType: (Optional) 
        :param cstJobName: (Optional) 客户作业名
        """

        self.pageSize = pageSize
        self.pageNum = pageNum
        self.statusList = statusList
        self.enable = enable
        self.cycle = cycle
        self.processType = processType
        self.manager = manager
        self.jobName = jobName
        self.jobType = jobType
        self.createTimeBefore = createTimeBefore
        self.createTimeAfter = createTimeAfter
        self.startTimeBefore = startTimeBefore
        self.startTimeAfter = startTimeAfter
        self.endTimeAfter = endTimeAfter
        self.endTimeBefore = endTimeBefore
        self.txDate = txDate
        self.jobChildType = jobChildType
        self.cstJobName = cstJobName
