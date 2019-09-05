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


class GetHttpSslResultObject(object):

    def __init__(self, source=None, title=None, sslCert=None, sslKey=None, jumpType=None, enabled=None):
        """
        :param source: (Optional) 证书来源。取值范围：default
        :param title: (Optional) 证书标题
        :param sslCert: (Optional) 证书内容
        :param sslKey: (Optional) 证书私钥
        :param jumpType: (Optional) 跳转类型。取值范围：
default - 采用回源域名的默认协议
http - 强制采用http协议回源
https - 强制采用https协议回源

        :param enabled: (Optional) SSL配置启用状态
        """

        self.source = source
        self.title = title
        self.sslCert = sslCert
        self.sslKey = sslKey
        self.jumpType = jumpType
        self.enabled = enabled
