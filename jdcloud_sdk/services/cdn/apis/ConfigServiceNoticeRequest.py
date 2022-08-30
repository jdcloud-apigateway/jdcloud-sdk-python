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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class ConfigServiceNoticeRequest(JDCloudRequest):
    """
    配置服务通知接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ConfigServiceNoticeRequest, self).__init__(
            '/serviceNotice:config', 'POST', header, version)
        self.parameters = parameters


class ConfigServiceNoticeParameters(object):

    def __init__(self,):
        """
        """

        self.id = None
        self.noticeType = None
        self.noticeWay = None
        self.noticeTo = None
        self.noticeCC = None
        self.noticeContent = None
        self.noticePeriod = None
        self.noticeStatus = None

    def setId(self, id):
        """
        :param id: (Optional) id 修改操作必传
        """
        self.id = id

    def setNoticeType(self, noticeType):
        """
        :param noticeType: (Optional) 通知类型,取值[reportForm],reportForm:报表.
        """
        self.noticeType = noticeType

    def setNoticeWay(self, noticeWay):
        """
        :param noticeWay: (Optional) 通知方式,取值[mail],mail:邮件.
        """
        self.noticeWay = noticeWay

    def setNoticeTo(self, noticeTo):
        """
        :param noticeTo: (Optional) 通知接收人,多个用逗号隔开.
        """
        self.noticeTo = noticeTo

    def setNoticeCC(self, noticeCC):
        """
        :param noticeCC: (Optional) 通知抄送人,多个用逗号隔开.
        """
        self.noticeCC = noticeCC

    def setNoticeContent(self, noticeContent):
        """
        :param noticeContent: (Optional) 通知正文.
        """
        self.noticeContent = noticeContent

    def setNoticePeriod(self, noticePeriod):
        """
        :param noticePeriod: (Optional) 通知周期,取值[daily,weekly,monthly].
        """
        self.noticePeriod = noticePeriod

    def setNoticeStatus(self, noticeStatus):
        """
        :param noticeStatus: (Optional) 通知状态，取值[init,start,stop]
        """
        self.noticeStatus = noticeStatus

