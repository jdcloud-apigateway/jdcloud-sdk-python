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


class CreateTicketRequest(JDCloudRequest):
    """
    创建免登录ticket
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateTicketRequest, self).__init__(
            '/user:createTicket', 'POST', header, version)
        self.parameters = parameters


class CreateTicketParameters(object):

    def __init__(self,):
        """
        """

        self.expire = None

    def setExpire(self, expire):
        """
        :param expire: (Optional) 有效期（默认24，最小1，最大24，单位小时）
        """
        self.expire = expire
