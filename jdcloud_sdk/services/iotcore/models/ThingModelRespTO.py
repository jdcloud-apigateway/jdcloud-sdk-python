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


class ThingModelRespTO(object):

    def __init__(self, id=None, name=None, description=None, changeLog=None, content=None, createTime=None, latestPublish=None, publishStatus=None, publishTime=None, thingModelVersion=None, thingTypeCode=None, updateTime=None):
        """
        :param id: (Optional) 模型id
        :param name: (Optional) 物模型名称
        :param description: (Optional) 描述
        :param changeLog: (Optional) 变更日志
        :param content: (Optional) 详细内容
        :param createTime: (Optional) 创建时间
        :param latestPublish: (Optional) 是否为最新发布版本
        :param publishStatus: (Optional) 发布状态
        :param publishTime: (Optional) 发布时间
        :param thingModelVersion: (Optional) 物模型版本号
        :param thingTypeCode: (Optional) 物类型id
        :param updateTime: (Optional) 更新操作时间
        """

        self.id = id
        self.name = name
        self.description = description
        self.changeLog = changeLog
        self.content = content
        self.createTime = createTime
        self.latestPublish = latestPublish
        self.publishStatus = publishStatus
        self.publishTime = publishTime
        self.thingModelVersion = thingModelVersion
        self.thingTypeCode = thingTypeCode
        self.updateTime = updateTime
