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


class PageItemVo(object):

    def __init__(self, id=None, title=None, url=None, icon=None, siteName=None, snippet=None, summary=None, dateLastCrawled=None):
        """
        :param id: (Optional) id
        :param title: (Optional) 标题
        :param url: (Optional) 网页url
        :param icon: (Optional) 网页icon url
        :param siteName: (Optional) 网站名称
        :param snippet: (Optional) 网页描述
        :param summary: (Optional) 网页摘要
        :param dateLastCrawled: (Optional) 抓取时间
        """

        self.id = id
        self.title = title
        self.url = url
        self.icon = icon
        self.siteName = siteName
        self.snippet = snippet
        self.summary = summary
        self.dateLastCrawled = dateLastCrawled
