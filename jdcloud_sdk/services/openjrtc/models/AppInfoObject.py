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


class AppInfoObject(object):

    def __init__(self, appId=None, appName=None, status=None, billType=None, createTime=None):
        """
        :param appId: (Optional) 应用ID
        :param appName: (Optional) 应用名称
        :param status: (Optional) 应用状态: OPEN-启用, CLOSE-停用

        :param billType: (Optional) 计费类型: Duration-按时长

        :param createTime: (Optional) 创建时间(UTC)
        """

        self.appId = appId
        self.appName = appName
        self.status = status
        self.billType = billType
        self.createTime = createTime