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


class ZoneBandwidth(object):

    def __init__(self, zonename=None, instanceName=None, pin=None, packType=None, chargeState=None, instanceExpireTime=None, bps=None, normalBps=None, mitigationBps=None, totalFlowStr=None, usedFlowStr=None, remainingFlowStr=None, instanceUsedStatus=None, icpStatus=None):
        """
        :param zonename: (Optional) 域名
        :param instanceName: (Optional) 所属实例名称
        :param pin: (Optional) 所属PIN
        :param packType: (Optional) 套餐类型
        :param chargeState: (Optional) 计费状态
        :param instanceExpireTime: (Optional) 实例到期时间
        :param bps: (Optional) 查询时间段内的峰值带宽，单位bit per second
        :param normalBps: (Optional) 查询时间段内的业务峰值带宽，单位bit per second
        :param mitigationBps: (Optional) 查询时间段内的攻击峰值带宽，单位bit per second
        :param totalFlowStr: (Optional) 套餐总流量
        :param usedFlowStr: (Optional) 套餐已使用流量
        :param remainingFlowStr: (Optional) 套餐剩余流量
        :param instanceUsedStatus: (Optional) 实例使用状态，正常, 超量, 弹性账单
        :param icpStatus: (Optional) 备案状态：false 未备案、true 已备案
        """

        self.zonename = zonename
        self.instanceName = instanceName
        self.pin = pin
        self.packType = packType
        self.chargeState = chargeState
        self.instanceExpireTime = instanceExpireTime
        self.bps = bps
        self.normalBps = normalBps
        self.mitigationBps = mitigationBps
        self.totalFlowStr = totalFlowStr
        self.usedFlowStr = usedFlowStr
        self.remainingFlowStr = remainingFlowStr
        self.instanceUsedStatus = instanceUsedStatus
        self.icpStatus = icpStatus
