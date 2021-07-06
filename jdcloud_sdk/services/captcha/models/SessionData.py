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


class SessionData(object):

    def __init__(self, appId, sceneId, secret, ip, userAgent, clientType, uuid=None, fingerPrint=None, clientVersion=None):
        """
        :param appId:  应用id
        :param sceneId:  场景id
        :param secret:  密钥，从界面获取
        :param uuid: (Optional) uuid，ios客户端传openudid, android客户端传androidid, pc和wxapp客户端可不传
        :param ip:  客户端ip
        :param userAgent:  客户端userAgent
        :param fingerPrint: (Optional) 指纹，客户端sdk获取
        :param clientType:  客户端类型, android, ios, pc, wxapp, m
        :param clientVersion: (Optional) 客户端版本，用户端app版本，可选
        """

        self.appId = appId
        self.sceneId = sceneId
        self.secret = secret
        self.uuid = uuid
        self.ip = ip
        self.userAgent = userAgent
        self.fingerPrint = fingerPrint
        self.clientType = clientType
        self.clientVersion = clientVersion
