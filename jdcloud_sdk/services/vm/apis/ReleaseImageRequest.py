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


class ReleaseImageRequest(JDCloudRequest):
    """
    
发布社区镜像。

详细操作说明请参考帮助文档：[镜像概述](https://docs.jdcloud.com/cn/virtual-machines/image-overview)

## 接口说明
- 只允许发布用户的私有镜像。
- 仅支持云盘系统盘的私有镜像。
- 带有加密快照的打包镜像无法发布为社区镜像。
- 发布为社区镜像后会撤销共享关系。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ReleaseImageRequest, self).__init__(
            '/regions/{regionId}/images/{imageId}:release', 'POST', header, version)
        self.parameters = parameters


class ReleaseImageParameters(object):

    def __init__(self, regionId,imageId,):
        """
        :param regionId: 地域ID。
        :param imageId: 镜像ID。
        """

        self.regionId = regionId
        self.imageId = imageId

