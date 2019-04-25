from Framework.DiagramVisitor import *
from Framework.CustomBlock import *
from Framework.InputPort import *
from Framework.SourceBuilder import *


class BuilderDirector(DiagramVisitor):
    def __init__(self, builder):
        self.builder = builder

    def visit_diagram(self, diagram):
        return True

    def visit_block(self, block):
        if isinstance(block, CustomBlock):
            return False
        if isinstance(block, InputBlock):
            return False
        if isinstance(block, OutputBlock):
            return False
        self.builder.build_fun(type(block), block.name)
        return True

    def visit_body(self, block):
        from FunctionBlock.MathFun import MathFun
        if isinstance(block, MathFun):
            for port in block.iter('output_port'):
                if len(block.strategy.exprs[port.name]):
                    self.builder.build_config(port.name, block.strategy.exprs[port.name])

    def visit_input(self, in_port):
        data_source = in_port.data_source()
        if data_source:
            if isinstance(data_source, InputPort):
                self.builder.build_param(in_port.name, data_source.value)
            else:
                self.builder.build_input(in_port.name, data_source.tag)
        else:
            self.builder.build_param(in_port.name, in_port.value)

    def visit_output(self, out_port):
        self.builder.build_output(out_port.name, out_port.tag)