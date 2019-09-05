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


class Video(object):

    def __init__(self, codec=None, bitrate=None, fps=None, width=None, height=None):
        """
        :param codec: (Optional) 视频编码。取值范围：h265、h264
        :param bitrate: (Optional) 视频码率。取值范围 [128、10000]，单位为 Kbps
        :param fps: (Optional) 视频帧率。取值范围为 [1、60]，单位为 fps
        :param width: (Optional) 视频输出宽度。取值范围 [128，4096] 整数。
当值为空时，若 height 也为空，则 width 和 height 与原视频保持一致；若 height 不为空，则 width 按照原视频的分辨率等比缩放。

        :param height: (Optional) 视频输出高度。取值范围 [128，4096] 整数。
当值为空时，若 width 也为空，则 width 和 height 与原视频保持一致；若 width 不为空，则 height 按照原视频的分辨率等比缩放。

        """

        self.codec = codec
        self.bitrate = bitrate
        self.fps = fps
        self.width = width
        self.height = height
