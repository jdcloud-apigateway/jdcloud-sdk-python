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


class SpectrumApplication(object):

    def __init__(self, origin_direct=None, dns=None, proxy_protocol=None, edge_ips=None, modified_on=None, created_on=None, ip_firewall=None, protocol=None, id=None, origin_dns=None, origin_port=None, traffic_type=None):
        """
        :param origin_direct: (Optional) 请注意该值仅适用于TCP情况。
源站的地址列表。可以指定单个端口，例如，"tcp://192.0.2.1:1000"；或者一系列端口，例如，"tcp://192.0.2.1:1000-2000"
origin_direct中的端口与protocol中的端口必须遵循如下规则，
1.origin_direct中如果是单个端口，protocol中的端口可以是[1, 65535]的任意单值；
2.origin_direct中如果是端口范围，protocol中的端口也必须是范围，且范围区间必须相同。

        :param dns: (Optional) 
        :param proxy_protocol: (Optional) 请注意该值仅适用于TCP情况。
开启到源站的的代理协议。默认值off，有效值off/v1/v2。
TCP的有效值，off (默认)/v1/v2。
请注意源站也需要配置对应的协议和版本。

        :param edge_ips: (Optional) 
        :param modified_on: (Optional) 应用最近修改时间。
        :param created_on: (Optional) 应用创建时间。
        :param ip_firewall: (Optional) 请注意该值仅适用于TCP情况。开启IP访问规则。
        :param protocol: (Optional) 星盾Spectrum IP的端口配置。
对于 TCP 应用，您可以指定单个端口，例如，"tcp/1000"；或者一系列端口，例如，"tcp/1000-2000"。
protocol中的端口与origin_direct中的端口必须遵循如下规则，
1.protocol中如果是单个端口，origin_direct中的端口可以是[1, 65535]任意单值；
2.protocol中如果是端口范围，origin_direct中的端口也必须是范围，且范围区间必须相同。
对于 HTTP/HTTPS 应用，您仅可以指定单个端口，例如，"tcp/1000"。

        :param id: (Optional) 应用标识。
        :param origin_dns: (Optional) 
        :param origin_port: (Optional) 源站端口。与origin_dns成对使用。
        :param traffic_type: (Optional) 确定流量如何从边缘传输到源站。
当应用协议是”TCP“是，该值为"direct"，Spectrum会将流量直接发送到您的源站。
当应用协议是”HTTP“或”HTTPS“是，该值为”http“或”https“，Spectrum将应用星盾的HTTP/HTTPS功能，将流量发送到您的源站。
        """

        self.origin_direct = origin_direct
        self.dns = dns
        self.proxy_protocol = proxy_protocol
        self.edge_ips = edge_ips
        self.modified_on = modified_on
        self.created_on = created_on
        self.ip_firewall = ip_firewall
        self.protocol = protocol
        self.id = id
        self.origin_dns = origin_dns
        self.origin_port = origin_port
        self.traffic_type = traffic_type
