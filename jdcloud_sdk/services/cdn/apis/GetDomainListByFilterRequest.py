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


class GetDomainListByFilterRequest(JDCloudRequest):
    """
    通过标签查询加速域名接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetDomainListByFilterRequest, self).__init__(
            '/domain:query', 'POST', header, version)
        self.parameters = parameters


class GetDomainListByFilterParameters(object):

    def __init__(self,):
        """
        """

        self.keyWord = None
        self.pageNumber = None
        self.pageSize = None
        self.status = None
        self.type = None
        self.accelerateRegion = None
        self.filterBy = None
        self.tagFilters = None

    def setKeyWord(self, keyWord):
        """
        :param keyWord: (Optional) 根据关键字进行模糊匹配，域名或者回源信息
        """
        self.keyWord = keyWord

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) pageNumber,默认值为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) pageSize,默认值为20,最大值为50
        """
        self.pageSize = pageSize

    def setStatus(self, status):
        """
        :param status: (Optional) 根据域名状态查询, 可选值[offline, online, configuring, auditing, audit_reject]
        """
        self.status = status

    def setType(self, type):
        """
        :param type: (Optional) 域名类型，(web:静态小文件，download:大文件加速，vod:视频加速，live:直播加速),不传查所有
        """
        self.type = type

    def setAccelerateRegion(self, accelerateRegion):
        """
        :param accelerateRegion: (Optional) 加速区域，(mainLand:中国大陆，nonMainLand:海外加港澳台，all:全球),不传为全球
        """
        self.accelerateRegion = accelerateRegion

    def setFilterBy(self, filterBy):
        """
        :param filterBy: (Optional) 筛选依据（0：根据域名筛选，1：根据回源信息筛选），默认按照域名进行筛选
        """
        self.filterBy = filterBy

    def setTagFilters(self, tagFilters):
        """
        :param tagFilters: (Optional) 标签过滤条件
        """
        self.tagFilters = tagFilters

