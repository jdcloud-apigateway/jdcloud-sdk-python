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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class CreateListenerRequest(JDCloudRequest):
    """
    创建一个监听器
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateListenerRequest, self).__init__(
            '/regions/{regionId}/listeners/', 'POST', header, version)
        self.parameters = parameters


class CreateListenerParameters(object):

    def __init__(self,regionId, listenerName, protocol, port, backendId, loadBalancerId, ):
        """
        :param regionId: Region ID
        :param listenerName: Listener的名字,只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符
        :param protocol: 监听协议, 取值为Tcp, Tls, Http, Https, Udp <br>【alb】支持Http, Https，Tcp、Tls和Udp <br>【nlb】支持Tcp, Udp  <br>【dnlb】支持Tcp, Udp
        :param port: 监听端口，取值范围为[1, 65535]
        :param backendId: 默认的后端服务Id
        :param loadBalancerId: Listener所属loadBalancer的Id
        """

        self.regionId = regionId
        self.listenerName = listenerName
        self.protocol = protocol
        self.hstsEnable = None
        self.hstsMaxAge = None
        self.port = port
        self.backendId = backendId
        self.loadBalancerId = loadBalancerId
        self.urlMapId = None
        self.action = None
        self.certificateSpecs = None
        self.limitation = None
        self.connectionIdleTimeSeconds = None
        self.description = None
        self.securityPolicyId = None

    def setHstsEnable(self, hstsEnable):
        """
        :param hstsEnable: (Optional) 【alb使用https时支持】是否开启HSTS，True(开启)， False(关闭)，缺省为False
        """
        self.hstsEnable = hstsEnable

    def setHstsMaxAge(self, hstsMaxAge):
        """
        :param hstsMaxAge: (Optional) 【alb使用https时支持】HSTS过期时间(秒)，取值范围为[1, 94608000(3年)]，缺省为31536000(1年)
        """
        self.hstsMaxAge = hstsMaxAge

    def setUrlMapId(self, urlMapId):
        """
        :param urlMapId: (Optional) 【alb Https和Http协议】转发规则组Id
        """
        self.urlMapId = urlMapId

    def setAction(self, action):
        """
        :param action: (Optional) 默认后端服务的转发策略,取值为Forward或Redirect, 现只支持Forward, 默认为Forward
        """
        self.action = action

    def setCertificateSpecs(self, certificateSpecs):
        """
        :param certificateSpecs: (Optional) 【alb Https和Tls协议】Listener绑定的默认证书，最多支持两个，两个证书的加密算法需要不同
        """
        self.certificateSpecs = certificateSpecs

    def setLimitation(self, limitation):
        """
        :param limitation: (Optional) 【仅ALB支持】限速配置
        """
        self.limitation = limitation

    def setConnectionIdleTimeSeconds(self, connectionIdleTimeSeconds):
        """
        :param connectionIdleTimeSeconds: (Optional) 【alb、nlb】空闲连接超时时间, 范围为[1,86400]。 <br>（Tcp和Tls协议）默认为：1800s <br>（Udp协议）默认为：300s <br>（Http和Https协议）默认为：60s <br>【dnlb】不支持
        """
        self.connectionIdleTimeSeconds = connectionIdleTimeSeconds

    def setDescription(self, description):
        """
        :param description: (Optional) 描述,允许输入UTF-8编码下的全部字符，不超过256字符
        """
        self.description = description

    def setSecurityPolicyId(self, securityPolicyId):
        """
        :param securityPolicyId: (Optional) 绑定的安全策略id，仅支持应用负载均衡的HTTPS、TLS监听配置，不传默认使用默认安全策略
        """
        self.securityPolicyId = securityPolicyId

