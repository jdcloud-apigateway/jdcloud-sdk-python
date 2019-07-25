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


class DomainObject(object):

    def __init__(self, id=None, name=None, cname=None, status=None, source=None, asDefault=None, createTime=None, updateTime=None):
        """
        :param id: (Optional) 域名ID
        :param name: (Optional) 域名名称
        :param cname: (Optional) 域名CNAME
        :param status: (Optional) 域名状态。取值范围：
  init - 初始状态
  configuring - 配置中
  normal - 正常
  stopped - 已停用

        :param source: (Optional) 域名来源。取值范围：
  system - 系统生成
  custom - 用户自建

        :param asDefault: (Optional) 是否默认域名
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 修改时间
        """

        self.id = id
        self.name = name
        self.cname = cname
        self.status = status
        self.source = source
        self.asDefault = asDefault
        self.createTime = createTime
        self.updateTime = updateTime
