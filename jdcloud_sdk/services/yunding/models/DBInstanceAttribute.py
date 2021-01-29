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


class DBInstanceAttribute(object):

    def __init__(self, instanceId=None, instanceName=None, instanceType=None, engine=None, engineVersion=None, instanceClass=None, instanceStorageType=None, storageEncrypted=None, instanceStorageGB=None, instanceCPU=None, instanceMemoryMB=None, regionId=None, azId=None, vpcId=None, subnetId=None, parameterGroupId=None, parameterGroupName=None, parameterStatus=None, internalDomainName=None, publicDomainName=None, instancePort=None, connectionMode=None, auditStatus=None, instanceStatus=None, createTime=None, charge=None, sourceInstanceId=None, roInstanceIds=None, primaryNode=None, secondaryNode=None, tags=None, vpcName=None):
        """
        :param instanceId: (Optional) 实例ID
        :param instanceName: (Optional) 实例名称，具体规则可参见帮助中心文档:[名称及密码限制](../../../documentation/Database-and-Cache-Service/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
        :param instanceType: (Optional) 实例类型，例如主实例，只读实例等，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param engine: (Optional) 实例引擎类型，如MySQL或SQL Server等，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param engineVersion: (Optional) 实例引擎版本，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param instanceClass: (Optional) 实例规格代码
        :param instanceStorageType: (Optional) 存储类型，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param storageEncrypted: (Optional) 实例数据加密. false：不加密; true：加密
        :param instanceStorageGB: (Optional) 磁盘，单位GB
        :param instanceCPU: (Optional) CPU核数
        :param instanceMemoryMB: (Optional) 内存大小，单位MB
        :param regionId: (Optional) 地域ID，参见[地域及可用区对照表](../Enum-Definitions/Regions-AZ.md)
        :param azId: (Optional) 可用区ID，第一个为主实例在的可用区，参见[地域及可用区对照表](../Enum-Definitions/Regions-AZ.md)
        :param vpcId: (Optional) VPC的ID
        :param subnetId: (Optional) 子网的ID
        :param parameterGroupId: (Optional) 参数组的ID<br>- 仅支持MySQL
        :param parameterGroupName: (Optional) 参数组的名称<br>- 仅支持MySQL
        :param parameterStatus: (Optional) 参数的状态，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)<br>- 仅支持MySQL
        :param internalDomainName: (Optional) 实例内网域名
        :param publicDomainName: (Optional) 实例公网域名
        :param instancePort: (Optional) 应用访问端口
        :param connectionMode: (Optional) 访问模式，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)<br>- 仅支持MySQL
        :param auditStatus: (Optional) 审计状态，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)<br>- 仅支持MySQL
        :param instanceStatus: (Optional) 实例状态，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param createTime: (Optional) 实例创建时间
        :param charge: (Optional) 计费配置
        :param sourceInstanceId: (Optional) MySQL只读实例对应的主实例ID<br>- 仅支持MySQL
        :param roInstanceIds: (Optional) 只读实例ID列表<br>- 仅支持MySQL
        :param primaryNode: (Optional) 高可用集群中主节点的信息<br>- 仅支持SQL Server
        :param secondaryNode: (Optional) 高可用集群中从节点的信息<br>- 仅支持SQL Server
        :param tags: (Optional) 标签信息
        :param vpcName: (Optional) vpc名称
        """

        self.instanceId = instanceId
        self.instanceName = instanceName
        self.instanceType = instanceType
        self.engine = engine
        self.engineVersion = engineVersion
        self.instanceClass = instanceClass
        self.instanceStorageType = instanceStorageType
        self.storageEncrypted = storageEncrypted
        self.instanceStorageGB = instanceStorageGB
        self.instanceCPU = instanceCPU
        self.instanceMemoryMB = instanceMemoryMB
        self.regionId = regionId
        self.azId = azId
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.parameterGroupId = parameterGroupId
        self.parameterGroupName = parameterGroupName
        self.parameterStatus = parameterStatus
        self.internalDomainName = internalDomainName
        self.publicDomainName = publicDomainName
        self.instancePort = instancePort
        self.connectionMode = connectionMode
        self.auditStatus = auditStatus
        self.instanceStatus = instanceStatus
        self.createTime = createTime
        self.charge = charge
        self.sourceInstanceId = sourceInstanceId
        self.roInstanceIds = roInstanceIds
        self.primaryNode = primaryNode
        self.secondaryNode = secondaryNode
        self.tags = tags
        self.vpcName = vpcName
