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


class Vpc(object):

    def __init__(self, vpcId=None, addressPrefix=None, description=None, vpcName=None, aclIds=None, routeTableIds=None, subnets=None, createdTime=None, resourceId=None, version=None, regionId=None, typeId=None, typeName=None, appType=None, appName=None, appKey=None):
        """
        :param vpcId: (Optional) Vpc的Id
        :param addressPrefix: (Optional) 如果为空，则不限制网段，如果不为空，10.0.0.0/8、172.16.0.0/12和192.168.0.0/16及它们包含的子网，且子网掩码长度为16-28之间
        :param description: (Optional) VPC 描述，取值范围：1~120个字符
        :param vpcName: (Optional) 私有网络名称，取值范围：1-60个中文、英文大小写的字母、数字和下划线分隔符
        :param aclIds: (Optional) 同一vpc下的acl id 列表
        :param routeTableIds: (Optional) 
        :param subnets: (Optional) 私有网络包含的子网列表
        :param createdTime: (Optional) vpc创建时间
        :param resourceId: (Optional) 云鼎资源ID
        :param version: (Optional) 版本
        :param regionId: (Optional) 所属区域
        :param typeId: (Optional) 业务类型：1-无界开放
        :param typeName: (Optional) 业务类型名称
        :param appType: (Optional) 应用类型
        :param appName: (Optional) 应用名称
        :param appKey: (Optional) appKey
        """

        self.vpcId = vpcId
        self.addressPrefix = addressPrefix
        self.description = description
        self.vpcName = vpcName
        self.aclIds = aclIds
        self.routeTableIds = routeTableIds
        self.subnets = subnets
        self.createdTime = createdTime
        self.resourceId = resourceId
        self.version = version
        self.regionId = regionId
        self.typeId = typeId
        self.typeName = typeName
        self.appType = appType
        self.appName = appName
        self.appKey = appKey
