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


class GpjmRunRoleInfoDTO(object):

    def __init__(self, runTimeOut=None, triggerType=None, triggerTime=None, flagRetry=None, retryCount=None, retryInterval=None, cycle=None, sequence=None, sequenceInterval=None, sequenceStartTime=None, sequenceEndTime=None, priority=None, timeout=None, flagParallel=None, flagAcross=None, flagCascadedTrigger=None, cycleLabel=None, triggerTypeLabel=None):
        """
        :param runTimeOut: (Optional) 作业超时时间，单位分钟
        :param triggerType: (Optional) 触发类型:dependency 依赖、time 时间、file 文件、manual 手工、once 一次性
        :param triggerTime: (Optional) 触发时间
        :param flagRetry: (Optional) 是否重试过
        :param retryCount: (Optional) 重试次数
        :param retryInterval: (Optional) 间隔/秒
        :param cycle: (Optional) 运行周期 ,F 分钟、H 小时、D 天、W 周、M 月、O 一次性运行、N 无周期
        :param sequence: (Optional) 周期具体日期
        :param sequenceInterval: (Optional) 周期间隔
        :param sequenceStartTime: (Optional) 周期开始时间
        :param sequenceEndTime: (Optional) 周期结束时间
        :param priority: (Optional) 作业优先级
        :param timeout: (Optional) 作业超时时间，单位分钟
        :param flagParallel: (Optional) 是否可以并行运行
        :param flagAcross: (Optional) 是否可以跨周期运行
        :param flagCascadedTrigger: (Optional) 是否级联触发，父任务重跑后是否被强制触发重跑
        :param cycleLabel: (Optional) 运行周期
        :param triggerTypeLabel: (Optional) 触发类型
        """

        self.runTimeOut = runTimeOut
        self.triggerType = triggerType
        self.triggerTime = triggerTime
        self.flagRetry = flagRetry
        self.retryCount = retryCount
        self.retryInterval = retryInterval
        self.cycle = cycle
        self.sequence = sequence
        self.sequenceInterval = sequenceInterval
        self.sequenceStartTime = sequenceStartTime
        self.sequenceEndTime = sequenceEndTime
        self.priority = priority
        self.timeout = timeout
        self.flagParallel = flagParallel
        self.flagAcross = flagAcross
        self.flagCascadedTrigger = flagCascadedTrigger
        self.cycleLabel = cycleLabel
        self.triggerTypeLabel = triggerTypeLabel
