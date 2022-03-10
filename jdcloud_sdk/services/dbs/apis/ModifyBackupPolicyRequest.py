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
    修改备份策略
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(ModifyBackupPolicyRequest, self).__init__(
            '/regions/{regionId}/backupPlans/{backupPlanId}:modifyBackupPolicy', 'POST', header, version)
        self.parameters = parameters


class ModifyBackupPolicyParameters(object):

    def __init__(self, regionId,backupPlanId,):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》]
        :param backupPlanId: 备份计划ID
        """

        self.regionId = regionId
        self.backupPlanId = backupPlanId
        self.fullBackupPeriod = None
        self.fullBackupDays = None
        self.fullBackupStartTime = None
        self.fullBackupRetentionPeriod = None
        self.logBackupRetentionPeriod = None
        self.enableBackupLogs = None

    def setFullBackupPeriod(self, fullBackupPeriod):
        """
        :param fullBackupPeriod: (Optional) 周期类型，目前仅支持weekly
        """
        self.fullBackupPeriod = fullBackupPeriod

    def setFullBackupDays(self, fullBackupDays):
        """
        :param fullBackupDays: (Optional) 进行全量备份的日期, 备份周期为 weekly 时可以取 0-6 分别对应的是周日到周六
        """
        self.fullBackupDays = fullBackupDays

    def setFullBackupStartTime(self, fullBackupStartTime):
        """
        :param fullBackupStartTime: (Optional) 全量备份的开始时间，精确到分,UTC时间格式，例如：23:30Z
        """
        self.fullBackupStartTime = fullBackupStartTime

    def setFullBackupRetentionPeriod(self, fullBackupRetentionPeriod):
        """
        :param fullBackupRetentionPeriod: (Optional) 全量备份保存天数，支持7-3650 天，默认7天
        """
        self.fullBackupRetentionPeriod = fullBackupRetentionPeriod

    def setLogBackupRetentionPeriod(self, logBackupRetentionPeriod):
        """
        :param logBackupRetentionPeriod: (Optional) 日志备份保存天数，支持7-3650 天，默认7天
        """
        self.logBackupRetentionPeriod = logBackupRetentionPeriod

    def setEnableBackupLogs(self, enableBackupLogs):
        """
        :param enableBackupLogs: (Optional) 是否开启日志备份；true：开启；false：关闭
        """
        self.enableBackupLogs = enableBackupLogs

