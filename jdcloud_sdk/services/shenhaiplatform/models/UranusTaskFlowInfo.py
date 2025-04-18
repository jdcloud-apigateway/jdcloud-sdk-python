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


class UranusTaskFlowInfo(object):

    def __init__(self, flowName, catalogCode, flowDesc=None, workers=None):
        """
        :param flowName:  工作流名称
        :param flowDesc: (Optional) 工作流描述
        :param catalogCode:  工作流所属目录
        :param workers: (Optional) 工作流协同人
        """

        self.flowName = flowName
        self.flowDesc = flowDesc
        self.catalogCode = catalogCode
        self.workers = workers
