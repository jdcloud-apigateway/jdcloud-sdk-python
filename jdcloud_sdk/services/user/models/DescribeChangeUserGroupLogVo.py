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


class DescribeChangeUserGroupLogVo(object):

    def __init__(self, operator=None, pin=None, createTime=None, userGroup=None, status=None, updateTime=None):
        """
        :param operator: (Optional) 操作人
        :param pin: (Optional) pin
        :param createTime: (Optional) 创建时间
        :param userGroup: (Optional) 用分组
        :param status: (Optional) 状态
        :param updateTime: (Optional) 修改时间
        """

        self.operator = operator
        self.pin = pin
        self.createTime = createTime
        self.userGroup = userGroup
        self.status = status
        self.updateTime = updateTime