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


class CreateBackupPlan(object):

    def __init__(self, name, servicePackage, chargeSpec, ):
        """
        :param name:  备份计划名称，支持中文、数字、大小写字母、英文下划线“_”、减号“-”，且不少于2字符不超过64字符
        :param servicePackage:  DBS服务包类型是枚举值， dbs.common.package 表示基础服务包，不含备份流量
        :param chargeSpec:  购买规格
        """

        self.name = name
        self.servicePackage = servicePackage
        self.chargeSpec = chargeSpec
