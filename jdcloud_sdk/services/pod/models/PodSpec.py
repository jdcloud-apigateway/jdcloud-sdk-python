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


class PodSpec(object):

    def __init__(self, name, instanceType, az, containers, primaryNetworkInterface, description=None, hostname=None, restartPolicy=None, terminationGracePeriodSeconds=None, dnsConfig=None, logConfig=None, hostAliases=None, volumes=None, charge=None, elasticIp=None):
        """
        :param name:  Pod名称
        :param description: (Optional) 描述信息，默认为空；允许输入UTF-8编码下的全部字符，不超过256字符。
        :param hostname: (Optional) 主机名；范围：[1-63]个ASCII字符，默认值为 podId
        :param restartPolicy: (Optional) pod中容器重启策略；Always, OnFailure, Never；默认：Always
        :param terminationGracePeriodSeconds: (Optional) 优雅关机宽限时长，如果超时，则触发强制关机。默认：30s，值不能是负数，范围：[0-300]
        :param instanceType:  实例类型；参考[文档](https://www.jdcloud.com/help/detail/1992/isCatalog/1)
        :param az:  容器所属可用区
        :param dnsConfig: (Optional) pod内容器的/etc/resolv.conf配置
        :param logConfig: (Optional) 容器日志配置信息；默认会在本地分配10MB的存储空间
        :param hostAliases: (Optional) 域名和IP映射的信息；</br> 最大10个alias
        :param volumes: (Optional) 域名和IP映射的信息；</br> 最大10个alias
        :param containers:  域名和IP映射的信息；</br> 最大10个alias
        :param charge: (Optional) 预付费（prepaid_by_duration）, 按配置后付费（postpaid_by_duration）。默认：按配置后付费
        :param elasticIp: (Optional) 主网卡主IP关联的弹性IP规格
        :param primaryNetworkInterface:  主网卡配置信息
        """

        self.name = name
        self.description = description
        self.hostname = hostname
        self.restartPolicy = restartPolicy
        self.terminationGracePeriodSeconds = terminationGracePeriodSeconds
        self.instanceType = instanceType
        self.az = az
        self.dnsConfig = dnsConfig
        self.logConfig = logConfig
        self.hostAliases = hostAliases
        self.volumes = volumes
        self.containers = containers
        self.charge = charge
        self.elasticIp = elasticIp
        self.primaryNetworkInterface = primaryNetworkInterface
