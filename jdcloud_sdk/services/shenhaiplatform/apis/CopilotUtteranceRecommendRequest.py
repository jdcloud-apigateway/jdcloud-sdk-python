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


class CopilotUtteranceRecommendRequest(JDCloudRequest):
    """
    根据对话中的一条发言，推荐可能的prompt
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(CopilotUtteranceRecommendRequest, self).__init__(
            '/regions/{regionId}/apps/{appName}/copilotUtteranceRecommend', 'GET', header, version)
        self.parameters = parameters


class CopilotUtteranceRecommendParameters(object):

    def __init__(self,regionId, appName, chatId, utteranceId):
        """
        :param regionId: 地域ID
        :param appName: 应用名称
        :param chatId: 对话id
        :param utteranceId: 发言id
        """

        self.regionId = regionId
        self.appName = appName
        self.chatId = chatId
        self.utteranceId = utteranceId

