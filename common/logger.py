# coding:utf-8
import logging
import os,time
# log_path是存放日志的路径
cur_path = os.path.dirname(__file__)

log_path = os.path.join(os.path.dirname(cur_path), 'logs')

# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):os.mkdir(log_path)
class Log():
    def __init__(self):
        #创建logger
        self.logname=os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #创建格式
        self.formatter=logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s-%(message)s')
    #用于写入控制台
    def __console(self,level,message):
        #添加用于写入控制台的handle
        consoleHandler=logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)
        #添加输出格式
        consoleHandler.setFormatter(self.formatter)
        #给logger添加handler
        self.logger.addHandler(consoleHandler)

        #添加用于写入文件的handler
        fileHandler=logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fileHandler.setLevel(logging.DEBUG)
        #handler添加格式
        fileHandler.setFormatter(self.formatter)
        # 给logger添加handler
        self.logger.addHandler(fileHandler)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(consoleHandler)
        self.logger.removeHandler(fileHandler)
        # 关闭打开的文件
        fileHandler.close()
    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)















