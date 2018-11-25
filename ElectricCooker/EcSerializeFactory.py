from ExFramework.ExSerializeFactory import *
from PyExecutorFactory import *


class EcSerializeFactory(ExSerializeFactory):
    def __init__(self):
        PyExecutorFactory().register('ecd', 'serialize', self)

    # 系列化编码器
    def jsonEncoder(self):
        return ExJsonEncoder


EcSerializeFactory()