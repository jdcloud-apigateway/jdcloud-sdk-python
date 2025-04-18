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


class GpdpSchedTriggerDependTree(object):

    def __init__(self, id=None, jobName=None, dependName=None, jobBelong=None, flagParallel=None, necessary=None, dayOffset=None, dependJobBelong=None, enable=None, createTime=None, updateTime=None, cstJobName=None, lastStatus=None, lastTxDate=None, planExeTime=None, tableName=None, manager=None, jobDesc=None, display=None, lastStartTime=None, lastEndTime=None, parent=None, child=None, dependList=None):
        """
        :param id: (Optional) 
        :param jobName: (Optional) 
        :param dependName: (Optional) 
        :param jobBelong: (Optional) 作业所属系统，G gravity版本、A automation版本,废弃字段
        :param flagParallel: (Optional) 是否可以上下游并行，1启用、0关闭
        :param necessary: (Optional) 是否强依赖，1启用、0关闭
        :param dayOffset: (Optional) 依赖偏移量，0当天，-1昨天
        :param dependJobBelong: (Optional) 依赖作业所属系统，G gravity版本、A automation版本,废弃字段
        :param enable: (Optional) 是否启用，1启用、0关闭
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 更新时间
        :param cstJobName: (Optional) 客户作业名称
        :param lastStatus: (Optional) 最后状态
        :param lastTxDate: (Optional) 最后数据日期
        :param planExeTime: (Optional) 计划执行时间
        :param tableName: (Optional) 作业表名
        :param manager: (Optional) manager作业负责人
        :param jobDesc: (Optional) 作业描述
        :param display: (Optional) 显示信息
        :param lastStartTime: (Optional) 最后开始时间
        :param lastEndTime: (Optional) 最后结束时间
        :param parent: (Optional) 是否含有父类
        :param child: (Optional) 是否有子类
        :param dependList: (Optional) 依赖父作业清单
        """

        self.id = id
        self.jobName = jobName
        self.dependName = dependName
        self.jobBelong = jobBelong
        self.flagParallel = flagParallel
        self.necessary = necessary
        self.dayOffset = dayOffset
        self.dependJobBelong = dependJobBelong
        self.enable = enable
        self.createTime = createTime
        self.updateTime = updateTime
        self.cstJobName = cstJobName
        self.lastStatus = lastStatus
        self.lastTxDate = lastTxDate
        self.planExeTime = planExeTime
        self.tableName = tableName
        self.manager = manager
        self.jobDesc = jobDesc
        self.display = display
        self.lastStartTime = lastStartTime
        self.lastEndTime = lastEndTime
        self.parent = parent
        self.child = child
        self.dependList = dependList
