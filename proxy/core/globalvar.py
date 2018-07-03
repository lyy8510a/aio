#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/6/21 下午1:51.
"""
import sys,os

from core import global_config
from config import Config as BaseConfig
if BaseConfig.ENV == 'Dev':
    from config import DevConfig as Config
else:
    from config import ProdConfig as Config




# 设置全局变量
class Globalvar(object):
    def __init__(self):

        self.config_attr_keys = []
        self.main()

    def get_attr_key(self):
        for item in dir(Config):
            if not item.startswith('__'):
                self.config_attr_keys.append(item)

    def get_attr_value(self,keys):
        for key in keys:
            global_config[key]=eval("Config."+key)

    def main(self):
        self.get_attr_key()
        self.get_attr_value(self.config_attr_keys)


if __name__ == '__main__':
    Globalvar()





