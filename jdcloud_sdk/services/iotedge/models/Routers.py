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


class Routers(object):

    def __init__(self, routerId=None, routerName=None, routerDesc=None, routerStatus=None, routerUpdateStatus=None, createTime=None, sourceName=None, targetName=None):
        """
        :param routerId: (Optional) router编号
        :param routerName: (Optional) router名称
        :param routerDesc: (Optional) router描述
        :param routerStatus: (Optional) router状态
        :param routerUpdateStatus: (Optional) router配置更新状态, SUCCESS-更新成功，UPDATEING-更新中,FAILTURE-更新失败
        :param createTime: (Optional) router创建时间
        :param sourceName: (Optional) router数据源名称
        :param targetName: (Optional) router数据目标名称
        """

        self.routerId = routerId
        self.routerName = routerName
        self.routerDesc = routerDesc
        self.routerStatus = routerStatus
        self.routerUpdateStatus = routerUpdateStatus
        self.createTime = createTime
        self.sourceName = sourceName
        self.targetName = targetName
