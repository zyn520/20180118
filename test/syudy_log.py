import logging
import os

#创建一个logger
logger1=logging.getLogger()
logger1.setLevel(logging.DEBUG)

#创建hander用于写入文件
fileHandler=logging.FileHandler('0103.log')
fileHandler.setLevel(logging.DEBUG)

#创建handler用于些人控制台
consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

#定义handler的输出格式
formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

#给handler添加格式
fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

#给logger添加handler
logger1.addHandler(fileHandler)
logger1.addHandler(consoleHandler)

logger1.info('abc')



