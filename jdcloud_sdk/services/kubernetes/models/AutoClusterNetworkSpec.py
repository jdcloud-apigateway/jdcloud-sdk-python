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


class AutoClusterNetworkSpec(object):

    def __init__(self, publicApiServer, masterCidr, nodeNetworkCidr, vpcId, dualStack=None, masterNatEnabled=None, natGateway=None, nodeElasticIpSpec=None):
        """
        :param publicApiServer:  kube-apiserver是否可公网访问，false则kube-apiserver不绑定公网地址，true绑定公网地址
        :param masterCidr:  master网络的cidr
        :param nodeNetworkCidr:  node网络的cidr，自动切分
        :param vpcId:  用户侧承载node和pod的vpc id
        :param dualStack: (Optional) 是否双栈支持，开启后，kube-apiserver将拥有ipv6地址，默认不开启
        :param masterNatEnabled: (Optional) 是否开启master访问公网的能力，如果需要引入公网OIDC认证时需要开启，默认不开启
        :param natGateway: (Optional) nat网关配置,如果clusterNetworkType为auto，当natGateway和nodeElasticIpSpec都为空时会自动创建nat虚机
        :param nodeElasticIpSpec: (Optional) 节点公网IP的配置，与nat网关配置互斥，不可同时设置
        """

        self.publicApiServer = publicApiServer
        self.masterCidr = masterCidr
        self.nodeNetworkCidr = nodeNetworkCidr
        self.vpcId = vpcId
        self.dualStack = dualStack
        self.masterNatEnabled = masterNatEnabled
        self.natGateway = natGateway
        self.nodeElasticIpSpec = nodeElasticIpSpec
