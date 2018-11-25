from ExFramework.ExSerializeFactory import *
from PyExecutorFactory import *


class FbdSerializeFactory(ExSerializeFactory):
    def __init__(self):
        PyExecutorFactory().register('fbd', 'serialize', self)

    # 系列化编码器
    def jsonEncoder(self):
        return ExJsonEncoder


FbdSerializeFactory()