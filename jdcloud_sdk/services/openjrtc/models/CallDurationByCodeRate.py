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


class CallDurationByCodeRate(object):

    def __init__(self, appId=None, date=None, audio=None, lte_480=None, gt_480_lte_720=None, gte_720=None):
        """
        :param appId: (Optional) 应用ID
        :param date: (Optional) 时间戳毫秒
        :param audio: (Optional) 音频通讯时长-second
        :param lte_480: (Optional) (0,480p]通讯时长-second
        :param gt_480_lte_720: (Optional) (480p,720p]通讯时长-second
        :param gte_720: (Optional) (720p,1080p]通讯时长-second
        """

        self.appId = appId
        self.date = date
        self.audio = audio
        self.lte_480 = lte_480
        self.gt_480_lte_720 = gt_480_lte_720
        self.gte_720 = gte_720
