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


class EnableCname2RsReq(object):

    def __init__(self, instanceId=None, domain=None, enable=None):
        """
        :param instanceId: (Optional) 实例id
        :param domain: (Optional) 域名
        :param enable: (Optional) 模式：0为云端模式，1为回源模式
        """

        self.instanceId = instanceId
        self.domain = domain
        self.enable = enable