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


class CreateFlowLogRequest(JDCloudRequest):
    """
    本接口用于创建流日志资源
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateFlowLogRequest, self).__init__(
            '/regions/{regionId}/flowLogs', 'POST', header, version)
        self.parameters = parameters


class CreateFlowLogParameters(object):

    def __init__(self,regionId, flowLogName, flowLogType, storageRegionId, storageId):
        """
        :param regionId: 地域 ID
        :param flowLogName: 流日志名称，只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符
        :param flowLogType: 流日志类型
PORT：采集资源可为云主机、弹性网卡

        :param storageRegionId: 流日志的存储服务所在地域，如日志服务所属地域，如cn-north-1
        :param storageId: 流日志的存储服务ID
若storageType = LOG时，值取日志主题ID，如logtopic-xxxx
当flowLogType = PORT时，值需取 templateUID = eniflowlogs 的日志主题ID

        """

        self.regionId = regionId
        self.flowLogName = flowLogName
        self.description = None
        self.flowLogType = flowLogType
        self.collectResources = None
        self.collectTrafficType = None
        self.collectInterval = None
        self.storageType = None
        self.storageRegionId = storageRegionId
        self.storageId = storageId

    def setDescription(self, description):
        """
        :param description: (Optional) 描述,允许输入UTF-8编码下的全部字符，不超过256字符
        """
        self.description = description

    def setCollectResources(self, collectResources):
        """
        :param collectResources: (Optional) 采集资源列表
        """
        self.collectResources = collectResources

    def setCollectTrafficType(self, collectTrafficType):
        """
        :param collectTrafficType: (Optional) 采集流量类型
ALL：记录指定资源的全部流量
ACCEPT：记录指定资源被安全组、网络ACL均接受的流量
REJECT：记录指定资源被安全组或网络ACL拒绝的流量     

        """
        self.collectTrafficType = collectTrafficType

    def setCollectInterval(self, collectInterval):
        """
        :param collectInterval: (Optional) 流日志采集时间间隔。单位：分钟。取值：1、5、10
        """
        self.collectInterval = collectInterval

    def setStorageType(self, storageType):
        """
        :param storageType: (Optional) 流日志的存储服务类型，支持存储到日志服务，日志服务取值：LOG
        """
        self.storageType = storageType
