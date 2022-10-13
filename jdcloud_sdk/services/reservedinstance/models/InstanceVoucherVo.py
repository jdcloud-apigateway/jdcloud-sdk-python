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


class InstanceVoucherVo(object):

    def __init__(self, instanceVoucherId=None, reservedInstanceType=None, isReserved=None, status=None, startTime=None, endTime=None):
        """
        :param instanceVoucherId: (Optional) 实例券ID
        :param reservedInstanceType: (Optional) 实例券类型(对应iaas侧resourceType)
        :param isReserved: (Optional) 是否有预留(1 有预留、2 无预留,对应iaas侧reservedType 预留:reserved, 不预留:unReserved)
        :param status: (Optional) 状态(1：正常: 2：已退订,-1:失效)
        :param startTime: (Optional) 生效时间
        :param endTime: (Optional) 失效时间
        """

        self.instanceVoucherId = instanceVoucherId
        self.reservedInstanceType = reservedInstanceType
        self.isReserved = isReserved
        self.status = status
        self.startTime = startTime
        self.endTime = endTime
