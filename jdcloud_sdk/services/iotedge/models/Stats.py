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


class Stats(object):

    def __init__(self, devices=None, activatedDevices=None, onlineDevices=None, monthMessages=None, monthDuration=None, products=None):
        """
        :param devices: (Optional) 用户的设备数
        :param activatedDevices: (Optional) 已激活的设备数
        :param onlineDevices: (Optional) 在线的设备数
        :param monthMessages: (Optional) 当月消息数
        :param monthDuration: (Optional) 当月设备在线时长
        :param products: (Optional) 产品数
        """

        self.devices = devices
        self.activatedDevices = activatedDevices
        self.onlineDevices = onlineDevices
        self.monthMessages = monthMessages
        self.monthDuration = monthDuration
        self.products = products