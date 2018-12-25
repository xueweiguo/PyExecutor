#通讯方式基类，规定通讯端口的行为特征
class CommPort:
    #对象初始化
    def __init__(self, address):
        self.address = address

    #发送数据
    def send_str(self, str):
        return None

    #接收数据
    def recv_str(self):
        return None

