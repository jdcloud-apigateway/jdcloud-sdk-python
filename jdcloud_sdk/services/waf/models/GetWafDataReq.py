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


class GetWafDataReq(object):

    def __init__(self, userPin=None, startTime=None, endTime=None):
        """
        :param userPin: (Optional) userPins
        :param startTime: (Optional) 起始时间, utc时间戳
        :param endTime: (Optional) 结束时间, utc时间戳，必须大于起始时间
        """

        self.userPin = userPin
        self.startTime = startTime
        self.endTime = endTime
