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


class PaDateHistogram(object):

    def __init__(self, sum=None, max=None, maxTimestamp=None, dataSeries=None, timeSeries=None):
        """
        :param sum: (Optional) 对于获取流量类统计信息的接口，该和表示符合查询条件的流量总和，单位Byte

        :param max: (Optional) 对于获取带宽类统计信息的接口，该最大值表示符合查询条件的最大带宽，单位bps（bit per second）

        :param maxTimestamp: (Optional) 对于获取带宽类统计信息的接口，该时间戳表示符合查询条件的最大带宽的发生时刻

        :param dataSeries: (Optional) 数据点集合。
如果是带宽，数据点的单位是bps（bit per second）
如果是流量，数据点的单位是Byte

        :param timeSeries: (Optional) 时间点集合。时间点的值为时间戳对应的long值。
        """

        self.sum = sum
        self.max = max
        self.maxTimestamp = maxTimestamp
        self.dataSeries = dataSeries
        self.timeSeries = timeSeries
