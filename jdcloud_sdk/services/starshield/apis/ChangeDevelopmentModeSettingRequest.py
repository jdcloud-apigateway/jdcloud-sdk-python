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


class ChangeDevelopmentModeSettingRequest(JDCloudRequest):
    """
    如果你需要对你的网站进行修改，开发模式可以让你暂时进入网站的开发模式。这将绕过星盾的加速缓存，并降低您的网站速度。
但如果您正在对可缓存的内容（如图片、css 或 JavaScript）进行更改，并希望立即看到这些更改，这时就很有用。一旦进入，开发模式将持续3小时，然后自动切换关闭。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ChangeDevelopmentModeSettingRequest, self).__init__(
            '/zones/{zone_identifier}/settings$$development_mode', 'PATCH', header, version)
        self.parameters = parameters


class ChangeDevelopmentModeSettingParameters(object):

    def __init__(self, zone_identifier, ):
        """
        :param zone_identifier: 
        """

        self.zone_identifier = zone_identifier
        self.value = None

    def setValue(self, value):
        """
        :param value: (Optional) on - 开启；off - 关闭
        """
        self.value = value

