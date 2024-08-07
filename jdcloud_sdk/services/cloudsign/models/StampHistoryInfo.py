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


class StampHistoryInfo(object):

    def __init__(self, id=None, createdBy=None, operatorPhone=None, createTime=None, operatorType=None, note=None):
        """
        :param id: (Optional) 印章操作记录ID
        :param createdBy: (Optional) 操作主体
        :param operatorPhone: (Optional) 联系方式
        :param createTime: (Optional) 操作时间
        :param operatorType: (Optional) 操作类型：创建印章、编辑印章、删除印章、加盖印章
        :param note: (Optional) 备注——合同信息
        """

        self.id = id
        self.createdBy = createdBy
        self.operatorPhone = operatorPhone
        self.createTime = createTime
        self.operatorType = operatorType
        self.note = note
