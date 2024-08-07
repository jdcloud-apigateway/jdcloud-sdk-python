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


class ActivityVo(object):

    def __init__(self, id=None, uuid=None, activityName=None, activityTime=None, address=None, scale=None, form=None, formStr=None, clueNum=None):
        """
        :param id: (Optional) 活动id
        :param uuid: (Optional) 活动uuid
        :param activityName: (Optional) 活动名称
        :param activityTime: (Optional) 活动日期
        :param address: (Optional) 活动地点
        :param scale: (Optional) 活动规模
        :param form: (Optional) 活动形式
        :param formStr: (Optional) 活动形式
        :param clueNum: (Optional) 线索数
        """

        self.id = id
        self.uuid = uuid
        self.activityName = activityName
        self.activityTime = activityTime
        self.address = address
        self.scale = scale
        self.form = form
        self.formStr = formStr
        self.clueNum = clueNum
