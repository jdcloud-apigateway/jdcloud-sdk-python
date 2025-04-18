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


class ResourceResp(object):

    def __init__(self, resourceType=None, resourceName=None, resourceCode=None, resourceStatus=None, resourceFlag=None, az=None, privateId=None, ipv4Cidr=None, subnetId=None, subnetCidr=None, natSubnetId=None, securityGroup=None, payMethod=None, id=None, effectiveStartTime=None):
        """
        :param resourceType: (Optional) 
        :param resourceName: (Optional) 
        :param resourceCode: (Optional) 
        :param resourceStatus: (Optional) 
        :param resourceFlag: (Optional) 
        :param az: (Optional) 
        :param privateId: (Optional) 
        :param ipv4Cidr: (Optional) 
        :param subnetId: (Optional) 
        :param subnetCidr: (Optional) 
        :param natSubnetId: (Optional) 
        :param securityGroup: (Optional) 
        :param payMethod: (Optional) 
        :param id: (Optional) 
        :param effectiveStartTime: (Optional) 
        """

        self.resourceType = resourceType
        self.resourceName = resourceName
        self.resourceCode = resourceCode
        self.resourceStatus = resourceStatus
        self.resourceFlag = resourceFlag
        self.az = az
        self.privateId = privateId
        self.ipv4Cidr = ipv4Cidr
        self.subnetId = subnetId
        self.subnetCidr = subnetCidr
        self.natSubnetId = natSubnetId
        self.securityGroup = securityGroup
        self.payMethod = payMethod
        self.id = id
        self.effectiveStartTime = effectiveStartTime
