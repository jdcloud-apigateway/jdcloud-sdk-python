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


class MediaClip(object):

    def __init__(self, mediaType, mediaId=None, mediaUrl=None, mediaIn=None, mediaOut=None, timelineIn=None, timelineOut=None, duration=None, posX=None, posY=None, content=None, font=None, fontSize=None, fontColor=None, fontColorOpacity=None, spacing=None, angle=None, borderStyle=None, outline=None, outlineColor=None, shadow=None, backColor=None, fontFace=None, operations=None):
        """
        :param mediaId: (Optional) 素材ID（素材类型为video或audio时适用）必须为视频点播媒资的视频ID。
一个Timeline中的所有MediaClip中，若有2个或以上的不同MediaId，即素材片段来源于2个或以上不同视频，则在提交剪辑作业时，必须在UserData中指明合并后的视频画面的宽高。
如 {\"extendData\": {\"width\": 720, \"height\": 500}}，其中width和height必须为[16, 4096]之间的偶数
* 素材类型为视频，音频时必填；文字和图片时必空。

        :param mediaType:  素材类型，必填。不同类型的轨类型，素材类型取值不同
* 视频轨目前支持的素材类型有：video，image
- video：视频
- image：图片
* 音频轨目前支持的素材类型有：audio
- audio：音频
* 文字轨目前支持的素材类型有：text
- text：文字

        :param mediaUrl: (Optional) 素材url（素材类型为image时适用）必填。京东对象存储的内网地址，图片资源公有读地址。

        :param mediaIn: (Optional) 素材片段在媒资中的入点（素材类型为video或audio时适用）单位：ms。默认为0。
        :param mediaOut: (Optional) 素材片段在媒资中的出点（素材类型为video或audio时适用）单位：ms。
        :param timelineIn: (Optional) 素材片段在合成时间线中的入点（素材类型为video、audio和text时适用）单位：ms。
* 如果为空，则会按照素材片段顺序相接的方式自动计算timelineIn。

        :param timelineOut: (Optional) 素材片段在合成时间线中的出点（素材类型为video、audio和text时适用）单位：ms。
* 如果为空，则会按照素材片段顺序相接的方式自动计算timelineOut = timelineIn + mediaDuration。
* 如果非空，有可能会导致timelineOut-timelineIn 与 mediaOut-mediaIn不符，最终会以timelineOut为准。

        :param duration: (Optional) 素材片段持续时长（素材类型为image时适用），单位:ms。
        :param posX: (Optional) X坐标（素材类型为video、audio和text时适用）：表示素材的左上角距离输出视频左上角的横向距离，单位：像素。
        :param posY: (Optional) Y坐标（素材类型为video、audio和text时适用）：表示素材的左上角距离输出视频左上角的纵向距离，单位：像素。
        :param content: (Optional) 文字内容（素材类型为text时适用）必填。
支持\n文字换行，比如："小明\n你好"。

        :param font: (Optional) 字体名称（素材类型为text时适用）
目前支持的字体有：FZHanZhen，FZShangKu，HYChaoJiZhanJia，HYLeMiao，HYNuoMi，HYYaKu，HYZhongXiu，JDLangZheng，SourceHanSans。默认为JDLangZheng:"京东朗正体"。
- JDLangZheng：京东朗正
- FZHanZhen：方正汉真
- FZShangKu：方正尚酷
- HYChaoJiZhanJia：汉仪机甲
- HYLeMiao：汉仪乐喵
- HYNuoMi：汉仪糯米
- HYYaKu：汉仪雅酷
- HYZhongXiu：汉仪中秀
- SourceHanSans：思源黑体

        :param fontSize: (Optional) 文字的字号（素材类型为text时适用）
        :param fontColor: (Optional) 字体颜色（素材类型为text时适用）。格式为#后跟16进制值。例如：#ffffff(RRGGBB)。
        :param fontColorOpacity: (Optional) 文字透明度（素材类型为text时适用）。当字幕类型为横幅文字时，表示文字的透明度，取值[0,1]，默认1。1为不透明，0为完全透明。
        :param spacing: (Optional) 文字间距（素材类型为text时适用）。表示横幅文字字间距。单位：像素，默认为0。
        :param angle: (Optional) 文字逆时针旋转角度（素材类型为text时适用）。表示横幅文字逆时针旋转角度。单位：度，默认为0。
        :param borderStyle: (Optional) 文字边框和阴影格式（素材类型为text时适用）。取值1或3，1=边框+阴影，3=不透明底框。默认为1。
        :param outline: (Optional) 描边宽度（素材类型为text时适用）。表示横幅文字描边宽度。单位：像素值，默认为0。
        :param outlineColor: (Optional) 描边颜色（素材类型为text时适用）。格式为#后跟16进制值。例如：#ffffff(RRGGBB)。
        :param shadow: (Optional) 文字投下阴影的深度（素材类型为text时适用）。表示横幅文字投下阴影的深度，单位：像素值，默认为0。
        :param backColor: (Optional) 阴影颜色（素材类型为text时适用）。格式为#后跟16进制值。例如：#ffffff(RRGGBB)。
        :param fontFace: (Optional) 字体样式（素材类型为text时适用）
        :param operations: (Optional) 
        """

        self.mediaId = mediaId
        self.mediaType = mediaType
        self.mediaUrl = mediaUrl
        self.mediaIn = mediaIn
        self.mediaOut = mediaOut
        self.timelineIn = timelineIn
        self.timelineOut = timelineOut
        self.duration = duration
        self.posX = posX
        self.posY = posY
        self.content = content
        self.font = font
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.fontColorOpacity = fontColorOpacity
        self.spacing = spacing
        self.angle = angle
        self.borderStyle = borderStyle
        self.outline = outline
        self.outlineColor = outlineColor
        self.shadow = shadow
        self.backColor = backColor
        self.fontFace = fontFace
        self.operations = operations
