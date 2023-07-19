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


class DetailAgentInfo(object):

    def __init__(self, agentId=None, agentName=None, agentPhone=None, agentIdCardNum=None, agentFileName=None, agentAuthFile=None):
        """
        :param agentId: (Optional) 授权ID
        :param agentName: (Optional) 授权人姓名
        :param agentPhone: (Optional) 手机号
        :param agentIdCardNum: (Optional) 身份证号
        :param agentFileName: (Optional) 授权书名称
        :param agentAuthFile: (Optional) 授权书（base64）--pdf格式
        """

        self.agentId = agentId
        self.agentName = agentName
        self.agentPhone = agentPhone
        self.agentIdCardNum = agentIdCardNum
        self.agentFileName = agentFileName
        self.agentAuthFile = agentAuthFile
