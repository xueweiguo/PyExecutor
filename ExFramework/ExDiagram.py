from ExFramework.ExComponent import *
from ExFramework.ExTagFactory import *
from ExFramework.ExComponentDict import *
from ExFramework.ExInputBlock import *
from ExFramework.ExOutputBlock import *

class ExDiagram(ExComponent):
    def __init__(self, parent, name, comment=''):
        ExComponent.__init__(self, parent, name, comment)

    def construct(self):
        self.set_tag(self.handle_request(self, 'create_tag'))
        ExComponentDict().register(self)
        return self

    def append(self, child):
        ExComponent.append(self, child)
        ExComponentDict().register(child)
        parent = self.parent()
        if parent:
            if isinstance(child, ExInputBlock):
                child.set_name('In' + str(self.countChild(ExInputBlock)))
                parent.append_input(child.name())
            elif isinstance(child, ExOutputBlock):
                child.set_name('Out' + str(self.countChild(ExOutputBlock)))
                parent.append_output(child.name())

    def remove(self, child):
        ExComponent.remove(self, child)
        ExComponentDict().unregister(child)

