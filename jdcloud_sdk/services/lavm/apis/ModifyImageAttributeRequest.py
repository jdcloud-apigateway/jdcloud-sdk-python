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


class ModifyImageAttributeRequest(JDCloudRequest):
    """
    修改镜像属性。
详细操作说明请参考帮助文档：[镜像概述](https://docs.jdcloud.com/cn/virtual-machines/image-overview)
## 接口说明
- 只支持修改镜像名称或描述。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyImageAttributeRequest, self).__init__(
            '/regions/{regionId}/images/{imageId}:modifyImageAttribute', 'POST', header, version)
        self.parameters = parameters


class ModifyImageAttributeParameters(object):

    def __init__(self,imageId, regionId, ):
        """
        :param imageId: 自定义镜像ID
        :param regionId: 地域ID。
        """

        self.imageId = imageId
        self.regionId = regionId
        self.name = None
        self.description = None

    def setName(self, name):
        """
        :param name: (Optional) 镜像名称。参考 [公共参数规范](https://docs.jdcloud.com/virtual-machines/api/general_parameters)。
        """
        self.name = name

    def setDescription(self, description):
        """
        :param description: (Optional) 镜像描述。参考 [公共参数规范](https://docs.jdcloud.com/virtual-machines/api/general_parameters)。
        """
        self.description = description
