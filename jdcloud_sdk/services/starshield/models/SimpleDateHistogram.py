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


class SimpleDateHistogram(object):

    def __init__(self, dataSeries=None, timeSeries=None):
        """
        :param dataSeries: (Optional) 数据点集合。
如果是带宽，数据点的单位是bps（bit per second）
如果是流量，数据点的单位是Byte
如果是请求量，数据点的单位是次数

        :param timeSeries: (Optional) 时间点集合。时间点的值为时间戳对应的long值。
        """

        self.dataSeries = dataSeries
        self.timeSeries = timeSeries
