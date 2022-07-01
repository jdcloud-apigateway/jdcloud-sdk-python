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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class UpdateTranscodeTemplateRequest(JDCloudRequest):
    """
    修改转码模板
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateTranscodeTemplateRequest, self).__init__(
            '/transcodeTemplates/{templateId}', 'PUT', header, version)
        self.parameters = parameters


class UpdateTranscodeTemplateParameters(object):

    def __init__(self, templateId,):
        """
        :param templateId: 模板ID
        """

        self.templateId = templateId
        self.name = None
        self.video = None
        self.audio = None
        self.encapsulation = None
        self.outFile = None
        self.definition = None
        self.templateType = None

    def setName(self, name):
        """
        :param name: (Optional) 模板名称。长度不超过128个字符。UTF-8编码。

        """
        self.name = name

    def setVideo(self, video):
        """
        :param video: (Optional) 视频参数配置
        """
        self.video = video

    def setAudio(self, audio):
        """
        :param audio: (Optional) 音频参数配置
        """
        self.audio = audio

    def setEncapsulation(self, encapsulation):
        """
        :param encapsulation: (Optional) 封装配置
        """
        self.encapsulation = encapsulation

    def setOutFile(self, outFile):
        """
        :param outFile: (Optional) 输出文件配置
        """
        self.outFile = outFile

    def setDefinition(self, definition):
        """
        :param definition: (Optional) 清晰度规格标记。取值范围：
  SD - 标清
  HD - 高清
  FHD - 超清
  2K
  4K

        """
        self.definition = definition

    def setTemplateType(self, templateType):
        """
        :param templateType: (Optional) 模板类型。取值范围：
  jdchd - 京享超清
  jdchs - 极速转码

        """
        self.templateType = templateType

