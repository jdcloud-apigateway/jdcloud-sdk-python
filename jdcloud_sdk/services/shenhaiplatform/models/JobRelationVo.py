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


class JobRelationVo(object):

    def __init__(self, jobName=None, cstJobName=None, lastTxDate=None, lastStartTime=None, lastEndTime=None, lastStatus=None, flagParallel=None, currentStatusMsg=None, sequenceStartTime=None, sequenceEndTime=None, sequenceInterval=None, enable=None, manager=None, jobBelong=None, necessary=None, depFlagParallel=None, triggerType=None, cycle=None, sequence=None):
        """
        :param jobName: (Optional) 作业名
        :param cstJobName: (Optional) 客户作业名称
        :param lastTxDate: (Optional) 最后以此执行日期
        :param lastStartTime: (Optional) 最后一次运行开始时间
        :param lastEndTime: (Optional) 最后一次结束时间
        :param lastStatus: (Optional) 最后一次运行状态，Pending、Ready、Running、Done、Failed、Clean
        :param flagParallel: (Optional) 是否可以自身并行，1启用、0关闭
        :param currentStatusMsg: (Optional) 当前作业状态信息
        :param sequenceStartTime: (Optional) 周期开始时间(适用小时分钟)
        :param sequenceEndTime: (Optional) 周期结束时间(适用小时分钟)
        :param sequenceInterval: (Optional) 周期间隔(适用小时分钟，当周期为小时，含义为间隔小时数，当周期为分钟，含义为间隔分钟数)
        :param enable: (Optional) 是否启用，1启用、0关闭
        :param manager: (Optional) 负责人，不超过10个
        :param jobBelong: (Optional) 作业所属系统，G gravity版本、A automation版本,用于迁移字段
        :param necessary: (Optional) 是否强依赖，1启用、0关闭
        :param depFlagParallel: (Optional) 是否可以上下游并行，1启用、0关闭
        :param triggerType: (Optional) 触发类型:dependency 依赖、time 时间、file 文件、manual 手工、once 一次性
        :param cycle: (Optional) 运行周期 ,F 分钟、H 小时、D 天、W 周、M 月、O 一次性运行、N 无周期
        :param sequence: (Optional) 周期具体日期
        """

        self.jobName = jobName
        self.cstJobName = cstJobName
        self.lastTxDate = lastTxDate
        self.lastStartTime = lastStartTime
        self.lastEndTime = lastEndTime
        self.lastStatus = lastStatus
        self.flagParallel = flagParallel
        self.currentStatusMsg = currentStatusMsg
        self.sequenceStartTime = sequenceStartTime
        self.sequenceEndTime = sequenceEndTime
        self.sequenceInterval = sequenceInterval
        self.enable = enable
        self.manager = manager
        self.jobBelong = jobBelong
        self.necessary = necessary
        self.depFlagParallel = depFlagParallel
        self.triggerType = triggerType
        self.cycle = cycle
        self.sequence = sequence
