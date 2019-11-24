# -*- coding: UTF-8 -*-
import requests
import json
from keywords.httpkeys import HTTP
import inspect

# eval函数:获取字符串表达式的结果
a = '1+1'
a1 = '{1:2}'
b = eval(a)
print(b)
print(a1)
"""
反射获取关键字：
反射获取函数：func = getattr(HTTp, 'post')
反射获取关子健参数：inspect.getfullargspec(func).__str__()
反射获取关键字描述: func.__doc__
"""
# a = 'post'
# http = HTTP()
# func = getattr(http, a)
# # func(http, 'http://112.74.191.10:8080/inter/HTTP/auth')
# args = inspect.getfullargspec(func).__str__()
# args = args[args.find('args=') + 5:args.find(', varargs')]
# args = eval(args)
# args.remove('self')
# print(len(args))
# print(func.__doc__)

a = ['', '', '无token', 'post', 'http://112.74.191.10:8081/inter/HTTP/auth', '', '', '', '']
http = HTTP()
func = getattr(http, a[3])
args = inspect.getfullargspec(func).__str__()
args = args[args.find('args=') + 5:args.find(', varargs')]
args = eval(args)
args.remove('self')

l = len(args)
if l < 1:
    func()

if l < 2:
    func(a[4])

if l < 3:
    func(a[4], a[5])

# if l <4:
#     func(a[4], a[5] ,a[6])
