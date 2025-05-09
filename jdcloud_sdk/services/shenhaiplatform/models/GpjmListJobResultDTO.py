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


class GpjmListJobResultDTO(object):

    def __init__(self, id=None, etlJob=None, processType=None, exeType=None, etlServer=None, description=None, frequency=None, lastStartTime=None, lastEndTime=None, runTime=None, lastJobStatus=None, lastTxDate=None, lastReturnCode=None, currentStatusMsg=None, enable=None, jobSessionID=None, expireTime=None, triggerType=None, triggerTime=None, cycle=None, sequence=None, priority=None, createUser=None, userName=None, retryCount=None, sequenceStartTime=None, sequenceEndTime=None, sequenceInterval=None, flagRetry=None, createTime=None, updateTime=None, cycleLabel=None, triggerTypeLabel=None, processTypeCn=None, channel=None, jobType=None, managerFlag=None, jobChildType=None, cstJobName=None):
        """
        :param id: (Optional) 作业id
        :param etlJob: (Optional) 作业名称
        :param processType: (Optional) 处理类型（calc：数据计算，extract：数据抽取，ods：ODS加工，load：数据推送，hdfs：数据同步,dqim:质量作业）
        :param exeType: (Optional) 作业执行类型
        :param etlServer: (Optional) 最后一次运行服务器
        :param description: (Optional) 作业描述
        :param frequency: (Optional) 周期具体日期
        :param lastStartTime: (Optional) 最后一次运行开始时间
        :param lastEndTime: (Optional) 最后一次运行结束时间
        :param runTime: (Optional) 运行时间
        :param lastJobStatus: (Optional) 最后一次运行状态
        :param lastTxDate: (Optional) 最后一次执行日期
        :param lastReturnCode: (Optional) 最后返回编码
        :param currentStatusMsg: (Optional) 当前作业状态信息
        :param enable: (Optional) 是否启用，0未上线、1已上线、2已下线
        :param jobSessionID: (Optional) Session ID
        :param expireTime: (Optional) 失效时间
        :param triggerType: (Optional) 触发类型:dependency 依赖、time 时间、file 文件、manual 手工、once 一次性
        :param triggerTime: (Optional) 触发时间
        :param cycle: (Optional) 运行周期 ,F 分钟、H 小时、D 天、W 周、M 月、O 一次性运行、N 无周期
        :param sequence: (Optional) 周期具体日期
        :param priority: (Optional) 作业优先级，数字越小优先级越高
        :param createUser: (Optional) 创建人
        :param userName: (Optional) 负责人，不超过10个
        :param retryCount: (Optional) 重试次数
        :param sequenceStartTime: (Optional) 周期开始时间(适用小时分钟)
        :param sequenceEndTime: (Optional) 周期结束时间(适用小时分钟)
        :param sequenceInterval: (Optional) 周期间隔(适用小时分钟，当周期为小时，含义为间隔小时数，当周期为分钟，含义为间隔分钟数)
        :param flagRetry: (Optional) 是否重试过
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 更新时间
        :param cycleLabel: (Optional) 周期中文名 ,F 分钟、H 小时、D 天、W 周、M 月、O 一次性运行、N 无周期
        :param triggerTypeLabel: (Optional) 触发方式中文名:dependency 依赖、time 时间、file 文件、manual 手工、once 一次性
        :param processTypeCn: (Optional) 处理类型中文名（数据计算，数据抽取，ODS加工，数据推送，数据同步, 质量作业）
        :param channel: (Optional) 数据来源渠道，集成开发（IDE）、数据管道（PIPE）
        :param jobType: (Optional) 任务类型
        :param managerFlag: (Optional) 是否为作业管理员或者工作空间管理员
        :param jobChildType: (Optional) 
        :param cstJobName: (Optional) 客户作业名
        """

        self.id = id
        self.etlJob = etlJob
        self.processType = processType
        self.exeType = exeType
        self.etlServer = etlServer
        self.description = description
        self.frequency = frequency
        self.lastStartTime = lastStartTime
        self.lastEndTime = lastEndTime
        self.runTime = runTime
        self.lastJobStatus = lastJobStatus
        self.lastTxDate = lastTxDate
        self.lastReturnCode = lastReturnCode
        self.currentStatusMsg = currentStatusMsg
        self.enable = enable
        self.jobSessionID = jobSessionID
        self.expireTime = expireTime
        self.triggerType = triggerType
        self.triggerTime = triggerTime
        self.cycle = cycle
        self.sequence = sequence
        self.priority = priority
        self.createUser = createUser
        self.userName = userName
        self.retryCount = retryCount
        self.sequenceStartTime = sequenceStartTime
        self.sequenceEndTime = sequenceEndTime
        self.sequenceInterval = sequenceInterval
        self.flagRetry = flagRetry
        self.createTime = createTime
        self.updateTime = updateTime
        self.cycleLabel = cycleLabel
        self.triggerTypeLabel = triggerTypeLabel
        self.processTypeCn = processTypeCn
        self.channel = channel
        self.jobType = jobType
        self.managerFlag = managerFlag
        self.jobChildType = jobChildType
        self.cstJobName = cstJobName
