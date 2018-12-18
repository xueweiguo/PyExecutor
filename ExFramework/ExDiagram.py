from ExFramework.ExComposite import *
from ExFramework.ExTagFactory import *
from ExFramework.ExComponentDict import *
from ExFramework.ExInputBlock import *
from ExFramework.ExOutputBlock import *

class ExDiagram(ExComposite):
    def __init__(self, parent, name, comment=''):
        ExComposite.__init__(self, parent, name, comment)

    def construct(self):
        self.tag = self.handle_request(self, 'create_tag')
        ExComponentDict().register(self)
        return self

    def append(self, child):
        ExComposite.append(self, child)
        ExComponentDict().register(child)
        parent = self.parent
        if parent:
            if isinstance(child, ExInputBlock):
                child.name = 'In' + str(self.countChild(ExInputBlock))
                parent.append_input(child.name)
            elif isinstance(child, ExOutputBlock):
                child.name = 'Out' + str(self.countChild(ExOutputBlock))
                parent.append_output(child.name)

    def remove(self, child):
        ExComposite.remove(self, child)
        ExComponentDict().unregister(child)

