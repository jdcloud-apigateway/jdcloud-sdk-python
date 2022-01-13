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


class DescribeOperationRecordsRequest(JDCloudRequest):
    """
    查询操作日志
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeOperationRecordsRequest, self).__init__(
            '/operationRecords', 'GET', header, version)
        self.parameters = parameters


class DescribeOperationRecordsParameters(object):

    def __init__(self, startTime, endTime, ):
        """
        :param startTime: 开始时间, UTC 时间, 格式：yyyy-MM-dd'T'HH:mm:ssZ
        :param endTime: 结束时间, UTC 时间, 格式：yyyy-MM-dd'T'HH:mm:ssZ
        """

        self.pageNumber = None
        self.pageSize = None
        self.startTime = startTime
        self.endTime = endTime
        self.action = None
        self.name = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小
        """
        self.pageSize = pageSize

    def setAction(self, action):
        """
        :param action: (Optional) 操作类型, 默认查全部. <br>- 0: 全部<br>- 1: 套餐变更<br>- 2: 防护规则变更<br>- 3: 防护对象变更<br>- 4: IP 地址变更<br>- 5: 防护包名称变更<br>- 6: IP地址库变更<br>- 7: 端口库变更<br>- 8: 访问控制规则变更
        """
        self.action = action

    def setName(self, name):
        """
        :param name: (Optional) 防护包名称, 支持模糊匹配
        """
        self.name = name

