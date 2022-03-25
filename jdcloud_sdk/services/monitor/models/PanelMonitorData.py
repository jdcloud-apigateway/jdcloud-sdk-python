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


class PanelMonitorData(object):

    def __init__(self, aggregator=None, dataPoint=None, downsample=None, downsamplePeriod=None, metric=None, metricName=None, resourceId=None, resourceName=None, tags=None, unit=None):
        """
        :param aggregator: (Optional) 聚合方式
        :param dataPoint: (Optional) 监控数据
        :param downsample: (Optional) 采样方式
        :param downsamplePeriod: (Optional) 采样周期
        :param metric: (Optional) metric
        :param metricName: (Optional) metric名字
        :param resourceId: (Optional) 实例id，汇总图无
        :param resourceName: (Optional) 实例名称，汇总图无；标签资源该值为实例id
        :param tags: (Optional) 该资源的维度值
        :param unit: (Optional) metric单位
        """

        self.aggregator = aggregator
        self.dataPoint = dataPoint
        self.downsample = downsample
        self.downsamplePeriod = downsamplePeriod
        self.metric = metric
        self.metricName = metricName
        self.resourceId = resourceId
        self.resourceName = resourceName
        self.tags = tags
        self.unit = unit