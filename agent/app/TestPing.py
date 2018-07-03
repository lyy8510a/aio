#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/6/21 下午4:33.
"""

from core import global_config
from core.base import BaseController
import time,sys

class TestPing(BaseController):


    def ping(self):
        try:
            if(self.no_pong_num <=  global_config['SERVER_NO_PONG_NUM']):
                result = self.checkPort(global_config['SERVER_HOST'],global_config['SERVER_PORT'])
                result2 = self.checkPort(global_config['PROXY_HOST'],global_config['PROXY_PORT'])
                if(result == 0 or result2 == 0):
                    self.no_pong_num = self.no_pong_num + 1
                time.sleep(1)
            else:
                # 超过指定次数，断开循环
                self.err_record('test.ping','该端口不通超过{0}次'.format(global_config['SERVER_NO_PONG_NUM']))
                sys.exit(1)
        except Exception as e:
            BaseController().err_record('test.ping', '问题为：{0}'.format(e))
            sys.exit(1)



if __name__ == '__main__':
    TestPing()