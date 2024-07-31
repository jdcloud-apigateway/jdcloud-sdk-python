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


class SaveUserAzVo(object):

    def __init__(self, paz=None, laz=None, cloudManufacturer=None):
        """
        :param paz: (Optional) 物理可用区
        :param laz: (Optional) 逻辑可用区
        :param cloudManufacturer: (Optional) 云厂商
        """

        self.paz = paz
        self.laz = laz
        self.cloudManufacturer = cloudManufacturer
