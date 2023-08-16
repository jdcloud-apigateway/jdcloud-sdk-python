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


class ModifyVpnConnectionSpec(object):

    def __init__(self, vpnConnectionName=None, description=None, bgpEnabled=None, trafficSelectors=None):
        """
        :param vpnConnectionName: (Optional) VPN连接的名称,只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符。
        :param description: (Optional) VPN连接的描述，允许输入UTF-8编码下的全部字符，不超过256字符。
        :param bgpEnabled: (Optional) “是否使用BGP路由，取值范围为：false（不使能）、true（使能）”
        :param trafficSelectors: (Optional) vpn connection policy，IPSec VPN的感兴趣流，用于第二阶段协商
        """

        self.vpnConnectionName = vpnConnectionName
        self.description = description
        self.bgpEnabled = bgpEnabled
        self.trafficSelectors = trafficSelectors
