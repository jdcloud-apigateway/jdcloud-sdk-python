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


class CompanyAuthInfoVo(object):

    def __init__(self, license=None, authWay=None, companyName=None, time=None, supportUpdateCompanyAuth=None, expireTime=None):
        """
        :param license: (Optional) 统一社会信用代码
        :param authWay: (Optional) 企业认证方式
        :param companyName: (Optional) 企业名
        :param time: (Optional) 认证时间
        :param supportUpdateCompanyAuth: (Optional) 是否允许更新认证
        :param expireTime: (Optional) 到期时间
        """

        self.license = license
        self.authWay = authWay
        self.companyName = companyName
        self.time = time
        self.supportUpdateCompanyAuth = supportUpdateCompanyAuth
        self.expireTime = expireTime
