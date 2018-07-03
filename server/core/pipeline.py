#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/6/22 下午4:13.
"""

import zmq,time,random,threading
from core import global_config

'''
客户端和服务端和代理端互相独立，无启动顺序。
'''




class ZMQ_SERVER(object):
    def __init__(self):
        self.pub_server_name = global_config['PROJECTNAME']

        context = zmq.Context(io_threads=2)
        #服务端pub
        self.socket = context.socket(zmq.PUB)
        self.socket.bind("tcp://127.0.0.1:5556")
        #从proxy拉取数据
        self.results_receiver = context.socket(zmq.PULL)
        self.results_receiver.bind("tcp://127.0.0.1:5558")

    def pub(self):
        while True:
            topic = random.randrange(9999, 10005)
            messagedata = random.randrange(1, 215) - 80
            print 'topic:%s messagedata:%s' % (topic, messagedata)
            self.socket.send('%d %d %s' % (topic, messagedata, self.pub_server_name))
            time.sleep(1)

    def rec(self):
        while True:
            result = self.results_receiver.recv_json()
            print(result)


    def start(self):
        rec_proc = threading.Thread(target=self.rec)
        pub_proc = threading.Thread(target=self.pub)
        pub_proc.start()
        rec_proc.start()
        pub_proc.join()
        rec_proc.join()

if __name__ == '__main__':
    zmq = ZMQ_SERVER()
    while True:
        zmq.pub()