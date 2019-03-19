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


class AddLiveStreamDomainWatermarkRequest(JDCloudRequest):
    """
    添加域名水印配置
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddLiveStreamDomainWatermarkRequest, self).__init__(
            '/watermarkDomains:config', 'POST', header, version)
        self.parameters = parameters


class AddLiveStreamDomainWatermarkParameters(object):

    def __init__(self, publishDomain, template):
        """
        :param publishDomain: 您的推流加速域名
        :param template: 水印模板自定义名称:
  - 标准质量模板：sd、hd、hsd
  - 自定义模板: 枚举类型校验，忽略大小写，自动删除空格,
              取值要求：数字、大小写字母或短横线("-"),
              首尾不能有特殊字符("-")
  - <b>注意: 不能与标准的转码模板和已定义命名重复</b>

        """

        self.publishDomain = publishDomain
        self.template = template

