from FunctionBlock.FbdStrategy import *


# 通信策略基类
class CommStrategy(FbdStrategy):
    def __init__(self, block=None):
        FbdStrategy.__init__(self, block)
        self.port = None
        self.packer = None
        self.status = None

    # 设定端口
    def set_port(self, port):
        self.port = port

    # 设定加密方式
    def set_security(self, sec):
        self.packer = sec

    # 启动通信
    def start(self, context):
        if self.port:
            self.port.open()

    # 终止通信
    def stop(self, context):
        if self.port:
            self.port.close()

    # 执行通信
    def execute(self, context):
        if self.port and self.packer:
            # 生成送信数据
            command = self.create_command(context)
            # 数据打包
            command = self.packer.pack(command)
            # 发送数据
            self.port.send_data(command)
            # 接收数据
            response = self.port.recv_data()
            # 数据拆包
            response = self.packer.un_pack(response)
            # 处理接收数据
            self.handle_response(context, response)

    def copy(self, memo):
        c = copy.copy(self)
        if self.port:
            c.port = copy.copy(self.port)
        else:
            c.port = None
        if self.packer:
            c.packer = copy.copy(self.packer)
        else:
            c.packer = None
        if self.status:
            c.status = copy.copy(self.status)
        else:
            c.status = None
        return c

    def create_command(self, context):
        pass

    def handle_response(self, context, response):
        pass



