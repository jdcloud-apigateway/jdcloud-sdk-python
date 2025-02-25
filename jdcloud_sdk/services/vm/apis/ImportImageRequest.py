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


class ImportImageRequest(JDCloudRequest):
    """
    
导入私有镜像。

详细操作说明请参考帮助文档：[导入私有镜像](https://docs.jdcloud.com/cn/virtual-machines/import-private-image)

## 接口说明
- 导入后的镜像将以 `云硬盘系统盘镜像` 格式作为私有镜像使用，同时会自动生成与导入镜像关联的快照。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ImportImageRequest, self).__init__(
            '/regions/{regionId}/images:import', 'POST', header, version)
        self.parameters = parameters


class ImportImageParameters(object):

    def __init__(self,regionId, architecture, osType, platform, diskFormat, systemDiskSizeGB, imageUrl, imageName, ):
        """
        :param regionId: 地域ID。
        :param architecture: 镜像架构。取值范围：`x86_64、arm64`。
        :param osType: 镜像的操作系统类型。取值范围：`windows、linux`。
        :param platform: 镜像的操作系统平台名称。
取值范围：`Ubuntu、CentOS、Windows Server、Other Linux、Other Windows`。

        :param diskFormat: 磁盘格式，取值范围：`qcow2、vhd、vmdk、raw`。
        :param systemDiskSizeGB: 以此镜像需要制作的系统盘的默认大小，单位GB。最小值40，最大值500，要求值是10的整数倍。
        :param imageUrl: 要导入镜像的对象存储外链地址。
        :param imageName: 导入镜像的自定义名称。参考 [公共参数规范](https://docs.jdcloud.com/virtual-machines/api/general_parameters)。
        """

        self.regionId = regionId
        self.architecture = architecture
        self.osType = osType
        self.platform = platform
        self.diskFormat = diskFormat
        self.systemDiskSizeGB = systemDiskSizeGB
        self.imageUrl = imageUrl
        self.osVersion = None
        self.imageName = imageName
        self.description = None
        self.forceImport = None
        self.dataDisks = None
        self.clientToken = None
        self.bootMode = None

    def setOsVersion(self, osVersion):
        """
        :param osVersion: (Optional) 镜像的操作系统版本。
        """
        self.osVersion = osVersion

    def setDescription(self, description):
        """
        :param description: (Optional) 导入镜像的描述信息。参考 [公共参数规范](https://docs.jdcloud.com/virtual-machines/api/general_parameters)。
        """
        self.description = description

    def setForceImport(self, forceImport):
        """
        :param forceImport: (Optional) 是否强制导入。强制导入会忽略镜像的合规性检测。默认为false。
        """
        self.forceImport = forceImport

    def setDataDisks(self, dataDisks):
        """
        :param dataDisks: (Optional) 云盘快照信息。

        """
        self.dataDisks = dataDisks

    def setClientToken(self, clientToken):
        """
        :param clientToken: (Optional) 用户导出镜像的幂等性保证。每次导出请传入不同的值，如果传值与某次的clientToken相同，则返还同一个请求结果，不能超过64个字符。
        """
        self.clientToken = clientToken

    def setBootMode(self, bootMode):
        """
        :param bootMode: (Optional) 镜像启动模式，默认bios，支持范围：`bios`、`uefi`。
        """
        self.bootMode = bootMode

