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


class UranusTableDeleteRequest(JDCloudRequest):
    """
    删除表
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(UranusTableDeleteRequest, self).__init__(
            '/regions/{regionId}/apps/{appName}/uranusTableDelete', 'GET', header, version)
        self.parameters = parameters


class UranusTableDeleteParameters(object):

    def __init__(self,regionId, appName, table, env):
        """
        :param regionId: 地域ID
        :param appName: 应用名称
        :param table: 根据表名删除表
        :param env: 环境信息，dev 开发、prod 生产
        """

        self.regionId = regionId
        self.appName = appName
        self.table = table
        self.env = env

