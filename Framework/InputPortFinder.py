from Framework.DiagramView import *

class InputPortFinder(DiagramVisitor):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.in_port = None

    # 希望继续后序访问时返回True
    def visit_input(self, in_port):
        pt = in_port.point()
        if 0 < self.__x - pt[0] < 10 and abs(pt[1] - self.__y) < 2:
            self.in_port = in_port
            return False
        return True

