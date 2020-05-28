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


class EventReportPageBo(object):

    def __init__(self, deviceId=None, order=None, orders=None, pageNo=None, pageSize=None):
        """
        :param deviceId: (Optional) 设备标识Id
        :param order: (Optional) 排序方式;升序-ASC,降序-DESC
        :param orders: (Optional) 排序方式;升序-ASC,降序-DESC
        :param pageNo: (Optional) 页码
        :param pageSize: (Optional) 每页条数
        """

        self.deviceId = deviceId
        self.order = order
        self.orders = orders
        self.pageNo = pageNo
        self.pageSize = pageSize
