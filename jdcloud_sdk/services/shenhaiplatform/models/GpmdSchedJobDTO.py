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


class GpmdSchedJobDTO(object):

    def __init__(self, jobName=None, jobSystem=None, jobDesc=None, lastStatus=None, lastTxDate=None, lastStartTime=None, lastEndTime=None, lastServer=None, lastSessionid=None, lastReturnCode=None, currentStatusMsg=None, triggerType=None, cycle=None, sequence=None, txDateOffset=None, priority=None, timeout=None, windowStartTime=None, windowEndTime=None, morrowAutoExec=None, dataZeroKillEnable=None, retryCount=None, retryInterval=None, flagAgain=None, flagAcross=None, flagParallel=None, flagCascadedTrigger=None, nsName=None, serverResourVal=None, runServers=None, requiredRunEnv=None, runScript=None, enable=None, manager=None, shareUser=None, expireTime=None, commands=None, createUser=None, createTime=None, updateTime=None, nodeName=None, topic=None, jobRunWay=None, runParams=None, belongSys=None, sequenceStartTime=None, sequenceEndTime=None, sequenceInterval=None, startTime=None, planExecTime=None, msDelayDealWay=None):
        """
        :param jobName: (Optional) 作业名称
        :param jobSystem: (Optional) 老作业兼容字段
        :param jobDesc: (Optional) 作业描述
        :param lastStatus: (Optional) 最后一次运行状态，Pending、Ready、Running、Done、Failed、Clean
        :param lastTxDate: (Optional) 最后依次执行日期
        :param lastStartTime: (Optional) 最后一次运行开始时间
        :param lastEndTime: (Optional) 最后一次运行结束时间
        :param lastServer: (Optional) 最后一次运行服务器
        :param lastSessionid: (Optional) Session ID
        :param lastReturnCode: (Optional) 最后返回编码
        :param currentStatusMsg: (Optional) 当前作业状态信息
        :param triggerType: (Optional) 触发类型:dependency 依赖、time 时间、file 文件、manual 手工、once 一次性
        :param cycle: (Optional) 运行周期 ,D 天、W 周、M 月、O 一次性运行、N 无周期
        :param sequence: (Optional) 周期具体日期
        :param txDateOffset: (Optional) T+N，偏移量
        :param priority: (Optional) 作业优先级，数字越小优先级越高
        :param timeout: (Optional) 作业超时时间，单位分钟
        :param windowStartTime: (Optional) 窗口期开始时间
        :param windowEndTime: (Optional) 窗口期结束时间
        :param morrowAutoExec: (Optional) 失败后次日是否自动运行，1是、0否
        :param dataZeroKillEnable: (Optional) 抽空之后的处理 0 无操作 1 作业失败 2发出警告
        :param retryCount: (Optional) 重试次数
        :param retryInterval: (Optional) 间隔/秒
        :param flagAgain: (Optional) 当期已经跑成功过，是否可以再跑，1启用、0关闭
        :param flagAcross: (Optional) 是否可以跨周期跑，1启用、0关闭
        :param flagParallel: (Optional) 是否可以自身并行，1启用、0关闭
        :param flagCascadedTrigger: (Optional) 是否级联触发，父任务重跑后是否被强制触发重跑，1是、0否
        :param nsName: (Optional) 命名空间名称
        :param serverResourVal: (Optional) 服务器资源消耗值
        :param runServers: (Optional) 指定运行服务器
        :param requiredRunEnv: (Optional) 需要的运行环境
        :param runScript: (Optional) 运行脚本
        :param enable: (Optional) 是否启用，0未上线、1已上线、2已下线
        :param manager: (Optional) 负责人，不超过10个
        :param shareUser: (Optional) 共享人，不超过10个
        :param expireTime: (Optional) 失效时间
        :param commands: (Optional) zip命令行
        :param createUser: (Optional) 创建人
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 更新时间
        :param nodeName: (Optional) 实时结点名称
        :param topic: (Optional) 实时主题
        :param jobRunWay: (Optional) 作业执行方式  0离线 1双写 2实时
        :param runParams: (Optional) 作业运行参数
        :param belongSys: (Optional) 所属系统
        :param sequenceStartTime: (Optional) 周期开始时间
        :param sequenceEndTime: (Optional) 周期结束时间
        :param sequenceInterval: (Optional) 周期间隔
        :param startTime: (Optional) 开始时间
        :param planExecTime: (Optional) 计划执行时间
        :param msDelayDealWay: (Optional) 主从同步延迟处理方式。0:警告无处理，1:作业延迟启动
        """

        self.jobName = jobName
        self.jobSystem = jobSystem
        self.jobDesc = jobDesc
        self.lastStatus = lastStatus
        self.lastTxDate = lastTxDate
        self.lastStartTime = lastStartTime
        self.lastEndTime = lastEndTime
        self.lastServer = lastServer
        self.lastSessionid = lastSessionid
        self.lastReturnCode = lastReturnCode
        self.currentStatusMsg = currentStatusMsg
        self.triggerType = triggerType
        self.cycle = cycle
        self.sequence = sequence
        self.txDateOffset = txDateOffset
        self.priority = priority
        self.timeout = timeout
        self.windowStartTime = windowStartTime
        self.windowEndTime = windowEndTime
        self.morrowAutoExec = morrowAutoExec
        self.dataZeroKillEnable = dataZeroKillEnable
        self.retryCount = retryCount
        self.retryInterval = retryInterval
        self.flagAgain = flagAgain
        self.flagAcross = flagAcross
        self.flagParallel = flagParallel
        self.flagCascadedTrigger = flagCascadedTrigger
        self.nsName = nsName
        self.serverResourVal = serverResourVal
        self.runServers = runServers
        self.requiredRunEnv = requiredRunEnv
        self.runScript = runScript
        self.enable = enable
        self.manager = manager
        self.shareUser = shareUser
        self.expireTime = expireTime
        self.commands = commands
        self.createUser = createUser
        self.createTime = createTime
        self.updateTime = updateTime
        self.nodeName = nodeName
        self.topic = topic
        self.jobRunWay = jobRunWay
        self.runParams = runParams
        self.belongSys = belongSys
        self.sequenceStartTime = sequenceStartTime
        self.sequenceEndTime = sequenceEndTime
        self.sequenceInterval = sequenceInterval
        self.startTime = startTime
        self.planExecTime = planExecTime
        self.msDelayDealWay = msDelayDealWay
