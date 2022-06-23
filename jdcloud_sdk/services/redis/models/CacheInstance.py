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


class CacheInstance(object):

    def __init__(self, cacheInstanceId=None, cacheInstanceName=None, cacheInstanceClass=None, cacheInstanceMemoryMB=None, cacheInstanceStatus=None, cacheInstanceDescription=None, createTime=None, azId=None, vpcId=None, subnetId=None, connectionDomain=None, port=None, charge=None, instanceVersion=None, auth=None, redisVersion=None, cacheInstanceType=None, ipv6On=None, tags=None, resourceGroupId=None, shardNumber=None, memoryMBPerShard=None, extension=None, otherDomains=None, slaveAppendonly=None, databaseNum=None, maxmemoryPolicy=None, replicaNumber=None, enableSmartProxy=None, cpuArchType=None):
        """
        :param cacheInstanceId: (Optional) 实例ID
        :param cacheInstanceName: (Optional) 实例名称
        :param cacheInstanceClass: (Optional) 规格代码，2.8、4.0标准版是实例规格，4.0自定义分片集群版实例表示单分片规格
        :param cacheInstanceMemoryMB: (Optional) 实例的总内存（MB），表示用户购买的可使用内存
        :param cacheInstanceStatus: (Optional) 实例状态：creating表示创建中，running表示运行中，error表示错误，changing表示变更规格中，deleting表示删除中，configuring表示修改参数中，restoring表示备份恢复中，upgrading表示升级中
        :param cacheInstanceDescription: (Optional) 实例描述
        :param createTime: (Optional) 创建时间（ISO 8601标准的UTC时间，格式为：YYYY-MM-DDTHH:mm:ssZ）
        :param azId: (Optional) az信息
        :param vpcId: (Optional) 实例所属VPC ID
        :param subnetId: (Optional) 实例所属子网ID
        :param connectionDomain: (Optional) 实例的访问域名
        :param port: (Optional) 实例的访问端口
        :param charge: (Optional) 实例的计费信息
        :param instanceVersion: (Optional) 实例的详细版本号，形如x.x-x.x
        :param auth: (Optional) 连接实例时，是否需要密码认证，false表示无密码
        :param redisVersion: (Optional) 创建实例时选择的引擎版本：目前支持2.8和4.0
        :param cacheInstanceType: (Optional) 实例类型：master-slave（标准版）、cluster（代理集群版）、native-cluster（cluster集群版）
        :param ipv6On: (Optional) 是否支持IPv6，0表示不支持（只能用IPv4），1表示支持
        :param tags: (Optional) 标签信息
        :param resourceGroupId: (Optional) 实例所属资源组ID
        :param shardNumber: (Optional) 实例分片数，标准版固定为1，自定义分片集群版实例分片数由用户创建时选择，其他实例为固定分片数
        :param memoryMBPerShard: (Optional) 单分片内存大小（MB）
        :param extension: (Optional) 扩展配置
        :param otherDomains: (Optional) 实例其他访问域名列表
        :param slaveAppendonly: (Optional) 从节点aof开关
        :param databaseNum: (Optional) db数量
        :param maxmemoryPolicy: (Optional) 淘汰策略
        :param replicaNumber: (Optional) 副本数，含主副本
        :param enableSmartProxy: (Optional) 实例是否开启SmartProxy，当架构类型为native-cluster时才有效，1表示开启，0表示不开启
        :param cpuArchType: (Optional) cpu架构类型:arm64、amd64
        """

        self.cacheInstanceId = cacheInstanceId
        self.cacheInstanceName = cacheInstanceName
        self.cacheInstanceClass = cacheInstanceClass
        self.cacheInstanceMemoryMB = cacheInstanceMemoryMB
        self.cacheInstanceStatus = cacheInstanceStatus
        self.cacheInstanceDescription = cacheInstanceDescription
        self.createTime = createTime
        self.azId = azId
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.connectionDomain = connectionDomain
        self.port = port
        self.charge = charge
        self.instanceVersion = instanceVersion
        self.auth = auth
        self.redisVersion = redisVersion
        self.cacheInstanceType = cacheInstanceType
        self.ipv6On = ipv6On
        self.tags = tags
        self.resourceGroupId = resourceGroupId
        self.shardNumber = shardNumber
        self.memoryMBPerShard = memoryMBPerShard
        self.extension = extension
        self.otherDomains = otherDomains
        self.slaveAppendonly = slaveAppendonly
        self.databaseNum = databaseNum
        self.maxmemoryPolicy = maxmemoryPolicy
        self.replicaNumber = replicaNumber
        self.enableSmartProxy = enableSmartProxy
        self.cpuArchType = cpuArchType
