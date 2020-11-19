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


class WebBlackListRule(object):

    def __init__(self, id=None, name=None, mode=None, key=None, value=None, pattern=None, action=None, actionValue=None, status=None, geoList=None, pageId=None, pageName=None):
        """
        :param id: (Optional) 黑名单规则 Id
        :param name: (Optional) 黑名单规则名称
        :param mode: (Optional) 匹配模式:<br>- 0: uri<br>- 1: ip<br>- 2: cookie<br>- 3: geo<br>- 4: header
        :param key: (Optional) 匹配 key. <br>- mode 为 cookie 时, 为 cookie 的 name<br>- mode 为 header 时, 为 header 的 key
        :param value: (Optional) 匹配 value. <br>- mode 为 uri 时, 为要匹配的 uri<br>- mode 为 ip 时, 为引用的 ip 黑白名单 Id<br>- mode 为 cookie 时, 为 cookie 的 value<br>- mode 为 header 时, 为 header 的 value
        :param pattern: (Optional) 匹配规则, mode 为 uri, cookie 和 header 时有效. 包含以下匹配规则: <br>- 0: 完全匹配<br>- 1: 前缀匹配<br>- 2: 包含<br>- 3: 正则匹配<br>- 4: 后缀匹配
        :param action: (Optional) 命中后处理动作. <br>- 0: 封禁并返回自定义页面<br>- 1: 跳转<br>- 2: 验证码
        :param actionValue: (Optional) 命中后处理值, 命中后处理动作为跳转时有效, 表示跳转路径
        :param status: (Optional) 规则状态. <br>- 0: 关闭<br>- 1: 开启
        :param geoList: (Optional) geo 黑名单地域列表, mode 不为 geo 或未设置时此字段为空
        :param pageId: (Optional) 关联的自定义页面id, 命中后处理动作为封禁并返回自定义页面时有效, 为空时表示默认页面
        :param pageName: (Optional) 关联的自定义页面名称, 命中后处理动作为封禁并返回自定义页面时有效
        """

        self.id = id
        self.name = name
        self.mode = mode
        self.key = key
        self.value = value
        self.pattern = pattern
        self.action = action
        self.actionValue = actionValue
        self.status = status
        self.geoList = geoList
        self.pageId = pageId
        self.pageName = pageName
