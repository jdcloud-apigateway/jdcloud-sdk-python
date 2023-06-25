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


class ListDomains(object):

    def __init__(self, wafInstanceId, domain=None, pageIndex=None, pageSize=None):
        """
        :param wafInstanceId:  WAF实例id
        :param domain: (Optional) 域名
        :param pageIndex: (Optional) 页码，[1-100]，默认为1
        :param pageSize: (Optional) 页大小，[1-100]，默认为20
        """

        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.pageIndex = pageIndex
        self.pageSize = pageSize
