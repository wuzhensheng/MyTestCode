# -*- coding: UTF-8 -*-
import requests,json

#创建session对象，模拟浏览器的cookie管理
session = requests.session()
jsonres = {}


#使用session请求接口
jsonres = session.post('http://112.71.191.8081/inter/HTTP/auth')
if jsonres['status'] == 200 and not (jsonres['token'] is None):
    print('pass')
else:
    print('fail')

#添加头
session.headers['token'] = ''
result = session.post('http://112.71.191.8081/inter/HTTP/auth')
jsonres = json.loads(result.text)
if jsonres['status'] == 200:
    print('pass')
else:
    print('fail')