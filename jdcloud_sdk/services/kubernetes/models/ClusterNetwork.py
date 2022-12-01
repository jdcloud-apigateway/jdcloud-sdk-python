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


class ClusterNetwork(object):

    def __init__(self, publicApiServer=None, masterCidr=None, serviceCidr=None, vpcId=None, podSubnets=None, clusterSubnets=None, natGateway=None, nodeElasticIpSpec=None):
        """
        :param publicApiServer: (Optional) kube-apiserver是否可公网访问，false则kube-apiserver不绑定公网地址，true绑定公网地址
        :param masterCidr: (Optional) master网络的cidr
        :param serviceCidr: (Optional) service网络的cidr
        :param vpcId: (Optional) 用户侧承载node和pod的vpc id
        :param podSubnets: (Optional) 集群Pod子网信息
        :param clusterSubnets: (Optional) 集群子网信息
        :param natGateway: (Optional) nat网关配置
        :param nodeElasticIpSpec: (Optional) 节点公网IP的配置，如果设置了节点公网IP，此项不为空
        """

        self.publicApiServer = publicApiServer
        self.masterCidr = masterCidr
        self.serviceCidr = serviceCidr
        self.vpcId = vpcId
        self.podSubnets = podSubnets
        self.clusterSubnets = clusterSubnets
        self.natGateway = natGateway
        self.nodeElasticIpSpec = nodeElasticIpSpec
