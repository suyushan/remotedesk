#!/usr/bin/python
#coding=utf-8
# File Name: client.py

from socket import *              # portable socket interface plus constants


class Client():
    """客户端类

    Attributes:
        host: ip地址
        port: 端口号
    """
    def __init__(self, host='192.168.1.101', port=54321):
        """初始化Client类"""s
        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.connect((host, port))
    def send(self, message):
        "发送数据，将message中的数据发送到连接的套接字"
        self.sockobj.send(message)
    def receive(self, cnt):
        "接受套接字的数据，以字符串形式返回，cnt指定要接受的最大数据量"
        return self.sockobj.recv(cnt)
    def close(self):
        "关闭套接字"
        self.sockobj.close()

