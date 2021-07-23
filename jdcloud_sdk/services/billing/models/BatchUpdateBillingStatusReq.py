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


class BatchUpdateBillingStatusReq(object):

    def __init__(self, serviceCode, resourceIds, action, mainResourceId=None, comment=None):
        """
        :param serviceCode:  产品编码
        :param mainResourceId: (Optional) 主资源ID
        :param resourceIds:  资源ID列表
        :param action:  操作(STOP 停止计费 ; RESTART 恢复计费)
        :param comment: (Optional) 操作说明
        """

        self.serviceCode = serviceCode
        self.mainResourceId = mainResourceId
        self.resourceIds = resourceIds
        self.action = action
        self.comment = comment
