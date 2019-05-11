from Framework.Block import *

# 策略基类
class FbdStrategy:
    def __init__(self, block):
        # 保存管理模块的tag值，用于从上下文中取得保管箱
        if block:
            self.key = block.tag
        else:
            self.key = None

    def __copy__(self):
        c = type(self).__new__(type(self))
        c.key = copy.copy(self.key)
        return c

    # 开始执行
    def start(self, context):
        pass

    # 终止执行
    def stop(self, context):
        pass

    # 执行计算动作
    def execute(self, context):
        pass

    # 绑定canvas
    def attach_view(self, block):
        pass

    # 取消绑定的canvas
    def detach_view(self, block):
        pass

    # 取得输入端口的当前值
    def _input_values(self, context):
        box = context.get_box(self.key)
        value = {}
        for port in type_filter(Composite.iter(box.block), InputPort):
            ds = port.data_source()
            if ds:
                if isinstance(ds, OutputPort):
                    value[port.name] = float(context.get_value(ds.tag))
                else:
                    value[port.name] = float(ds.value)
            else:
                value[port.name] = 0
        return value