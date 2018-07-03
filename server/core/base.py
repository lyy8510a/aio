#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/6/21 下午4:01.
"""


from core import global_config
import time,socket


class BaseController(object):
    def __init__(self):
        # ping不通次数
        self.no_pong_num = 0


    # 检查端口连通性
    def checkPort(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return 1
        except:
            return 0
    # 记录日志
    def err_record(self,type,logs):
        content = "{0}:[{1}]-{2} \r\n".format(self.getDateTime(),type,logs)
        self.writeFile(global_config['ERRLOG_PATH'],content)



    def record(self,type,logs):
        content = "{0}:[{1}]-{2} \r\n".format(self.getDateTime(), type, logs)
        self.writeFile(global_config['ACCESSLOG_PATH'], content)

    # 写文件的方法
    def writeFile(self,path,content):
        try:
            with open(path,'a+') as f:
                f.write(content)
            return True
        except Exception as e:
            return e

    # 日期+时间
    def getDateTime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #日期
    def getDate(self):
        return time.strftime("%Y-%m-%d", time.localtime())
    #时间
    def getTime(self):
        return time.strftime("%H:%M:%S", time.localtime())


if __name__ == '__main__':
    BaseController()