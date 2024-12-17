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


class K8sNameSpaceSelectorSpec(object):

    def __init__(self, allNamespace, excludeNamespace=None, namespace=None):
        """
        :param allNamespace:  是否全部命名空间
        :param excludeNamespace: (Optional) 需要排除的namespace。可以多个，用分隔号分割,例如A,B
        :param namespace: (Optional) namespace-> stdout+全部容器 模式下 可以多个，用分隔号分割,例如A,B;
        """

        self.allNamespace = allNamespace
        self.excludeNamespace = excludeNamespace
        self.namespace = namespace