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


class RegisterUserRequestObj(object):

    def __init__(self, appId=None, userName=None, userId=None, portraitUrl=None, temporary=None):
        """
        :param appId: (Optional) 应用ID
        :param userName: (Optional) 用户名称
        :param userId: (Optional) 业务接入方用户体系定义的userId
        :param portraitUrl: (Optional) 用户头像url
        :param temporary: (Optional) 是否临时用户
        """

        self.appId = appId
        self.userName = userName
        self.userId = userId
        self.portraitUrl = portraitUrl
        self.temporary = temporary
