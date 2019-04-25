from Framework.DiagramVisitor import *


class DiagramTreeVisitor(DiagramVisitor):
    def __init__(self):
        self.tags = set()

    def visit_diagram(self, diagram):
        self.tags.add(diagram.tag)
        return True

    def visit_block(self, block):
        self.tags.add(block.tag)
        return True

    def visit_input(self, in_port):
        self.tags.add(in_port.tag)
        return True

    def visit_output(self, out_port):
        self.tags.add(out_port.tag)
        return True

    def visit_connector(self, connector):
        self.tags.add(connector.tag)
        return True

    def visit_note(self, note):
        self.tags.add(note.tag)
        return True

    def in_set(self, tag):
        return tag in self.tags
