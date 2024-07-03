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


class DescribeRangetimeCabinetOriCurrentRequest(JDCloudRequest):
    """
    按照时间段查询单个机柜AB路电流-原始数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeRangetimeCabinetOriCurrentRequest, self).__init__(
            '/idcs/{idc}/rangetimeCabinetOriCurrent', 'GET', header, version)
        self.parameters = parameters


class DescribeRangetimeCabinetOriCurrentParameters(object):

    def __init__(self,idc, resourceId, startTime, endTime):
        """
        :param idc: IDC机房ID
        :param resourceId: 机柜资源ID
        :param startTime: 查询时间范围的开始时间， UNIX时间戳，（最多支持最近90天数据查询）
        :param endTime: 查询时间范围的结束时间， UNIX时间戳，（最多支持最近90天数据查询）
        """

        self.idc = idc
        self.resourceId = resourceId
        self.startTime = startTime
        self.endTime = endTime
