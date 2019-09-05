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


class UpdateWatermarkRequestObject(object):

    def __init__(self, name=None, imgUrl=None, width=None, height=None, sizeUnit=None, position=None, offsetX=None, offsetY=None, offsetUnit=None):
        """
        :param name: (Optional) 水印名称。只支持中英文、数字。长度不超过128个字符。UTF-8编码。

        :param imgUrl: (Optional) 图片地址
        :param width: (Optional) 水印宽度。
当 sizeUnit = pixel 时，取值范围为 [8, 4096] 整数
当 sizeUnit = percent 时，取值范围为 [0, 100] 小数

        :param height: (Optional) 水印高度。
当 sizeUnit = pixel 时，取值范围为 [8, 4096] 整数
当 sizeUnit = percent 时，取值范围为 [0, 100] 小数

        :param sizeUnit: (Optional) 尺寸单位。取值范围：
  pixel - 像素
  percent - 百分比
默认值为 pixel

        :param position: (Optional) 水印位置。取值范围：
  LT - 左上
  RT - 右上
  LB - 左下
  RB - 右下

        :param offsetX: (Optional) 水平偏移。
当 offsetUnit = pixel 时，取值范围为 [8, 4088] 整数
当 offsetUnit = percent 时，取值范围为 [0, 100] 小数

        :param offsetY: (Optional) 竖直偏移。
当 offsetUnit = pixel 时，取值范围为 [8, 4088] 整数
当 offsetUnit = percent 时，取值范围为 [0, 100] 小数

        :param offsetUnit: (Optional) 偏移单位。取值范围：
  pixel - 像素
  percent - 百分比
默认值为 pixel

        """

        self.name = name
        self.imgUrl = imgUrl
        self.width = width
        self.height = height
        self.sizeUnit = sizeUnit
        self.position = position
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.offsetUnit = offsetUnit
