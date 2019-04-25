from Framework.DiagramVisitor import *
from Framework.CustomBlock import *


class ConnectionCoordinator(DiagramVisitor):
    def __init__(self, memo):
        self.memo = memo

    # 希望继续访问端口对象是，必须返回True
    def visit_block(self, block):
        block.reset_connections(self.memo)
        return True

    def visit_input(self, in_port):
        in_port.reset_connections(self.memo)
        return True

    def visit_output(self, out_port):
        out_port.reset_connections(self.memo)
        return True

    def visit_connector(self, connector):
        connector.reset_connections(self.memo)
        return True



