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


class LogDetailRequest(JDCloudRequest):
    """
    获取满足条件的日志详情
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(LogDetailRequest, self).__init__(
            '/logDetail', 'POST', header, version)
        self.parameters = parameters


class LogDetailParameters(object):

    def __init__(self,pin, product, ):
        """
        :param pin: 租户
        :param product: 产品名，必填
        """

        self.pin = pin
        self.searchId = None
        self.product = product
        self.instance = None
        self.logType = None
        self.ip = None
        self.podName = None
        self.namespace = None
        self.cluster = None
        self.containerName = None
        self.filePath = None
        self.startTime = None
        self.endTime = None
        self.direction = None
        self.limit = None
        self.step = None
        self.streamFilter = None
        self.lineFilter = None
        self.fmtFilter = None

    def setSearchId(self, searchId):
        """
        :param searchId: (Optional) UUID，同一批次保持一致，必填
        """
        self.searchId = searchId

    def setInstance(self, instance):
        """
        :param instance: (Optional) 实例
        """
        self.instance = instance

    def setLogType(self, logType):
        """
        :param logType: (Optional) 日志类型
        """
        self.logType = logType

    def setIp(self, ip):
        """
        :param ip: (Optional) ip
        """
        self.ip = ip

    def setPodName(self, podName):
        """
        :param podName: (Optional) pod name
        """
        self.podName = podName

    def setNamespace(self, namespace):
        """
        :param namespace: (Optional) 命名空间
        """
        self.namespace = namespace

    def setCluster(self, cluster):
        """
        :param cluster: (Optional) 集群
        """
        self.cluster = cluster

    def setContainerName(self, containerName):
        """
        :param containerName: (Optional) 容器名
        """
        self.containerName = containerName

    def setFilePath(self, filePath):
        """
        :param filePath: (Optional) 文件路径
        """
        self.filePath = filePath

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 开始时间纳秒数字，默认一小时前
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 结束时间纳秒数字，默认现在
        """
        self.endTime = endTime

    def setDirection(self, direction):
        """
        :param direction: (Optional) 正序：FORWARD、倒序：BACKWARD，默认BACKWARD
        """
        self.direction = direction

    def setLimit(self, limit):
        """
        :param limit: (Optional) 查询数量数字，默认100
        """
        self.limit = limit

    def setStep(self, step):
        """
        :param step: (Optional) 步长时间（单位：秒），10、0.5
        """
        self.step = step

    def setStreamFilter(self, streamFilter):
        """
        :param streamFilter: (Optional) label过滤
        """
        self.streamFilter = streamFilter

    def setLineFilter(self, lineFilter):
        """
        :param lineFilter: (Optional) 行过滤
        """
        self.lineFilter = lineFilter

    def setFmtFilter(self, fmtFilter):
        """
        :param fmtFilter: (Optional) 格式化过滤条件
        """
        self.fmtFilter = fmtFilter

