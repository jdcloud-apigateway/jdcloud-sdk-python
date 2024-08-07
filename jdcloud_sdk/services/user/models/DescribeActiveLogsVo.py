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


class DescribeActiveLogsVo(object):

    def __init__(self, operatorErp=None, pin=None, activeTime=None, status=None, createTime=None, batchNo=None):
        """
        :param operatorErp: (Optional) 操作人
        :param pin: (Optional) pin
        :param activeTime: (Optional) 激活时间
        :param status: (Optional) 是否激活成功：0否1是
        :param createTime: (Optional) 创建时间
        :param batchNo: (Optional) 批量号
        """

        self.operatorErp = operatorErp
        self.pin = pin
        self.activeTime = activeTime
        self.status = status
        self.createTime = createTime
        self.batchNo = batchNo
