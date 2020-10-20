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


class ClusterListNode(object):

    def __init__(self, id=None, name=None, dataCenter=None, recordId=None, monitorResourceId=None, status=None, errorMessage=None, createTime=None, payType=None, duration=None, outerIp=None):
        """
        :param id: (Optional) 集群ID
        :param name: (Optional) 集群名称
        :param dataCenter: (Optional) 集群所属地域
        :param recordId: (Optional) 集群ID
        :param monitorResourceId: (Optional) 监控ID
        :param status: (Optional) 集群状态
        :param errorMessage: (Optional) 错误信息
        :param createTime: (Optional) 集群创建时间
        :param payType: (Optional) 集群收费类型
        :param duration: (Optional) 集群运行时间
        :param outerIp: (Optional) 公网Ip
        """

        self.id = id
        self.name = name
        self.dataCenter = dataCenter
        self.recordId = recordId
        self.monitorResourceId = monitorResourceId
        self.status = status
        self.errorMessage = errorMessage
        self.createTime = createTime
        self.payType = payType
        self.duration = duration
        self.outerIp = outerIp
