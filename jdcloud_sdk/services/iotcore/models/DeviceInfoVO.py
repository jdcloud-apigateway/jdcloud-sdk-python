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


class DeviceInfoVO(object):

    def __init__(self, activateTime=None, connectAgentDeviceId=None, createTime=None, customProfiles=None, deviceId=None, deviceName=None, deviceTagList=None, globalProfiles=None, lastConnectTime=None, lastDisconnectTime=None, latitude=None, longitude=None, macAddress=None, manufactureId=None, manufactureName=None, nodeType=None, lastReportTime=None, status=None, thingModelId=None, thingModelVersion=None, thingTypeCode=None, thingTypeName=None, uniqueId=None, updateTime=None):
        """
        :param activateTime: (Optional) 激活时间
        :param connectAgentDeviceId: (Optional) 代理设备id
        :param createTime: (Optional) 创建时间
        :param customProfiles: (Optional) 
        :param deviceId: (Optional) 设备标识id
        :param deviceName: (Optional) 设备名称
        :param deviceTagList: (Optional) 
        :param globalProfiles: (Optional) 
        :param lastConnectTime: (Optional) 最近一次上线时间
        :param lastDisconnectTime: (Optional) 最近一次离线时间
        :param latitude: (Optional) 纬度
        :param longitude: (Optional) 经度
        :param macAddress: (Optional) 设备mac地址
        :param manufactureId: (Optional) 生产厂商ID
        :param manufactureName: (Optional) 生产厂商名称
        :param nodeType: (Optional) 设备连接类型
        :param lastReportTime: (Optional) 设备上报数据更新时间
        :param status: (Optional) 设备状态：0 停用;1 未激活;2 离线;3 在线
        :param thingModelId: (Optional) 物模型ID
        :param thingModelVersion: (Optional) 物模型版本号
        :param thingTypeCode: (Optional) 物类型ID
        :param thingTypeName: (Optional) 物类型名称
        :param uniqueId: (Optional) 设备物理ID
        :param updateTime: (Optional) 更新时间
        """

        self.activateTime = activateTime
        self.connectAgentDeviceId = connectAgentDeviceId
        self.createTime = createTime
        self.customProfiles = customProfiles
        self.deviceId = deviceId
        self.deviceName = deviceName
        self.deviceTagList = deviceTagList
        self.globalProfiles = globalProfiles
        self.lastConnectTime = lastConnectTime
        self.lastDisconnectTime = lastDisconnectTime
        self.latitude = latitude
        self.longitude = longitude
        self.macAddress = macAddress
        self.manufactureId = manufactureId
        self.manufactureName = manufactureName
        self.nodeType = nodeType
        self.lastReportTime = lastReportTime
        self.status = status
        self.thingModelId = thingModelId
        self.thingModelVersion = thingModelVersion
        self.thingTypeCode = thingTypeCode
        self.thingTypeName = thingTypeName
        self.uniqueId = uniqueId
        self.updateTime = updateTime
