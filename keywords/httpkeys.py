# -*- coding: UTF-8 -*-
import requests, json


# 创建一个http接口请求的关键字类
class HTTP:
    # 构造函数，实例化示例变量
    def __init__(self, writer):
        # 创建session对象，模拟浏览器的cookie管理
        self.session = requests.session()
        # 存放json解析后的结果
        self.jsonres = {}
        # 用来保存数据，实现关联
        self.params = {}
        self.url = {}
        # 写入结果的excel


        self.writer = writer

    # 设置地址
    def seturl(self, url):
        if url.startswith('http') or url.startswith('https'):
            self.url = url
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        else:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, 'error: url地址不合法')

        # 定义post实例方法，用来发送post请求

    def post(self, path, data=None):
        """
        # 定义post示例方法，用来发送post请求
        :param path: url路径
        :param data: 键值对传参的字符串
        :return: 无返回值
        """
        try:
            if not path.startswith('http'):
                path = self.url + '/' + path

            # 如果需要传参，就掉post，传递data
            if data is None or data == '':
                result = self.session.post(path)
            else:
                # 替换参数
                data = self.__getParams(data)
                # 转为字典
                data = self.__todict(data)
                # 发送请求
                result = self.session.post(path, data=data)

            self.jsonres = json.loads(result.text)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
        except Exception as e:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            print(e)

    # 定义断言相等的关键字，用来判断json的key对应的值和期望相等
    def assertequals(self, key, value):
        res = ''
        try:
            res = str(self.jsonres[key])
        except Exception as e:
            print(e)

        if res == str(value):
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(res))
        else:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(res))

    # 定义一个传入header头信息的方法
    def addheader(self, key, value):
        value = self.__getParams(value)
        self.session.headers[key] = value
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        self.writer.write(self.writer.row, self.writer.clo + 1, str(value))

    def savejson(self, key, p):
        res = ''
        try:
            res = self.jsonres[key]
        except Exception as e:
            print(e)
        self.params[p] = res
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        self.writer.write(self.writer.row, self.writer.clo + 1, str(res))

    def __getParams(self, s):
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])
        return s

    # 将一个标准的url地址转成字典
    def __todict(self, data):
        """
        username=Test55&password=123456
        {'username': 'Test55', 'password': '123456'}
        :param data:
        :return:
        """
        # 分割参数个数
        httpparams = {}
        param = data.split('&')
        for ss in param:
            # 把键值对分开
            p = ss.split('=')
            if len(p) > 1:
                httpparams[p[0]] = p[1]
        print(httpparams)
        return httpparams
