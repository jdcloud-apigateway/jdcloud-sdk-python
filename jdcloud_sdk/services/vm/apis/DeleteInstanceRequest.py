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


class DeleteInstanceRequest(JDCloudRequest):
    """
    
删除一台云主机实例。

详细操作说明请参考帮助文档：[删除实例](https://docs.jdcloud.com/cn/virtual-machines/delete-instance)

## 接口说明
- 不可以删除包年包月未到期的云主机。如果云主机为包年包月已到期的，并且用户处于白名单中，也不允许删除。
- 不可以删除没有计费信息的云主机，该情况只限于创建过程中出现了异常。
- 云主机状态必须为运行 `running`、停止 `stopped`、错误 `error`、状态，同时云主机没有正在进行中的任务才可以删除。
- 如果云主机中挂载的数据盘为按配置计费的云硬盘且 `AutoDelete` 属性为 `true`，那么数据盘会随云主机一起删除。
- 云主机中绑定的弹性公网IP不会随云主机一起删除，如果不需要保留，需要单独进行删除，需要使用者注意。
- 如出现不能删除的情况请 [提交工单](https://ticket.jdcloud.com/applyorder/submit) 或联系京东云客服。
 [MFA enabled]
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteInstanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteInstanceParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域ID。
        :param instanceId: 云主机ID。
        """

        self.regionId = regionId
        self.instanceId = instanceId

