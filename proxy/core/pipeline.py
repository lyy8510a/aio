#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/6/22 下午4:13.
"""

import zmq,time,random
from core import global_config

'''
客户端和服务端和代理端互相独立，无启动顺序。
'''




class ZMQ_PROXY(object):
    def __init__(self):
        self.proxy_id = random.randrange(1, 10005)
        print "I am proxy #%s" % (self.proxy_id)
        context = zmq.Context()
        # recieve work
        self.consumer_receiver = context.socket(zmq.PULL)
        # self.consumer_receiver.bind("tcp://{0}:{1}".format( global_config['RECIEVE_HOST'],global_config['RECIEVE_PORT']))
        self.consumer_receiver.bind("tcp://127.0.0.1:5557")
        # send work
        self.consumer_sender = context.socket(zmq.PUSH)
        # self.consumer_sender.connect("tcp://{0}:{1}".format( global_config['SENDER_HOST'],global_config['SENDER_PORT']))
        self.consumer_sender.connect("tcp://127.0.0.1:5558")

    def worker(self):
        work = self.consumer_receiver.recv_json()
        if (work['host']):
            result = {'proxy_id': self.proxy_id, 'host': work['host']}
            self.consumer_sender.send_json(result)





if __name__ == '__main__':
    zmq = ZMQ_PROXY()
    while True:
        zmq.worker()