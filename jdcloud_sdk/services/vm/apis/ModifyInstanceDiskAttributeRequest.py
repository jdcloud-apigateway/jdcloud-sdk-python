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


class ModifyInstanceDiskAttributeRequest(JDCloudRequest):
    """
    
修改一台云主机中的云硬盘属性。

详细操作说明请参考帮助文档：[配置云硬盘删除属性](https://docs.jdcloud.com/cn/virtual-machines/configurate-delete-attributes)

## 接口说明
- 该接口当前只能修改实例中的云硬盘随实例删除属性。
- 仅按配置计费、并且非共享型的云硬盘支持修改。
- 包年包月计费的云硬盘该属性不生效，实例删除时云硬盘将保留。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyInstanceDiskAttributeRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:modifyInstanceDiskAttribute', 'POST', header, version)
        self.parameters = parameters


class ModifyInstanceDiskAttributeParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域ID。
        :param instanceId: 云主机ID。
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.dataDisks = None

    def setDataDisks(self, dataDisks):
        """
        :param dataDisks: (Optional) 云硬盘列表。
        """
        self.dataDisks = dataDisks

