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


class UranusTaskInfoNodeReq(object):

    def __init__(self, taskCode=None, taskChangeStatus=None, taskChangeStatusDesc=None, gravityStatus=None, gravityStatusDesc=None):
        """
        :param taskCode: (Optional) 节点code
        :param taskChangeStatus: (Optional) 状态 集合
        :param taskChangeStatusDesc: (Optional) 发布变更状态描述
        :param gravityStatus: (Optional) 作业状态
        :param gravityStatusDesc: (Optional) 作业状态描述
        """

        self.taskCode = taskCode
        self.taskChangeStatus = taskChangeStatus
        self.taskChangeStatusDesc = taskChangeStatusDesc
        self.gravityStatus = gravityStatus
        self.gravityStatusDesc = gravityStatusDesc
