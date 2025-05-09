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


class PodTemplateContainer(object):

    def __init__(self, name=None, command=None, args=None, env=None, image=None, secret=None, imageCacheId=None, tty=None, workingDir=None, livenessProbe=None, readinessProbe=None, resources=None, systemDisk=None, volumeMounts=None):
        """
        :param name: (Optional) 模板内容器名称
        :param command: (Optional) 容器执行的命令。
        :param args: (Optional) 容器执行命令的参数。
        :param env: (Optional) 容器执行的环境变量。
        :param image: (Optional) 容器镜像名称。
        :param secret: (Optional) 容器镜像仓库认证信息。
        :param imageCacheId: (Optional) 容器镜像缓存ID。
        :param tty: (Optional) 容器是否分配tty。
        :param workingDir: (Optional) 容器的工作目录。
        :param livenessProbe: (Optional) 容器存活探针配置
        :param readinessProbe: (Optional) 容器服务就绪探针配置
        :param resources: (Optional) 容器计算资源配置
        :param systemDisk: (Optional) 容器计算资源配置
        :param volumeMounts: (Optional) 容器计算资源配置
        """

        self.name = name
        self.command = command
        self.args = args
        self.env = env
        self.image = image
        self.secret = secret
        self.imageCacheId = imageCacheId
        self.tty = tty
        self.workingDir = workingDir
        self.livenessProbe = livenessProbe
        self.readinessProbe = readinessProbe
        self.resources = resources
        self.systemDisk = systemDisk
        self.volumeMounts = volumeMounts
