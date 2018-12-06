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


class DescribeAllRegionAlarmsCmRequest(JDCloudRequest):
    """
    查询所有region的自定义监控规则
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeAllRegionAlarmsCmRequest, self).__init__(
            '/cm/alarms', 'GET', header, version)
        self.parameters = parameters


class DescribeAllRegionAlarmsCmParameters(object):

    def __init__(self, ):
        """
        """

        self.pageNumber = None
        self.pageSize = None
        self.namespace = None
        self.obj = None
        self.serviceCode = None
        self.resourceId = None
        self.status = None
        self.isAlarming = None
        self.enabled = None
        self.region = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 当前所在页，默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页面大小，默认为20；取值范围[1, 100]
        """
        self.pageSize = pageSize

    def setNamespace(self, namespace):
        """
        :param namespace: (Optional) 命名空间名称
        """
        self.namespace = namespace

    def setObj(self, obj):
        """
        :param obj: (Optional) 对象名称
        """
        self.obj = obj

    def setServiceCode(self, serviceCode):
        """
        :param serviceCode: (Optional) 产品名称
        """
        self.serviceCode = serviceCode

    def setResourceId(self, resourceId):
        """
        :param resourceId: (Optional) 资源Id
        """
        self.resourceId = resourceId

    def setStatus(self, status):
        """
        :param status: (Optional) 规则报警状态, 1：正常, 2：报警，4：数据不足
        """
        self.status = status

    def setIsAlarming(self, isAlarming):
        """
        :param isAlarming: (Optional) 是否为正在报警的规则，0为忽略，1为是，与 status 同时只能生效一个,isAlarming 优先生效
        """
        self.isAlarming = isAlarming

    def setEnabled(self, enabled):
        """
        :param enabled: (Optional) 规则状态：1为启用，0为禁用
        """
        self.enabled = enabled

    def setRegion(self, region):
        """
        :param region: (Optional) region info
        """
        self.region = region

