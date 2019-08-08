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


class DescribeMonitorTargetRequest(JDCloudRequest):
    """
    查询子域名的可用监控对象
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(DescribeMonitorTargetRequest, self).__init__(
            '/regions/{regionId}/domain/{domainId}/monitorTarget', 'GET', header, version)
        self.parameters = parameters


class DescribeMonitorTargetParameters(object):

    def __init__(self, regionId, domainId, subDomainName):
        """
        :param regionId: 实例所属的地域ID
        :param domainId: 域名ID，请使用describeDomains接口获取。
        :param subDomainName: 子域名
        """

        self.regionId = regionId
        self.domainId = domainId
        self.subDomainName = subDomainName
