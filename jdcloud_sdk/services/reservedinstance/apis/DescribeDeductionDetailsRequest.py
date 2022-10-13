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


class DescribeDeductionDetailsRequest(JDCloudRequest):
    """
    查询实例券使用明细列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeDeductionDetailsRequest, self).__init__(
            '/regions/{regionId}/deductionDetails', 'GET', header, version)
        self.parameters = parameters


class DescribeDeductionDetailsParameters(object):

    def __init__(self,regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.reservedInstanceType = None
        self.reservedInstanceId = None
        self.instanceId = None
        self.startTime = None
        self.endTime = None
        self.pageNo = None
        self.pageSize = None

    def setReservedInstanceType(self, reservedInstanceType):
        """
        :param reservedInstanceType: (Optional) 实例券类型
        """
        self.reservedInstanceType = reservedInstanceType

    def setReservedInstanceId(self, reservedInstanceId):
        """
        :param reservedInstanceId: (Optional) 实例券ID
        """
        self.reservedInstanceId = reservedInstanceId

    def setInstanceId(self, instanceId):
        """
        :param instanceId: (Optional) 抵扣实例ID
        """
        self.instanceId = instanceId

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 使用开始时间
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 使用结束时间
        """
        self.endTime = endTime

    def setPageNo(self, pageNo):
        """
        :param pageNo: (Optional) 页码,默认为1
        """
        self.pageNo = pageNo

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认10，最大100
        """
        self.pageSize = pageSize

