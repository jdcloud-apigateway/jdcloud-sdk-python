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


class Plan(object):

    def __init__(self, core=None, bandwidth=None, diskSize=None, flow=None, memory=None, planId=None, classification=None, diskType=None, originalPrice=None, supportOS=None):
        """
        :param core: (Optional) CPU核数
        :param bandwidth: (Optional) 峰值带宽单位：Mbps
        :param diskSize: (Optional) 磁盘容量单位：GB。
        :param flow: (Optional) 每月流量单位：GB。
        :param memory: (Optional) 内存 单位：GB
        :param planId: (Optional) 套餐ID
        :param classification: (Optional) 套餐分类：通用型套餐（字段：universal）、存储型套餐（字段：storage）、企业型套餐（字段：enterprise）
        :param diskType: (Optional) 磁盘类型
        :param originalPrice: (Optional) 价格
        :param supportOS: (Optional) 套餐支持的操作系统类型
        """

        self.core = core
        self.bandwidth = bandwidth
        self.diskSize = diskSize
        self.flow = flow
        self.memory = memory
        self.planId = planId
        self.classification = classification
        self.diskType = diskType
        self.originalPrice = originalPrice
        self.supportOS = supportOS
