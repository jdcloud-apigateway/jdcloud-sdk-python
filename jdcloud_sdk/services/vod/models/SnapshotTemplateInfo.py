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


class SnapshotTemplateInfo(object):

    def __init__(self, templateId=None, templateName=None, snapshotType=None, imageSampleConfig=None, imageSpriteConfig=None, createTime=None, updateTime=None):
        """
        :param templateId: (Optional) 模板ID
        :param templateName: (Optional) 模板标题。长度不超过 128 个字节。UTF-8 编码。
        :param snapshotType: (Optional) 模板类型。取值范围：
  sample - 采样截图模板
  sprite - 雪碧图模板

        :param imageSampleConfig: (Optional) 采样截图模板配置
        :param imageSpriteConfig: (Optional) 雪碧图模板配置
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 修改时间
        """

        self.templateId = templateId
        self.templateName = templateName
        self.snapshotType = snapshotType
        self.imageSampleConfig = imageSampleConfig
        self.imageSpriteConfig = imageSpriteConfig
        self.createTime = createTime
        self.updateTime = updateTime
