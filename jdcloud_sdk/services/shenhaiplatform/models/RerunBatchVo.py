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


class RerunBatchVo(object):

    def __init__(self, id=None, remark=None, operator=None, status=None, statusLabel=None, submitSuccessCount=None, submitFailCount=None, submitPendingCount=None, submitSubmittingCount=None, submitTotalCount=None, createTime=None):
        """
        :param id: (Optional) 批次id
        :param remark: (Optional) 重跑原因
        :param operator: (Optional) 操作人员
        :param status: (Optional) 状态
        :param statusLabel: (Optional) 状态-展示
        :param submitSuccessCount: (Optional) 提交成功数量
        :param submitFailCount: (Optional) 提交失败数量
        :param submitPendingCount: (Optional) 提交待处理数量
        :param submitSubmittingCount: (Optional) 提交中数量
        :param submitTotalCount: (Optional) 提交总数
        :param createTime: (Optional) 操作时间
        """

        self.id = id
        self.remark = remark
        self.operator = operator
        self.status = status
        self.statusLabel = statusLabel
        self.submitSuccessCount = submitSuccessCount
        self.submitFailCount = submitFailCount
        self.submitPendingCount = submitPendingCount
        self.submitSubmittingCount = submitSubmittingCount
        self.submitTotalCount = submitTotalCount
        self.createTime = createTime
