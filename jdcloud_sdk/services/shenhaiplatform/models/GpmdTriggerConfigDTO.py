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


class GpmdTriggerConfigDTO(object):

    def __init__(self, conditionType=None, secondaryType=None, serverDomain=None, serverPort=None, username=None, usernamePwd=None, protocol=None, databaseName=None, dataSource=None, object=None, conditionConfig=None, triggerTime=None, triggerInterval=None, beginTime=None, endTime=None):
        """
        :param conditionType: (Optional) 条件类型
        :param secondaryType: (Optional) 次要类型
        :param serverDomain: (Optional) 服务器域名
        :param serverPort: (Optional) 服务器端口
        :param username: (Optional) 用户名
        :param usernamePwd: (Optional) 用户密码
        :param protocol: (Optional) 协议
        :param databaseName: (Optional) 数据库名称
        :param dataSource: (Optional) 数据源
        :param object: (Optional) 对象信息
        :param conditionConfig: (Optional) 条件配置
        :param triggerTime: (Optional) 触发时间
        :param triggerInterval: (Optional) 触发间隔
        :param beginTime: (Optional) 开始时间
        :param endTime: (Optional) 结束时间
        """

        self.conditionType = conditionType
        self.secondaryType = secondaryType
        self.serverDomain = serverDomain
        self.serverPort = serverPort
        self.username = username
        self.usernamePwd = usernamePwd
        self.protocol = protocol
        self.databaseName = databaseName
        self.dataSource = dataSource
        self.object = object
        self.conditionConfig = conditionConfig
        self.triggerTime = triggerTime
        self.triggerInterval = triggerInterval
        self.beginTime = beginTime
        self.endTime = endTime
