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


class DeleteHttpHeaderRequest(JDCloudRequest):
    """
    删除httpHeader
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteHttpHeaderRequest, self).__init__(
            '/domain/{domain}/httpHeader', 'PUT', header, version)
        self.parameters = parameters


class DeleteHttpHeaderParameters(object):

    def __init__(self, domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.edgeType = None
        self.headerType = None
        self.headerName = None

    def setEdgeType(self, edgeType):
        """
        :param edgeType: (Optional) 0表示header在边缘生效，1表示header回源生效，2表示在边缘和回源都生效，该字段不传时默认header在边缘和回源都生效
        """
        self.edgeType = edgeType

    def setHeaderType(self, headerType):
        """
        :param headerType: (Optional) header类型[resp,req]
        """
        self.headerType = headerType

    def setHeaderName(self, headerName):
        """
        :param headerName: (Optional) header名
        """
        self.headerName = headerName

