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


class ModifyAnalysisThresholdRequest(JDCloudRequest):
    """
    设置缓存分析阈值
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyAnalysisThresholdRequest, self).__init__(
            '/regions/{regionId}/cacheInstance/{cacheInstanceId}/cacheAnalysisThreshold', 'POST', header, version)
        self.parameters = parameters


class ModifyAnalysisThresholdParameters(object):

    def __init__(self, regionId,cacheInstanceId,):
        """
        :param regionId: 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2
        :param cacheInstanceId: 缓存Redis实例ID，是访问实例的唯一标识
        """

        self.regionId = regionId
        self.cacheInstanceId = cacheInstanceId
        self.stringSize = None
        self.listSize = None
        self.hashSize = None
        self.setSize = None
        self.zsetSize = None
        self.top = None

    def setStringSize(self, stringSize):
        """
        :param stringSize: (Optional) String类型阈值
        """
        self.stringSize = stringSize

    def setListSize(self, listSize):
        """
        :param listSize: (Optional) List类型阈值
        """
        self.listSize = listSize

    def setHashSize(self, hashSize):
        """
        :param hashSize: (Optional) Hash类型阈值
        """
        self.hashSize = hashSize

    def setSetSize(self, setSize):
        """
        :param setSize: (Optional) Set类型阈值
        """
        self.setSize = setSize

    def setZsetSize(self, zsetSize):
        """
        :param zsetSize: (Optional) Zset类型阈值
        """
        self.zsetSize = zsetSize

    def setTop(self, top):
        """
        :param top: (Optional) top值，范围10~1000
        """
        self.top = top
