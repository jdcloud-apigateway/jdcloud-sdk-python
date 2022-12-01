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


class DmsOgTableRule(object):

    def __init__(self, autoTableShardingInfo=None, tableShardingInfo=None):
        """
        :param autoTableShardingInfo: (Optional) 自动分表信息。
        :param tableShardingInfo: (Optional) 分表信息。
        """

        self.autoTableShardingInfo = autoTableShardingInfo
        self.tableShardingInfo = tableShardingInfo
