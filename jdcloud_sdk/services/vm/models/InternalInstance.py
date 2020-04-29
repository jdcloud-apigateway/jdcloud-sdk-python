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


class InternalInstance(object):

    def __init__(self, instanceId=None, instanceName=None, instanceType=None, vpcId=None, subnetId=None, privateIpAddress=None, status=None, description=None, imageId=None, systemDisk=None, dataDisks=None, primaryNetworkInterface=None, secondaryNetworkInterfaces=None, launchTime=None, az=None, keyNames=None, faultDomain=None, chargeOnStopped=None, dedicatedPoolId=None, dedicatedHostId=None, hostIp=None):
        """
        :param instanceId: (Optional) 云主机ID
        :param instanceName: (Optional) 云主机名称
        :param instanceType: (Optional) 实例规格
        :param vpcId: (Optional) 主网卡所属VPC的ID
        :param subnetId: (Optional) 主网卡所属子网的ID
        :param privateIpAddress: (Optional) 主网卡主IP地址
        :param status: (Optional) 云主机状态，<a href="http://docs.jdcloud.com/virtual-machines/api/vm_status">参考云主机状态</a>
        :param description: (Optional) 云主机描述
        :param imageId: (Optional) 镜像ID
        :param systemDisk: (Optional) 系统盘配置
        :param dataDisks: (Optional) 数据盘配置
        :param primaryNetworkInterface: (Optional) 主网卡配置
        :param secondaryNetworkInterfaces: (Optional) 辅助网卡配置
        :param launchTime: (Optional) 创建时间
        :param az: (Optional) 云主机所在可用区
        :param keyNames: (Optional) 密钥对名称
        :param faultDomain: (Optional) 高可用组中的错误域
        :param chargeOnStopped: (Optional) 关机模式，只支持云盘做系统盘的按配置计费云主机。KeepCharging：关机后继续计费；StopCharging：关机后停止计费。
        :param dedicatedPoolId: (Optional) 实例所属的专有宿主机池
        :param dedicatedHostId: (Optional) 专有宿主机ID
        :param hostIp: (Optional) 实例的物理机 IP
        """

        self.instanceId = instanceId
        self.instanceName = instanceName
        self.instanceType = instanceType
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.privateIpAddress = privateIpAddress
        self.status = status
        self.description = description
        self.imageId = imageId
        self.systemDisk = systemDisk
        self.dataDisks = dataDisks
        self.primaryNetworkInterface = primaryNetworkInterface
        self.secondaryNetworkInterfaces = secondaryNetworkInterfaces
        self.launchTime = launchTime
        self.az = az
        self.keyNames = keyNames
        self.faultDomain = faultDomain
        self.chargeOnStopped = chargeOnStopped
        self.dedicatedPoolId = dedicatedPoolId
        self.dedicatedHostId = dedicatedHostId
        self.hostIp = hostIp
