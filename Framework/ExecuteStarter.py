from Framework.DiagramVisitor import *


class ExecuteStarter(DiagramVisitor):
    def __init__(self, context):
        self.context = context

    def visit_block(self, block):
        from Framework.CustomBlock import CustomBlock
        if isinstance(block, CustomBlock):
            return True
        else:
            block.start(self.context)
