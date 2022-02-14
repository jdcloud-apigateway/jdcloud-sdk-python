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


class UpdateCollectInfoSpec(object):

    def __init__(self, enabled, resourceType, agResource=None, filterEnabled=None, logCustomTarget=None, logCustomTargetConf=None, logFile=None, logFilters=None, logPath=None, logtopicEnabled=None, regexpStr=None, resourceMode=None, resources=None, tagResource=None):
        """
        :param agResource: (Optional) 高可用组资源
        :param enabled:  采集状态，0-禁用，1-启用
        :param filterEnabled: (Optional) 过滤器是否启用。当appcode为custom时必填
        :param logCustomTarget: (Optional) 自定义日志转发目的地, 只支持业务应用日志。支持类型："kafka"，"es"
        :param logCustomTargetConf: (Optional) 自定义日志转发目的地配置，KV 结构，具体配置参考 LogCustomTargetKafkaConf 和 LogCustomTargetEsConf
        :param logFile: (Optional) 日志文件名。当appcode为custom时为必填。日志文件名支持正则表达式。
        :param logFilters: (Optional) 过滤器。设置过滤器后可根据用户设定的关键词采集部分日志，如仅采集 Error 的日志。目前最大允许5个。
        :param logPath: (Optional) 日志路径。当appcode为custom时为必填。目前仅支持对 Linux 云主机上的日志进行采集，路径支持通配符“*”和“？”，文件路径应符合 Linux 的文件路径规则
        :param logtopicEnabled: (Optional) 目的地是否是日志服务logtopic，只支持业务应用日志
        :param regexpStr: (Optional) 首行正则
        :param resourceMode: (Optional) 采集资源时选择的模式，1.正常的选择实例模式（默认模式）；2.选择标签tag模式 3.选择高可用组ag模式
        :param resourceType:  采集实例类型, 只能是 all/part  当选择all时，传入的实例列表无效
        :param resources: (Optional) 采集实例列表（存在上限限制）
        :param tagResource: (Optional) 
        """

        self.agResource = agResource
        self.enabled = enabled
        self.filterEnabled = filterEnabled
        self.logCustomTarget = logCustomTarget
        self.logCustomTargetConf = logCustomTargetConf
        self.logFile = logFile
        self.logFilters = logFilters
        self.logPath = logPath
        self.logtopicEnabled = logtopicEnabled
        self.regexpStr = regexpStr
        self.resourceMode = resourceMode
        self.resourceType = resourceType
        self.resources = resources
        self.tagResource = tagResource
