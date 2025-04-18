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


class GpdjmcCalcJobResultDTO(object):

    def __init__(self, jobName=None, tableId=None, databaseName=None, workspaceCode=None, tableName=None, cstJobName=None, jobSystem=None, triggerType=None, triggerConfig=None, zipCommand=None, zipFileName=None, zipParams=None, dependencies=None, manager=None, cooperator=None, priority=None, jobDesc=None, scriptType=None, scriptTemplate=None, cycle=None, sequence=None, lifeCycle=None, retry=None, runTime=None, runDate=None, runTimeOut=None, scriptSourceType=None, startRunTime=None, endRunTime=None, runScript=None, notifyOccasion=None, notifyTime=None, notifyPattern=None, notifier=None, hasModel=None, scriptByte=None, version=None, core=None, channel=None, sequenceStartTime=None, sequenceEndTime=None, sequenceInterval=None, enable=None, runParams=None, submitConf=None, updateInfo=None):
        """
        :param jobName: (Optional) 作业名称
        :param tableId: (Optional) 表id
        :param databaseName: (Optional) 数据库名称
        :param workspaceCode: (Optional) 工作空间
        :param tableName: (Optional) 模型表名
        :param cstJobName: (Optional) 客户作业名称
        :param jobSystem: (Optional) 作业系统
        :param triggerType: (Optional) 任务类型(触发类型)
        :param triggerConfig: (Optional) 
        :param zipCommand: (Optional) zip命令行
        :param zipFileName: (Optional) zip名称
        :param zipParams: (Optional) zip参数
        :param dependencies: (Optional) 依赖任务列表
        :param manager: (Optional) 负责人
        :param cooperator: (Optional) 协作人
        :param priority: (Optional) 优先级
        :param jobDesc: (Optional) 任务描述
        :param scriptType: (Optional) 脚本类型
        :param scriptTemplate: (Optional) 脚本模板
        :param cycle: (Optional) 运行频率(运行周期)
        :param sequence: (Optional) 运行频率(运行周期内序列)
        :param lifeCycle: (Optional) 生命周期
        :param retry: (Optional) 失败后是否重试
        :param runTime: (Optional) 定时、一次任务（开始运行时间）
        :param runDate: (Optional) 定时、一次任务（开始运行时间）
        :param runTimeOut: (Optional) 超时时间
        :param scriptSourceType: (Optional) 脚本来源类型（本地或者git）
        :param startRunTime: (Optional) 开始运行时间
        :param endRunTime: (Optional) 结束运行时间
        :param runScript: (Optional) 运行脚本
        :param notifyOccasion: (Optional) 通知事件
        :param notifyTime: (Optional) 通知时间
        :param notifyPattern: (Optional) 通知模式
        :param notifier: (Optional) 通知者
        :param hasModel: (Optional) 是否拥有模型
        :param scriptByte: (Optional) 脚本文件字节数组,是将脚本文件内容转换为byte数组
        :param version: (Optional) 根据版本号，判断是重新发布还是新建，如果新建添加版本号，不是新建，更新历史表作业状态状态
        :param core: (Optional) 判断是否是运维中心调用编辑接口1，运维中心
        :param channel: (Optional) 数据渠道来源：新模型（MODEL），老模型（OLD_MODEL）、集成开发（IDE）、数据管道（PIPE）、数据质量（DQ）、AI(KUAI)
        :param sequenceStartTime: (Optional) 周期开始时间
        :param sequenceEndTime: (Optional) 周期结束时间
        :param sequenceInterval: (Optional) 时间间隔
        :param enable: (Optional) 启用状态
        :param runParams: (Optional) 脚本运行引擎  枚举值 "TEZ、MR、SPARK"
        :param submitConf: (Optional) 提交配置（仅HiveSQL在Spark引擎下支持指定）
        :param updateInfo: (Optional) 审计日志信息
        """

        self.jobName = jobName
        self.tableId = tableId
        self.databaseName = databaseName
        self.workspaceCode = workspaceCode
        self.tableName = tableName
        self.cstJobName = cstJobName
        self.jobSystem = jobSystem
        self.triggerType = triggerType
        self.triggerConfig = triggerConfig
        self.zipCommand = zipCommand
        self.zipFileName = zipFileName
        self.zipParams = zipParams
        self.dependencies = dependencies
        self.manager = manager
        self.cooperator = cooperator
        self.priority = priority
        self.jobDesc = jobDesc
        self.scriptType = scriptType
        self.scriptTemplate = scriptTemplate
        self.cycle = cycle
        self.sequence = sequence
        self.lifeCycle = lifeCycle
        self.retry = retry
        self.runTime = runTime
        self.runDate = runDate
        self.runTimeOut = runTimeOut
        self.scriptSourceType = scriptSourceType
        self.startRunTime = startRunTime
        self.endRunTime = endRunTime
        self.runScript = runScript
        self.notifyOccasion = notifyOccasion
        self.notifyTime = notifyTime
        self.notifyPattern = notifyPattern
        self.notifier = notifier
        self.hasModel = hasModel
        self.scriptByte = scriptByte
        self.version = version
        self.core = core
        self.channel = channel
        self.sequenceStartTime = sequenceStartTime
        self.sequenceEndTime = sequenceEndTime
        self.sequenceInterval = sequenceInterval
        self.enable = enable
        self.runParams = runParams
        self.submitConf = submitConf
        self.updateInfo = updateInfo
