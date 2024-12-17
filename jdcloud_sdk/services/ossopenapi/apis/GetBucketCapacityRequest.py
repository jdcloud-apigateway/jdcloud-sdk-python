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


class GetBucketCapacityRequest(JDCloudRequest):
    """
    根据type获取bucket用量数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetBucketCapacityRequest, self).__init__(
            '/regions/{regionId}/capacity/', 'POST', header, version)
        self.parameters = parameters


class GetBucketCapacityParameters(object):

    def __init__(self,regionId, capacityTypes, method, ):
        """
        :param regionId: 区域ID
        :param capacityTypes: <p>查询用量数据类型：</p><br><code>1000040</code>:标准存储<br><code>1000041</code>:低冗余存储<br><code>1000042</code>:归档存储<br><code>1000043</code>归档overHead存储:<br><code>1000044</code>低频存储:<br><code>1000045</code>低频overHead存储:<br><code>1</code>:内网GET流量<br><code>2</code>:内网HEAD流量<br><code>3</code>:内网PUT流量<br><code>4</code>:内网POST流量<br><code>5</code>:内网DELETE流量<br><code>6</code>:内网OPTIONS流量<br><code>7</code>:内网TRACE流量<br><code>11</code>:外网GET流量<br><code>12</code>:外网HEAD流量<br><code>13</code>:外网PUT流量<br><code>14</code>:外网POST流量<br><code>15</code>:外网DELETE流量<br><code>16</code>:外网OPTIONS流量<br><code>17</code>:外网TRACE流量<br><code>21</code>:CDN GET流量<br><code>22</code>:CDN HEAD流量<br><code>23</code>:CDN PUT流量<br><code>24</code>:CDN POST流量<br><code>25</code>:CDN DELETE流量<br><code>26</code>:CDN OPTIONS流量<br><code>27</code>:CDN TRACE流量<br><code>31</code>:内网GET数<br><code>32</code>:内网HEAD数<br><code>33</code>:内网PUT数<br><code>34</code>:内网POST数<br><code>35</code>:内网DELETE数<br><code>36</code>:内网OPTIONS数<br><code>37</code>:内网TRACE数<br><code>51</code>:外网GET数<br><code>52</code>:外网HEAD数<br><code>53</code>:外网PUT数<br><code>54</code>:外网POST数<br><code>55</code>:外网DELETE数<br><code>56</code>:外网OPTIONS数<br><code>57</code>:外网TRACE数<br><code>61</code>:CDN GET数<br><code>62</code>:CDN HEAD数<br><code>63</code>:CDN PUT数<br><code>64</code>:CDN POST数<br><code>65</code>:CDN DELETE数<br><code>66</code>:CDN OPTIONS数<br><code>67</code>:CDN TRACE数<br><code>71</code>:归档提前删除<br><code>72</code>:低频提前删除<br><code>81</code>:归档取回Bulk<br><code>82</code>:归档取回Std<br><code>83</code>:归档取回Exp<br><code>84</code>:低频数据取回

        :param method: 返回数据的方式： <code>1</code>:recent(区间值), <code>2</code>:current(当前值。method = 2 时如果查询当前值时传入beginTime，则按照beginTime时间来进行查询；如果不传beginTime，则按照后端系统时间查询。)
        """

        self.regionId = regionId
        self.capacityTypes = capacityTypes
        self.beginTime = None
        self.endTime = None
        self.periodType = None
        self.method = method
        self.bucketNames = None

    def setBeginTime(self, beginTime):
        """
        :param beginTime: (Optional) 开始时间，使用UTC时间，格式为：YYYY-MM-DDTHH:mm:ss'Z'
        """
        self.beginTime = beginTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 结束时间，使用UTC时间，格式为：YYYY-MM-DDTHH:mm:ss'Z'
        """
        self.endTime = endTime

    def setPeriodType(self, periodType):
        """
        :param periodType: (Optional) 查询数据的聚合方式:<br><code>0</code>:all, 最大查询区间365天 <br><code>1</code>:hour，最大查询区间31天。默认1<br><code>2</code>:day, 最大查询区间365天。
        """
        self.periodType = periodType

    def setBucketNames(self, bucketNames):
        """
        :param bucketNames: (Optional) 查询的bucket Names。如果查询用户全部Bucket,则不传
        """
        self.bucketNames = bucketNames
