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


class AclUser(object):

    def __init__(self, userName=None, password=None, whiteRemoteAddress=None):
        """
        :param userName: (Optional) 用户名
        :param password: (Optional) 密码
        :param whiteRemoteAddress: (Optional) 用户级别白名单
        """

        self.userName = userName
        self.password = password
        self.whiteRemoteAddress = whiteRemoteAddress
