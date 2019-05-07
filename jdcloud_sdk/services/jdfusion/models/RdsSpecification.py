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


class RdsSpecification(object):

    def __init__(self, instanceClass=None, cpu=None, memoryGB=None, disk=None):
        """
        :param instanceClass: (Optional) 规格编号
        :param cpu: (Optional) CPU核数
        :param memoryGB: (Optional) 内存大小
        :param disk: (Optional) 
        """

        self.instanceClass = instanceClass
        self.cpu = cpu
        self.memoryGB = memoryGB
        self.disk = disk