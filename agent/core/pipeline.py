#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/6/22 下午4:13.
"""

import zmq,time,threading,Queue
from core import global_config

'''
客户端和服务端和代理端互相独立，无启动顺序。
'''



class ZMQ_AGENT(object):

    def __init__(self):
        # self.pub_server_name = 'push-agent'
        self.topic = global_config['TOPIC']

        # Prepare our context and sockets
        context = zmq.Context(io_threads=2)

        # 绑定代理，往服务端上传的东西往这边丢
        self.producer = context.socket(zmq.PUSH)
        self.producer.connect("tcp://{0}:{1}".format(global_config['PROXY_HOST'],global_config['PROXY_PORT']))

        # 连接到主机获取订阅，同于触发动作
        self.subscriber = context.socket(zmq.SUB)
        self.subscriber.connect("tcp://{0}:{1}".format(global_config['SERVER_HOST'],global_config['SERVER_PORT']))
        # 订阅topic
        self.subscriber.setsockopt(zmq.SUBSCRIBE, self.topic)
        print(self.topic)


    # 订阅消息
    def sub(self):
        while True:
            message = self.subscriber.recv()
            print(message)


    # 推送信息到服务端
    def push(self,work_message):
        while True:
            print(work_message)
            self.producer.send_json(work_message)
            time.sleep(1)

    def ping(self):
        starttime = time.time()
        while True:
            timenow = time.time()
            work_message = {'starttime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(starttime)),
                            'timenow': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timenow)), 'host': '10.0.53.129'}
            self.push(work_message)


    # 单脚本主程序
    def run(self):
        # 各搞各的，开两线程
        ping_proc=threading.Thread(target=self.ping)
        sub_proc= threading.Thread(target=self.sub)

        sub_proc.start()
        ping_proc.start()
        ping_proc.join()
        sub_proc.join()

# if __name__ == '__main__':
#     ZMQ_AGENT().run()