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


class CreateWatermarkRequest(JDCloudRequest):
    """
    添加水印
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateWatermarkRequest, self).__init__(
            '/watermarks', 'POST', header, version)
        self.parameters = parameters


class CreateWatermarkParameters(object):

    def __init__(self, name, imgUrl, width, height, position, offsetX, offsetY):
        """
        :param name: 水印名称
        :param imgUrl: 图片地址
        :param width: 水印宽度
        :param height: 水印高度
        :param position: 水印位置。取值范围：
  LT - 左上
  RT - 右上
  LB - 左下
  RB - 右下

        :param offsetX: 水平偏移
        :param offsetY: 竖直偏移
        """

        self.name = name
        self.imgUrl = imgUrl
        self.width = width
        self.height = height
        self.position = position
        self.unit = None
        self.offsetX = offsetX
        self.offsetY = offsetY

    def setUnit(self, unit):
        """
        :param unit: (Optional) 偏移单位
        """
        self.unit = unit

