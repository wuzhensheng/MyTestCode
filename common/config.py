# coding:utf8
from common import logger
from common.txt import Txt

# 全局变量，用来存储配置
config = {}


def get_config(path):
    """
    用来格式化打印日志到文件和控制台
    :param path: 配置文件路径
    :return: 返回配置文件dict
    """
    global config
    # 重新或趋时，先清空配置
    config.clear()
    txt = Txt(path)
    data = txt.read()

    for s in data:
        # 跳过注释
        if s.startswith('#'):
            continue

        try:
            key = s[0:s.find('=')]
            value = s[s.find('=') + 1:s.__len__()]
            config[key] = value
        except Exception as e:
            logger.warn('配置文件格式错误，请检查' + str(s))
            logger.execption(e)
    return config


dict = get_config('../lib/conf/conf.txt')
print(dict)