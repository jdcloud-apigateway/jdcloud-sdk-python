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


class BillDetailRequest(JDCloudRequest):
    """
    账单明细
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(BillDetailRequest, self).__init__(
            '/regions/{regionId}/billDetail/{billId}', 'GET', header, version)
        self.parameters = parameters


class BillDetailParameters(object):

    def __init__(self,regionId, billId):
        """
        :param regionId: 地域编码，参考OpenAPI公共说明
        :param billId: 计费账单编号
        """

        self.regionId = regionId
        self.billId = billId

