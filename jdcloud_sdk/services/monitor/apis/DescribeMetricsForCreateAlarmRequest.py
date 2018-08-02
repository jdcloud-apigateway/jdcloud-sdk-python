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


class DescribeMetricsForCreateAlarmRequest(JDCloudRequest):
    """
    查询可用创建监控规则的指标列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeMetricsForCreateAlarmRequest, self).__init__(
            '/metricsForCreateAlarm', 'GET', header, version)
        self.parameters = parameters


class DescribeMetricsForCreateAlarmParameters(object):

    def __init__(self, ):
        """
        """

        self.serviceCode = None

    def setServiceCode(self, serviceCode):
        """
        :param serviceCode: (Optional) 资源的类型，默认为空，展示所有项目
vm-->云主机
disk-->云硬盘
ip-->公网ip
balance-->负载均衡
database-->云数据库mysql版本
cdn-->京东CDN
redis-->redis云缓存
mongodb-->mongoDB云缓存
storage-->云存储
sqlserver-->云数据库sqlserver版 
nativecontainer-->容器

        """
        self.serviceCode = serviceCode

