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


class QueryJBoxAvgBandwidthRequest(JDCloudRequest):
    """
    查询平均带宽
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryJBoxAvgBandwidthRequest, self).__init__(
            '/jdbox:queryAvgBandwidth', 'GET', header, version)
        self.parameters = parameters


class QueryJBoxAvgBandwidthParameters(object):

    def __init__(self, starttime, stoptime, pluginPin, ):
        """
        :param starttime: 指定查询开始时间(格式:201906011000)，返回数据包含该时间点。
        :param stoptime: 指定查询结束时间(格式:201906011100)，返回数据不包含该时间点
        :param pluginPin: 插件pin,多个用,隔开
        """

        self.starttime = starttime
        self.stoptime = stoptime
        self.pluginPin = pluginPin
        self.clientid = None
        self.page = None
        self.size = None

    def setClientid(self, clientid):
        """
        :param clientid: (Optional) 按照设备ID查询设备带宽,即macaddr,多个用,隔开
        """
        self.clientid = clientid

    def setPage(self, page):
        """
        :param page: (Optional) 用于支持分页查询，默认为1，表示第几页。
        """
        self.page = page

    def setSize(self, size):
        """
        :param size: (Optional) 用于支持分页查询，表示每页返回多少条数据，默认每页返回10条数据，size必须是10的整数倍，并且最大值是100。
        """
        self.size = size
