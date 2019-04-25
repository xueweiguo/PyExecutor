import math
import json
#通信端口基类，规定端口的行为特征
class CommPort:
    # 对象初始化
    def __init__(self):
        self.response = None
        self.t = 0

    # 打开通信端口
    def open(self):
        pass

    # 关闭通信端口
    def close(self):
        pass

    #发送数据
    def send_data(self, data):
        if data[0:9] == 'sec#1234,':
            data = data[9:]
        if data[0:6] == 'login,':
            self.response = 'sec#1234'
        elif data[0:7] == 'logout,':
            self.response = 'logout OK!'
        elif data[0:8] == 'get_data':
            values = []
            values.append(math.sin(self.t / 20) * 2)
            values.append(math.sin(self.t / 30) * 3)
            values.append(math.sin(self.t / 50) * 5)
            self.t = self.t + 1
            self.response = json.dumps(values)
            self.response = self.response + '.des.bcc'
        else:
            self.response = 'set_data_ok.des.bcc'
        # print('CommPort.send_data(', data, ')')

    #接收数据
    def recv_data(self):
        return self.response

