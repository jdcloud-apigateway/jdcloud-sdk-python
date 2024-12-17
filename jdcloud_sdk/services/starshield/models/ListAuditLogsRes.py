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


class ListAuditLogsRes(object):

    def __init__(self, auditId=None, auditWhen=None, metadataId=None, metadataName=None, actionType=None, actionResult=None, actorType=None, actorUser=None, actorIp=None, oldValue=None, newValue=None):
        """
        :param auditId: (Optional) 审计日志requestId
        :param auditWhen: (Optional) 审计日志时间
        :param metadataId: (Optional) 元数据id：zoneId、popId、instanceId
        :param metadataName: (Optional) 元数据对象：域名、节点名称、实例名称
        :param actionType: (Optional) 事件类型：开启pause、开启lockdown、开启黑白名单、开启关闭节点
一、域名操作
op_zone_on_pause：开启pause
op_zone_off_pause：关闭pause
op_zone_on_lockdown：开启lockdown
op_zone_off_lockdown：关闭lockdown
op_zone_on_black：开启域名黑名单
op_zone_off_black：关闭域名黑名单
op_zone_on_white：开启域名白名单
op_zone_off_white：关闭域名白名单
op_zone_dns_records_archive：解析记录归档

二、节点操作
op_pop_change_pack：节点套餐调整
op_pop_online：节点上线
op_pop_offline：节点下线

三、实例套餐调整
op_instance_change_pack：实例套餐规格调整

        :param actionResult: (Optional) 事件结果：False->失败 True->成功
        :param actorType: (Optional) 操作用户类型：console->控制台用户、system->系统周期性定时任务等、op->运营后台
        :param actorUser: (Optional) 操作用户：运营后台erp、控制台user
        :param actorIp: (Optional) 操作ip
        :param oldValue: (Optional) 旧配置
        :param newValue: (Optional) 新配置
        """

        self.auditId = auditId
        self.auditWhen = auditWhen
        self.metadataId = metadataId
        self.metadataName = metadataName
        self.actionType = actionType
        self.actionResult = actionResult
        self.actorType = actorType
        self.actorUser = actorUser
        self.actorIp = actorIp
        self.oldValue = oldValue
        self.newValue = newValue