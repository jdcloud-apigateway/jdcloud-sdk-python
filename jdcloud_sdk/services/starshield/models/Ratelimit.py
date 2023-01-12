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


class Ratelimit(object):

    def __init__(self, characteristics=None, requests_per_period=None, period=None, mitigation_timeout=None, requests_to_origin=None, counting_expression=None):
        """
        :param characteristics: (Optional) 使用以下一个或多个特征：
UI值==============API值
(隐式包含)---------cf.colo.id(强制性的)
IP---------------ip.src
Cookie-----------http.request.cookies["<cookie_name>"]
标头--------------http.request.headers["<header_name>"]
查询--------------http.request.uri.args["<query_param_name>"]
支持NAT的IP-------cf.unique_visitor_id
ASN--------------ip.geoip.asnum
国家/地区----------ip.geoip.country
JA3指纹-----------cf.bot_management.ja3_hash

最多使用5个特征。
'IP'和'支持NAT的IP'不能同时使用。
如果你使用http.request.headers["<header_name>"]，<header_name>必须是小写，因为星盾在边缘规范化了标头名称。

        :param requests_per_period: (Optional) 在一段时间内触发规则的请求数。
        :param period: (Optional) 评估请求速率时要考虑的时间段（以秒为单位）。
有效值10/60/120/300/600/3600，即10, 60 (1分钟), 120 (2分钟), 300 (5分钟), 600 (10分钟), or 3600 (1小时)。

        :param mitigation_timeout: (Optional) 一旦达到速率，速率限制规则将在该时间段内（以秒为单位）生效。
使用质询操作之一时，无法定义持续时间。在这种情况下，当访问者通过质询时，其相应的请求计数器设置为零。当规则特征值相同的访问者发出足够的请求再次触发限速规则时，他们将收到新的质询。
有效值30/60/600/3600/86400，即30, 60 (1分钟), 600 (10分钟), 3600 (1小时), or 86400 (1天)。
当action的值为managed_challenge/js_challenge/challenge时，你必须设置mitigation_timeout的值为0。

        :param requests_to_origin: (Optional) true代表,在确定请求速率时，只考虑发往源站的请求（即未缓存的请求）。
        :param counting_expression: (Optional) 定义用于确定请求速率的标准。默认情况下，计数表达式与规则表达式相同。将此字段设置为空字符串（“”）时，也会应用默认值。
计数表达式可以包括HTTP响应字段。当计数表达式中有响应字段时，计数将在发送响应后进行。
        """

        self.characteristics = characteristics
        self.requests_per_period = requests_per_period
        self.period = period
        self.mitigation_timeout = mitigation_timeout
        self.requests_to_origin = requests_to_origin
        self.counting_expression = counting_expression
