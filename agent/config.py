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
    PROJECTNAME = 'middle-api'

    #环境
    ENV = 'Dev'
    # ENV = 'Prod'
    # 基础路径
    BASE_PATH = os.path.dirname(__file__)

    # PID路径
    PID_PATH = BASE_PATH+'/aio_agent.pid'
    # 日志路径
    LOG_PATH = BASE_PATH+'/logs/aio_agent.log'
    ERRLOG_PATH = BASE_PATH+'/logs/aio_agent_errlogs.log'
    ACCESSLOG_PATH = BASE_PATH+'/logs/aio_agent_accesslogs.log'


class ProdConfig(Config):
    """Production config class."""

    # 服务端主机IP
    SERVER_HOST = '127.0.0.1'
    PROXY_HOST = '127.0.0.1'
    SERVER_PORT = 5556
    PROXY_PORT = 5557
    SERVER_NO_PONG_NUM = 10

    # pip代理
    PIP_PROXY = 'http://10.0.249.25:10002'
    # ZMQ proxy地址 用于信息上传
    PRODUCER = "tcp://{0}:{1}".format(PROXY_HOST,PROXY_PORT)
    # 本机IP
    TOPIC = "10001"
    # ZQM server地址 用于服务器下发指令
    SUBSCRIBER= "tcp://{0}:{1}".format(SERVER_HOST,SERVER_PORT)



class DevConfig(Config):
    """Development config class."""

    # 服务端主机IP
    SERVER_HOST = '127.0.0.1'
    PROXY_HOST = '127.0.0.1'
    SERVER_PORT = 5556
    PROXY_PORT = 5557
    SERVER_NO_PONG_NUM = 10

    # pip代理
    PIP_PROXY = 'http://10.0.249.25:10002'
    # ZMQ proxy地址 用于信息上传
    PRODUCER = "tcp://{0}:{1}".format(PROXY_HOST, PROXY_PORT)
    # 本机IP
    TOPIC = "10001"
    # ZQM server地址 用于服务器下发指令
    SUBSCRIBER = "tcp://{0}:{1}".format(SERVER_HOST, SERVER_PORT)
