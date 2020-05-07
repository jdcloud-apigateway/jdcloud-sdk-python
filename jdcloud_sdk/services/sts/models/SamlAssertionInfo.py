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


class SamlAssertionInfo(object):

    def __init__(self, subjectType=None, subject=None, recipient=None, issuer=None):
        """
        :param subjectType: (Optional) SAML断言中NameID的格式
        :param subject: (Optional) SAML断言中Subject.NameID字段值
        :param recipient: (Optional) SAML断言中Subject.SubjectConfirmation.SubjectConfirmationData字段中Recipient字段值
        :param issuer: (Optional) SAML断言中Issuer字段值
        """

        self.subjectType = subjectType
        self.subject = subject
        self.recipient = recipient
        self.issuer = issuer