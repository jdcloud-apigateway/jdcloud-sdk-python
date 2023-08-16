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


class BgwRoute(object):

    def __init__(self, bgwRouteId=None, bgwId=None, bgwRouteDestination=None, bgwRouteNexthop=None, origin=None, bgwRoutePriority=None, bgwRouteNextHopType=None, description=None):
        """
        :param bgwRouteId: (Optional) Bgw上路由的Id
        :param bgwId: (Optional) bgw的Id
        :param bgwRouteDestination: (Optional) Bgw上路由的目的地址,格式如：172.10.2.15/16，参见RFC 4632
        :param bgwRouteNexthop: (Optional) Bgw上路由的下一跳设备资源Id,目前支持托管通道Id，专线通道Id,vpc接口Id和vpn连接Id
        :param origin: (Optional) Bgw上的路由是静态的还是传播的:static,propagated
        :param bgwRoutePriority: (Optional) Bgw上路由的优先级
        :param bgwRouteNextHopType: (Optional) Bgw上路由的下一跳类型：目前支持privateVif（专线网关）、hostedPrivateVif（托管网关）、vpcAttachment（vpc接口）、vpnConnection(vpn连接)
        :param description: (Optional) Bgw路由的描述
        """

        self.bgwRouteId = bgwRouteId
        self.bgwId = bgwId
        self.bgwRouteDestination = bgwRouteDestination
        self.bgwRouteNexthop = bgwRouteNexthop
        self.origin = origin
        self.bgwRoutePriority = bgwRoutePriority
        self.bgwRouteNextHopType = bgwRouteNextHopType
        self.description = description
