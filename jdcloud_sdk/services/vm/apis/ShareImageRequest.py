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


class ShareImageRequest(JDCloudRequest):
    """
    
共享私有镜像。

详细操作说明请参考帮助文档：[共享私有镜像](https://docs.jdcloud.com/cn/virtual-machines/share-image)

## 接口说明
- 只允许共享用户的私有镜像。
- 单个镜像最多可以共享给20个京东云帐户、不可以共享给自己。
- 带有加密快照的打包镜像无法共享。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ShareImageRequest, self).__init__(
            '/regions/{regionId}/images/{imageId}:share', 'POST', header, version)
        self.parameters = parameters


class ShareImageParameters(object):

    def __init__(self, regionId,imageId,pins):
        """
        :param regionId: 地域ID。
        :param imageId: 镜像ID。
        :param pins: 共享的目标京东云帐户列表。
        """

        self.regionId = regionId
        self.imageId = imageId
        self.pins = pins

