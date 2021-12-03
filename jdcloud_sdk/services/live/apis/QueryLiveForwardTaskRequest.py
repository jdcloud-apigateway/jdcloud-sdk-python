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


class QueryLiveForwardTaskRequest(JDCloudRequest):
    """
    查询直播拉流转推任务

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryLiveForwardTaskRequest, self).__init__(
            '/LiveForwardTask:query', 'GET', header, version)
        self.parameters = parameters


class QueryLiveForwardTaskParameters(object):

    def __init__(self, ):
        """
        """

        self.pageNum = None
        self.pageSize = None
        self.filters = None

    def setPageNum(self, pageNum):
        """
        :param pageNum: (Optional) 页码
- 取值范围 [1, 100000]

        """
        self.pageNum = pageNum

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小
- 取值范围 [10, 100]

        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) 拉流转推任务查询过滤条件:
- name:   taskId 任务ID
- value:  如果参数为空，则查询全部
- name:   taskName 任务名称
- value:  如果参数为空，则查询全部

        """
        self.filters = filters

