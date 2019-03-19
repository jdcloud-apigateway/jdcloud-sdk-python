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


class ServiceDetail(object):

    def __init__(self, serviceName, apiList, resourceList, ):
        """
        :param serviceName:  产品线名称
        :param apiList:  策略相关OpenAPI的Action列表
        :param resourceList:  资源列表
        """

        self.serviceName = serviceName
        self.apiList = apiList
        self.resourceList = resourceList
