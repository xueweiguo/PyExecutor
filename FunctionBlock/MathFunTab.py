from FunctionBlock.FbdBlock import *


class MathFunTab(PropertyTab):
    def __init__(self, parent, name, element):
        PropertyTab.__init__(self, parent, name, element)
        self.pack(side=TOP)

        self.list = ListView(self, ("输出", "表达式", "说明"))
        # 设置列宽
        self.list.config_column("输出", 50)
        self.list.config_column("表达式", 150, True)
        self.list.config_column("说明", 100, True)
        self.list.pack()

        r = 0
        for key, expr in self.element.strategy.exprs.items():
            self.list.insert("", r, iid=key, text=r + 1, values=(key,  expr[0], expr[1]))  # 插入数据，
            r = r + 1

    def apply(self):
        self.element.handle_request(self.element, 'change_member',
                            {'getter': FbdBlock.get_strategy,
                             'setter': FbdBlock.set_strategy})
        expressions = dict()
        for iid in self.list.get_children(''):
            values = self.list.set(iid)
            self.element.strategy.exprs[values['输出']] = values['表达式'], values['说明']

