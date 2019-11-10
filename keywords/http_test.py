# -*- coding: UTF-8 -*-
import requests, json
from keywords.httpkeys import HTTP

url = 'http://112.74.191.10:8081/inter/HTTP/auth'

#创建HTTP实例对象，用来调用关键字
http = HTTP()
# http.post('http://112.74.191.10:8081/inter/HTTP/auth')
# http.assertquals('status', 200)

#传入token为''
# http.addheader('token', '')
# http.post(path=url)
# http.assertquals('status', 200)
# print(http.jsonres['token'])
#
# http.assertquals('token', http.jsonres['token'])
http.post(path=url)
http.assertquals('status', 200)
http.seavjson('t', 'token')
http.addheader('token', '{t}')
print(http.session.headers)


#登录一个用户，查询用户信息
http.post('http://112.74.191.10:8081/inter/HTTP/login', 'username=Tester55&password=123456')
http.assertquals('status', 200)
http.seavjson('id', 'userid')
http.post('http://112.74.191.10:8081/inter/HTTP/getUserInfo', 'id={id}')
http.assertquals('status', 200)
http.post('http://112.74.191.10:8081/inter/HTTP/logout')
http.assertquals('status', 200)