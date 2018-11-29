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


class BackupSynchronicity(object):

    def __init__(self, serviceId=None, instanceId=None, serviceStatus=None, srcRegion=None, destRegion=None, engine=None, engineVersion=None, createTime=None, newestDataTime=None):
        """
        :param serviceId: (Optional) 跨地域备份同步服务ID
        :param instanceId: (Optional) RDS 实例ID
        :param serviceStatus: (Optional) 跨地域备份同步服务状态，正常，running；错误，error
        :param srcRegion: (Optional) 源实例所在地域
        :param destRegion: (Optional) 备份同步的目标地域
        :param engine: (Optional) 数据库类型
        :param engineVersion: (Optional) 数据库版本
        :param createTime: (Optional) 创建时间
        :param newestDataTime: (Optional) 跨地域备份的最新数据时间点
        """

        self.serviceId = serviceId
        self.instanceId = instanceId
        self.serviceStatus = serviceStatus
        self.srcRegion = srcRegion
        self.destRegion = destRegion
        self.engine = engine
        self.engineVersion = engineVersion
        self.createTime = createTime
        self.newestDataTime = newestDataTime
