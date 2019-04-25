from Framework.DiagramVisitor import *


class StatsVisitor(DiagramVisitor):
    def __init__(self):
        self.diagrams = 0
        self.blocks = 0
        self.inputs = 0
        self.outputs = 0

    def visit_diagram(self, diagram):
        print('type=', type(diagram), ',tag=', diagram.tag, ',name=', diagram.name)
        self.diagrams = self.diagrams + 1
        return True

    def visit_block(self, block):
        print('type=', type(block), ',tag=', block.tag, ',name=', block.name)
        self.blocks = self.blocks + 1
        return True

    def visit_body(self, block):
        return True

    def visit_input(self, in_port):
        print('type=', type(in_port), ', tag=', in_port.tag, ',name=', in_port.name)
        self.inputs = self.inputs + 1
        return True

    def visit_output(self, out_port):
        print('type=', type(out_port), ',tag=', out_port.tag, ',name=', out_port.name)
        self.outputs = self.outputs + 1
        return True

    def get_result(self):
        print('diagrams:', self.diagrams)
        print('blocks:', self.blocks)
        print('inputs:', self.inputs)
        print('outputs:', self.outputs)