from ExFramework.ExComponent import *
from ExFramework.ExTagFactory import *
from ExFramework.ExComponentDict import *

class ExDiagram(ExComponent):
    def __init__(self, name, comment=''):
        ExComponent.__init__(self, name, comment)

    def append(self, child):
        child.set_tag(ExTagFactory().createTag())
        ExComponent.append(self, child)
        ExComponentDict().register(child)

    def remove(self, child):
        ExComponentDict().unregister(child)
        ExComponent.remove(self, child)
