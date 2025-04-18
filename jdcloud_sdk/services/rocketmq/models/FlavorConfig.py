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


class FlavorConfig(object):

    def __init__(self, onSale=None, instanceClassCode=None, cpu=None, memoryGB=None, storageLimit=None, nodeCountLimit=None, replicaPeGroupLimit=None):
        """
        :param onSale: (Optional) 指定规格是否售卖
        :param instanceClassCode: (Optional) 规格代码
        :param cpu: (Optional) 指定规格表示的cpu核数
        :param memoryGB: (Optional) 指定规格表示的内存
        :param storageLimit: (Optional) 存储配置(是不是云盘、本地盘的大小、云盘的最小值、最大值、默认值、步长)
        :param nodeCountLimit: (Optional) 节点个数配置(节点个数最小值、最大值、默认值、步长)
        :param replicaPeGroupLimit: (Optional) 副本组个数配置(副本组个数最小值、最大值、默认值、步长)
        """

        self.onSale = onSale
        self.instanceClassCode = instanceClassCode
        self.cpu = cpu
        self.memoryGB = memoryGB
        self.storageLimit = storageLimit
        self.nodeCountLimit = nodeCountLimit
        self.replicaPeGroupLimit = replicaPeGroupLimit
