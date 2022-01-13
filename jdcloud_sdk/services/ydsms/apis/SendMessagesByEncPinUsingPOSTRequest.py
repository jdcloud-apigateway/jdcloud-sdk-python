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


class SendMessagesByEncPinUsingPOSTRequest(JDCloudRequest):
    """
    根据加密pin发送短信
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SendMessagesByEncPinUsingPOSTRequest, self).__init__(
            '/sendMessagesByEncPin', 'POST', header, version)
        self.parameters = parameters


class SendMessagesByEncPinUsingPOSTParameters(object):

    def __init__(self, appId, signId, templateId, encPins, ):
        """
        :param appId: 应用id
        :param signId: 签名id
        :param templateId: 模板id
        :param encPins: 加密pin集合，不能超过100个
        """

        self.appId = appId
        self.signId = signId
        self.templateId = templateId
        self.encPins = encPins
        self.params = None

    def setParams(self, params):
        """
        :param params: (Optional) 短信模板变量对应的数据值
        """
        self.params = params

