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


class DsOnlineParam(object):

    def __init__(self, appName=None, appDesc=None, appEnv=None, appVolume=None, useSSL=None, usePrivileged=None, protocols=None):
        """
        :param appName: (Optional) App名称
        :param appDesc: (Optional) App描述
        :param appEnv: (Optional) App环境变量
        :param appVolume: (Optional) App添加卷
        :param useSSL: (Optional) 是否使用SSL，0-不使用，1-使用
        :param usePrivileged: (Optional) 使用特权运行，0-不使用，1-使用
        :param protocols: (Optional) 协议列表维护
        """

        self.appName = appName
        self.appDesc = appDesc
        self.appEnv = appEnv
        self.appVolume = appVolume
        self.useSSL = useSSL
        self.usePrivileged = usePrivileged
        self.protocols = protocols
