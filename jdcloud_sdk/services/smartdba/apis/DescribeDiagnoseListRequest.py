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


class DescribeDiagnoseListRequest(JDCloudRequest):
    """
    获取当前实例的所有诊断记录
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(DescribeDiagnoseListRequest, self).__init__(
            '/regions/{regionId}/instance/{instanceGid}/diagnoses', 'GET', header, version)
        self.parameters = parameters


class DescribeDiagnoseListParameters(object):

    def __init__(self, regionId,instanceGid,):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceGid: RDS 实例ID，唯一标识一个RDS实例
        """

        self.regionId = regionId
        self.instanceGid = instanceGid
        self.pageIndex = None
        self.pageSize = None

    def setPageIndex(self, pageIndex):
        """
        :param pageIndex: (Optional) 显示数据的页码，默认为1，取值范围：[-1,∞)。pageIndex 为-1时，返回所有数据页码；
        """
        self.pageIndex = pageIndex

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页显示的数据条数，默认为10，取值范围：[1,100]，用于查询列表的接口
        """
        self.pageSize = pageSize
