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


class GpmdOpenApiResponseCalcJobResultDTO(object):

    def __init__(self, success=None, result=None, code=None, msg=None, _REQ_SEQ_NO_=None):
        """
        :param success: (Optional) 成功标识，1成功，0失败
        :param result: (Optional) 
        :param code: (Optional) 返回状态码
        :param msg: (Optional) 返回状态信息
        :param _REQ_SEQ_NO_: (Optional) 返回请求流水号
        """

        self.success = success
        self.result = result
        self.code = code
        self.msg = msg
        self._REQ_SEQ_NO_ = _REQ_SEQ_NO_
