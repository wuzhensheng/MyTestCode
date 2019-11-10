# -*- coding: UTF-8 -*-
import requests,json

#创建一个http接口请求的关键字类
class HTTP:
    #构造函数，实例化示例变量
    def __init__(self):
        #创建session对象，模拟浏览器的cookie管理
        self.session = requests.session()
        # 存放json解析后的结果
        self.jsonres =  {}
        # 用来保存数据，实现关联
        self.params = {}

    # 定义post实例方法，用来发送post请求
    def post(self, path, data=None):
        # 如果需要传参，就掉post，传递data
        if data is None:
            result = self.session.post(path)
        else:
            #替换参数
            data = self.__getParams(data)
            #转为字典
            data = self.__todict(data)
            #发送请求
            result = self.session.post(path, data=data)

        self.jsonres = json.loads(result.text)
        print(self.jsonres)

    # 定义断言相等的关键字，用来判断json的key对应的值和期望相等
    def assertquals(self, key, value):
        if self.jsonres[key] == value:
            print('Pass')
        else:
            print('Fail')

    # 定义一个传入header头信息的方法
    def addheader(self, key, value):
        value = self.__getParams(value)
        self.session.headers[key] = value

    def seavjson(self, p, key):
        self.params[p] = self.jsonres[key]

    def __getParams(self, s):
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])
        return s
    # 将一个标准的url地址转成字典
    def __todict(self,data):
        """
        username=Test55&password=123456
        {'username': 'Test55', 'password': '123456'}
        :param data:
        :return:
        """
        #分割参数个数
        httpparams = {}
        param = data.split('&')
        for ss in param:
            #把键值对分开
            p = ss.split('=')
            httpparams[p[0]] = p[1]
        print(httpparams)
        return httpparams

