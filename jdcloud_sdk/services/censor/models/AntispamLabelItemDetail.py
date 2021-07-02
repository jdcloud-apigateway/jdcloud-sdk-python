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


class AntispamLabelItemDetail(object):

    def __init__(self, hitInfos=None, anticheatInfo=None, imageTagInfo=None, imageListInfo=None, hitLocationInfos=None):
        """
        :param hitInfos: (Optional) 针对命中sublabel的补充说明
        :param anticheatInfo: (Optional) 命中反作弊相关策略，hitType为反垃圾命中类型，1：数据异常 2：行为模型 3：设备模型 4：业务类型 5：校验异常 6：模拟器 7：越狱或root 8：浏览器异常 9：ip异常 10：京东黑名单 11：自定义黑名单 12：自定义白名单
        :param imageTagInfo: (Optional) 命中标签详细信息，对于返回的hintInfo的解释说明，可能为空
        :param imageListInfo: (Optional) 
        :param hitLocationInfos: (Optional) 
        """

        self.hitInfos = hitInfos
        self.anticheatInfo = anticheatInfo
        self.imageTagInfo = imageTagInfo
        self.imageListInfo = imageListInfo
        self.hitLocationInfos = hitLocationInfos
