from Framework.Block import *


class FbdBlock(Block):
    def __init__(self, cd=None, name="", comment=''):
        Block.__init__(self, cd, name, comment)
        self.strategy = None

    # 构建功能模块
    def construct(self, parent):
        Block.construct(self, parent)
        self.construct_io(parent)
        # 根据Type端口状态决定策略对象
        type_port = self.port('Type')
        if type_port:
            self.reset_strategy(type_port.value)
        else:
            self.reset_strategy(0)
        return self

    # 监视Type端口状态
    def handle_request(self, component, req, params=None):
        # 检测Type端口状态
        if (req == 'change_member') \
                and isinstance(component, InputPort) \
                and (component.name == 'Type'):
            cur = params.get('cur')
            new = params.get('new')
            if (cur != new) and (cur != new):
                # 根据端口状态终止策略对象
                self.reset_strategy(int(new))
        return Block.handle_request(self, component, req, params)

    def attach_canvas(self, canvas):
        Block.attach_canvas(self, canvas)
        self.strategy.attach_canvas(self)

    def detach_canvas(self):
        self.strategy.detach_canvas(self)
        Block.detach_canvas(self)

    # 生成保管箱
    def deposit_box(self):
        class DepositBox:
            def __init__(self, block, strategy):
                self.block = block
                self.strategy = strategy
        return DepositBox(self, self.strategy)

    #开始运算
    def start(self, context):
        context.register_box(self.tag, self.deposit_box())
        self.strategy.start(context)

    #终止运算
    def stop(self, context):
        box = context.get_box(self.tag)
        box.strategy.stop(context)
        context.unregister_box(self.tag)

    #执行运算
    def execute(self, context):
        box = context.get_box(self.tag)
        try:
            # 执行中策略对象被变更时的处理
            if box.strategy != self.strategy:
                if self.canvas:
                    box.strategy.detach_canvas(self)
                box.strategy.stop(context)
                if self.canvas:
                    self.strategy.attach_canvas(self)
                self.strategy.start(context)
                box.strategy = self.strategy
            box.strategy.execute(context)
        except Exception as e:
            print('FbdBlock.execute error:', e)

    # 重置策略对象
    def reset_strategy(self, t):
        # 解除canvas绑定
        if self.strategy and self.canvas:
            self.strategy.detach_canvas(self)
        # 替换策略对象
        self.strategy = self.create_strategy(t)
        # 绑定canvas
        if self.canvas:
            self.strategy.attach_canvas(self)

    def reset_connections(self, memo):
        self.strategy.key = memo.get(self.strategy.key)

    def copy(self, memo):
        c = Block.copy(self, memo)
        c.strategy = copy.copy(self.strategy)
        return c

    def construct_io(self, parent):
        pass

    def create_strategy(self, t):
        pass

    def get_strategy(self):
        return self.strategy

    def set_strategy(self, strategy):
        self.strategy = strategy