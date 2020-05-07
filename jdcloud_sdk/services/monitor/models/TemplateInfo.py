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


class TemplateInfo(object):

    def __init__(self, createTime=None, deleted=None, description=None, name=None, params=None, templateAddr=None, templateType=None, templateUid=None, thumbnailAddr=None, updateTime=None):
        """
        :param createTime: (Optional) 
        :param deleted: (Optional) 是否删除，0否，1是
        :param description: (Optional) 描述
        :param name: (Optional) 名称
        :param params: (Optional) 模板参数信息
        :param templateAddr: (Optional) 模板oss地址
        :param templateType: (Optional) 类型，0为系统，1为自定义
        :param templateUid: (Optional) 唯一标识
        :param thumbnailAddr: (Optional) 模板缩略图oss地址
        :param updateTime: (Optional) 
        """

        self.createTime = createTime
        self.deleted = deleted
        self.description = description
        self.name = name
        self.params = params
        self.templateAddr = templateAddr
        self.templateType = templateType
        self.templateUid = templateUid
        self.thumbnailAddr = thumbnailAddr
        self.updateTime = updateTime