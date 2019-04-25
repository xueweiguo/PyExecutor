class DiagramVisitor:
    # 希望继续后序访问时返回True
    def visit_diagram(self, diagram):
        return True

    # 希望继续后序访问时返回True
    def visit_block(self, block):
        return True

    # 希望继续后序访问时返回True
    def visit_body(self, block):
        return True

    # 希望继续后序访问时返回True
    def visit_input(self, in_port):
        return True

    # 希望继续后序访问时返回True
    def visit_output(self, out_port):
        return True

    # 希望继续后序访问时返回True
    def visit_connector(self, connector):
        return True

    # 希望继续后序访问时返回True
    def visit_note(self, note):
        return True
