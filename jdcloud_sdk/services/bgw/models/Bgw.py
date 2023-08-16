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


class Bgw(object):

    def __init__(self, bgwId=None, bgwName=None, description=None, vifIds=None, vpcAttachmentIds=None, vpnConnectionIds=None, azType=None, az=None, createdTime=None):
        """
        :param bgwId: (Optional) bgw的Id
        :param bgwName: (Optional) 边界网关的名称，只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符。
        :param description: (Optional) Bgw的描述，只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符。
        :param vifIds: (Optional) Bgw上通道Id列表
        :param vpcAttachmentIds: (Optional) Bgw上vpc接口Id列表
        :param vpnConnectionIds: (Optional) Bgw上vpn连接Id列表
        :param azType: (Optional) 边界网关az类型，取值：standard(标准BGW)，edge(边缘BGW)
        :param az: (Optional) 边界网关可用区，边缘BGW必须指定可用区，中心BGW返回空
        :param createdTime: (Optional) Bgw的创建时间
        """

        self.bgwId = bgwId
        self.bgwName = bgwName
        self.description = description
        self.vifIds = vifIds
        self.vpcAttachmentIds = vpcAttachmentIds
        self.vpnConnectionIds = vpnConnectionIds
        self.azType = azType
        self.az = az
        self.createdTime = createdTime
