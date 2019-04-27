from FunctionBlock.CommPort import *


# 通信端口类，负责处理通信ID
class SectionPortProxy(CommPort):
    # 对象初始化
    def __init__(self, port=None, usr=None, pwd=None):
        CommPort.__init__(self)
        self.port = port
        self.usr = usr
        self.pwd = pwd
        self.section = None

    # 打开端口
    def open(self):
        if self.port.open():
            # 使用用户名，密码进行认证
            login_str = "login, user={}, password={}".format(self.usr, self.pwd)
            self.port.send_data(login_str)
            # 认证成功的情况下，保存secion信息
            self.section = self.port.recv_data()
    # 关闭端口
    def close(self):
        if self.section:
            # 取消认证
            logout_str = "logout, user={}".format(self.usr, self.pwd)
            self.port.send_data(logout_str)
            if self.port.recv_data() == 'logout OK!':
                # 取消成功是，关闭端口
                self.port.close()
                self.section = None

    # 发送数据
    def send_data(self, data):
        if self.section:
            # 发送数据是增加section信息作为前缀
            return self.port.send_data(self.section + ',' + data)

    # 接收数据
    def recv_data(self):
        if self.section:
            return self.port.recv_data()