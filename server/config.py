#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/6/21 下午1:27.
"""
import os

class Config(object):
    """Base config class."""
    # 版本
    VERSION = 'v0.0.1'
    # 项目名称
    PROJECTNAME = 'aio_server'

    #环境
    ENV = 'Dev'
    # ENV = 'Prod'
    # 基础路径
    BASE_PATH = os.path.dirname(__file__)

    # PID路径
    PID_PATH = BASE_PATH+'/aio_server.pid'
    # 日志路径
    LOG_PATH = BASE_PATH+'/logs/aio_server.log'
    ERRLOG_PATH = BASE_PATH+'/logs/aio_server_errlogs.log'
    ACCESSLOG_PATH = BASE_PATH+'/logs/aio_server_accesslogs.log'


class ProdConfig(Config):
    """Production config class."""

    # 服务端主机IP
    SERVER_HOST = '127.0.0.1'
    PROXY_HOST = '127.0.0.1'
    SERVER_PORT = 5556
    PROXY_PORT = 5557





class DevConfig(Config):
    """Development config class."""

    # 服务端主机IP
    SERVER_HOST = '127.0.0.1'
    PROXY_HOST = '127.0.0.1'
    SERVER_PORT = 5556
    PROXY_PORT = 5558

