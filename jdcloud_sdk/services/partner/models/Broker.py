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


class Broker(object):

    def __init__(self, name=None, identity=None, identityDesc=None, position=None, tel=None, email=None):
        """
        :param name: (Optional) 对接人名称
        :param identity: (Optional) 对接人身份
        :param identityDesc: (Optional) 对接人身份说明
        :param position: (Optional) 岗位
        :param tel: (Optional) 电话
        :param email: (Optional) 邮箱
        """

        self.name = name
        self.identity = identity
        self.identityDesc = identityDesc
        self.position = position
        self.tel = tel
        self.email = email