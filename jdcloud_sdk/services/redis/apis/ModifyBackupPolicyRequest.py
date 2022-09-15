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


class ModifyBackupPolicyRequest(JDCloudRequest):
    """
    开启或更新缓存Redis实例的自动备份策略，可修改备份周期和备份时间
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyBackupPolicyRequest, self).__init__(
            '/regions/{regionId}/cacheInstance/{cacheInstanceId}/backupPolicy', 'PATCH', header, version)
        self.parameters = parameters


class ModifyBackupPolicyParameters(object):

    def __init__(self,regionId, cacheInstanceId, backupTime, backupPeriod):
        """
        :param regionId: 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2
        :param cacheInstanceId: 缓存Redis实例ID，是访问实例的唯一标识
        :param backupTime: 设置自动备份时间，格式为：HH:mm-HH:mm 时区，例如"01:00-02:00 +0800"，表示东八区的1点到2点
        :param backupPeriod: 备份周期，包括：Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday，多个用逗号分隔
        """

        self.regionId = regionId
        self.cacheInstanceId = cacheInstanceId
        self.autoBackup = None
        self.backupTime = backupTime
        self.backupPeriod = backupPeriod

    def setAutoBackup(self, autoBackup):
        """
        :param autoBackup: (Optional) 是否开启自动备份，true表示开启，false表示关闭
        """
        self.autoBackup = autoBackup

