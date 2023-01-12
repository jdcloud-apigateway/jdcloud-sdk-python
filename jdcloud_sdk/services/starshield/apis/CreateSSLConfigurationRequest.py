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


class CreateSSLConfigurationRequest(JDCloudRequest):
    """
    上载域的新SSL证书
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateSSLConfigurationRequest, self).__init__(
            '/zones/{zone_identifier}/custom_certificates', 'POST', header, version)
        self.parameters = parameters


class CreateSSLConfigurationParameters(object):

    def __init__(self,zone_identifier, ):
        """
        :param zone_identifier: 
        """

        self.zone_identifier = zone_identifier
        self.certificate = None
        self.private_key = None
        self.bundle_method = None
        self.geo_restrictions = None
        self.ty_pe = None

    def setCertificate(self, certificate):
        """
        :param certificate: (Optional) 域的SSL证书或证书以及中间证书
        """
        self.certificate = certificate

    def setPrivate_key(self, private_key):
        """
        :param private_key: (Optional) 域的私钥
        """
        self.private_key = private_key

    def setBundle_method(self, bundle_method):
        """
        :param bundle_method: (Optional) 合法值ubiquitous/optimal/force，默认值ubiquitous。
ubiquitous：SSL泛捆绑在各处有着最高的概率被验证，甚至能被使用过时的或不寻常的信任存储的客户端验证。
optimal：最佳捆绑使用最短的认证链和最新的中间证书。
force：强制捆绑会验证证书链，但不以其他方式修改证书链。

        """
        self.bundle_method = bundle_method

    def setGeo_restrictions(self, geo_restrictions):
        """
        :param geo_restrictions: (Optional) 
        """
        self.geo_restrictions = geo_restrictions

    def setTy_pe(self, ty_pe):
        """
        :param ty_pe: (Optional) “legacy_custom”类型支持在TLS握手中不包含SNI的传统客户端。
合法值：
legacy_custom
sni_custom

        """
        self.ty_pe = ty_pe

