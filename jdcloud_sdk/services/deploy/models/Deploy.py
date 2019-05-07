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


class Deploy(object):

    def __init__(self, deployId=None, appId=None, appName=None, groupId=None, groupName=None, regionId=None, startTime=None, endTime=None, deployStatus=None, desc=None, deployMethod=None, deploySource=None, deployCmd=None, cmdSource=None, cmdType=None, productType=None, downloadUrl=None, md5=None, compileProject=None, compileSeries=None, ossSpace=None, ossDir=None, fileType=None, rollbackAble=None, concurrencyUnit=None, concurrencyNum=None, concurrencyPct=None, lbStatus=None, lbInstance=None, lbBackend=None, repeatPolicy=None, noticeTrigger=None, noticeMethod=None, jdsfEnabled=None):
        """
        :param deployId: (Optional) 上线单ID
        :param appId: (Optional) 应用ID
        :param appName: (Optional) 应用名称
        :param groupId: (Optional) 部署组名称
        :param groupName: (Optional) 部署组ID
        :param regionId: (Optional) 地域
        :param startTime: (Optional) 部署开始时间
        :param endTime: (Optional) 部署结束时间
        :param deployStatus: (Optional) 部署状态 0待部署, 1部署中, 2成功, 3失败, 4回滚中， 5回滚成功， 6回滚失败， 7已取消
        :param desc: (Optional) 描述
        :param deployMethod: (Optional) 部署方式：1滚动部署，2蓝绿部署
        :param deploySource: (Optional) 部署来源：1url，2云编译，3云存储
        :param deployCmd: (Optional) 部署操作
        :param cmdSource: (Optional) 1使用输入的操作，2使用程序自带操作
        :param cmdType: (Optional) 部署操作展示格式：1form,2ymal
        :param productType: (Optional) 项目类型 1tomcat,2
        :param downloadUrl: (Optional) 下载url
        :param md5: (Optional) md5
        :param compileProject: (Optional) 云编译项目名
        :param compileSeries: (Optional) 云编译构建序号
        :param ossSpace: (Optional) 云存储空间
        :param ossDir: (Optional) 云存储目录
        :param fileType: (Optional) 文件类型：1.tar，2.zio,3.tar.gz
        :param rollbackAble: (Optional) 是否可回滚 1是，2否
        :param concurrencyUnit: (Optional) 并发单位
        :param concurrencyNum: (Optional) 并发机器数
        :param concurrencyPct: (Optional) 并发度
        :param lbStatus: (Optional) 负载均衡：1启动，2禁用
        :param lbInstance: (Optional) lb实例
        :param lbBackend: (Optional) lb 后端实例
        :param repeatPolicy: (Optional) 同名文件处理方式：1部署失败，2覆盖，3保留
        :param noticeTrigger: (Optional) 通知频率：1异常发送，2每次发送
        :param noticeMethod: (Optional) 通知方式：1消息，2邮件，3短信
        :param jdsfEnabled: (Optional) 使用分布式服务框架：0不使用，1使用
        """

        self.deployId = deployId
        self.appId = appId
        self.appName = appName
        self.groupId = groupId
        self.groupName = groupName
        self.regionId = regionId
        self.startTime = startTime
        self.endTime = endTime
        self.deployStatus = deployStatus
        self.desc = desc
        self.deployMethod = deployMethod
        self.deploySource = deploySource
        self.deployCmd = deployCmd
        self.cmdSource = cmdSource
        self.cmdType = cmdType
        self.productType = productType
        self.downloadUrl = downloadUrl
        self.md5 = md5
        self.compileProject = compileProject
        self.compileSeries = compileSeries
        self.ossSpace = ossSpace
        self.ossDir = ossDir
        self.fileType = fileType
        self.rollbackAble = rollbackAble
        self.concurrencyUnit = concurrencyUnit
        self.concurrencyNum = concurrencyNum
        self.concurrencyPct = concurrencyPct
        self.lbStatus = lbStatus
        self.lbInstance = lbInstance
        self.lbBackend = lbBackend
        self.repeatPolicy = repeatPolicy
        self.noticeTrigger = noticeTrigger
        self.noticeMethod = noticeMethod
        self.jdsfEnabled = jdsfEnabled