from Framework.DiagramVisitor import *
from Framework.CustomBlock import *


class ExecuteStarter(DiagramVisitor):
    def __init__(self, context):
        self.context = context

    def visit_block(self, block):
        if isinstance(block, CustomBlock):
            return True
        else:
            block.start(self.context)
