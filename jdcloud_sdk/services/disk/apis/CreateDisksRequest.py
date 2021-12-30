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


class CreateDisksRequest(JDCloudRequest):
    """
    -   创建一块或多块按配置或者按使用时长付费的云硬盘。
-   云硬盘类型包括高效云盘(premium-hdd)、SSD云盘(ssd)、通用型SSD(ssd.gp1)、性能型SSD(ssd.io1)、容量型HDD(hdd.std1)。
-   计费方式默认为按配置付费。
-   创建完成后，云硬盘状态为 available。
-   可选参数快照 ID用于从快照创建新盘。
-   批量创建时，云硬盘的命名为 硬盘名称-数字，例如 myDisk-1，myDisk-2。
-   maxCount为最大努力，不保证一定能达到maxCount。
-   userTags 为创建云盘时打的标签

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateDisksRequest, self).__init__(
            '/regions/{regionId}/disks', 'POST', header, version)
        self.parameters = parameters


class CreateDisksParameters(object):

    def __init__(self, regionId, diskSpec, maxCount, clientToken):
        """
        :param regionId: 地域ID
        :param diskSpec: 创建云硬盘规格
        :param maxCount: 购买实例数量；取值范围：[1,100]
        :param clientToken: 幂等性校验参数
        """

        self.regionId = regionId
        self.diskSpec = diskSpec
        self.maxCount = maxCount
        self.userTags = None
        self.clientToken = clientToken

    def setUserTags(self, userTags):
        """
        :param userTags: (Optional) 用户标签,默认为空;tag标签的限制：每个资源最多允许绑定 10 个不同的标签，同一资源每个标签“键”上只能存在1个标签“值”；标签键/值只支持中文、数字、大小写字母、空格及特殊符号_.:/=+-@;当无tags时,reps结果返回中tagmsg为空
        """
        self.userTags = userTags

