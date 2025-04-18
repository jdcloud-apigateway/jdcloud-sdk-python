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


class WorkspaceCreateReq(object):

    def __init__(self, userPin=None, workspaceId=None, workspaceName=None, manager=None, workspaceDescription=None, workspaceModel=None, engineType=None, calculateResourceCode=None, integrationResourceCode=None, needBundleProject=None, bundleDevProjectReq=None, bundleProdProjectReq=None):
        """
        :param userPin: (Optional) 
        :param workspaceId: (Optional) 
        :param workspaceName: (Optional) 
        :param manager: (Optional) 
        :param workspaceDescription: (Optional) 
        :param workspaceModel: (Optional) 
        :param engineType: (Optional) 
        :param calculateResourceCode: (Optional) 
        :param integrationResourceCode: (Optional) 
        :param needBundleProject: (Optional) 
        :param bundleDevProjectReq: (Optional) 
        :param bundleProdProjectReq: (Optional) 
        """

        self.userPin = userPin
        self.workspaceId = workspaceId
        self.workspaceName = workspaceName
        self.manager = manager
        self.workspaceDescription = workspaceDescription
        self.workspaceModel = workspaceModel
        self.engineType = engineType
        self.calculateResourceCode = calculateResourceCode
        self.integrationResourceCode = integrationResourceCode
        self.needBundleProject = needBundleProject
        self.bundleDevProjectReq = bundleDevProjectReq
        self.bundleProdProjectReq = bundleProdProjectReq
