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


class ListQualityDetectionTemplatesResultObject(object):

    def __init__(self, pageNumber=None, pageSize=None, totalElements=None, totalPages=None, content=None):
        """
        :param pageNumber: (Optional) 当前页码
        :param pageSize: (Optional) 每页数量
        :param totalElements: (Optional) 查询总数
        :param totalPages: (Optional) 总页数
        :param content: (Optional) 分页内容
        """

        self.pageNumber = pageNumber
        self.pageSize = pageSize
        self.totalElements = totalElements
        self.totalPages = totalPages
        self.content = content
