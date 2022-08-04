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


class DescribeRealtimeCabinetCurrentRequest(JDCloudRequest):
    """
    查询多个机柜AB路实时电流
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeRealtimeCabinetCurrentRequest, self).__init__(
            '/idcs/{idc}/realtimeCabinetCurrent', 'GET', header, version)
        self.parameters = parameters


class DescribeRealtimeCabinetCurrentParameters(object):

    def __init__(self, idc,resourceId):
        """
        :param idc: IDC机房ID
        :param resourceId: 资源ID，支持多个resourceId批量查询，每个id用英文竖线分隔
        """

        self.idc = idc
        self.resourceId = resourceId

