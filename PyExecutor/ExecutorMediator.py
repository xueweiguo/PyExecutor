from Foundation.Observer import Observer
from Framework.Diagram import Diagram
from Framework.Block import Block


# 中介者类
class ExecutorMediator(Observer):
    def __init__(self, wnd):
        self.wnd = wnd

    # 转接Observer通知
    def update(self, invoker, event, params):
        self.wnd.after(0, self.update_impl, invoker, event, params)

    def update_impl(self, invoker, req, params):
        # print('PyMediator.update(', invoker, req,')')
        if isinstance(invoker, Block):
            if req == 'append':
                self.wnd.tree.append_node(invoker)
            elif req == 'remove':
                self.wnd.tree.remove_node(invoker)
            elif req == 'insert':
                self.wnd.tree.insert_node(invoker, params['index'])
            elif req == 'change_name':
                self.wnd.tree.update_node(invoker)
        self.wnd.view.update()

    def focus(self, iid):
        component = self.wnd.view.dict[iid]
        if isinstance(component, Diagram):
            self.wnd.view.set_diagram(component)
