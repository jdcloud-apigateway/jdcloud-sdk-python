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


class BizType(object):

    def __init__(self, bizTypeId=None, name=None, description=None, industryInfo=None, censorType=None, updateTime=None):
        """
        :param bizTypeId: (Optional) 机审策略id
        :param name: (Optional) 业务名称，英文名称，不能超过32个字符
        :param description: (Optional) 规则描述
        :param industryInfo: (Optional) 行业分类，可选政府、新闻、电商、社交、视频直播、金融
        :param censorType: (Optional) 内容安全类型，可选api/oss/website，默认为api
        :param updateTime: (Optional) 更新时间
        """

        self.bizTypeId = bizTypeId
        self.name = name
        self.description = description
        self.industryInfo = industryInfo
        self.censorType = censorType
        self.updateTime = updateTime