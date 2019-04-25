from Foundation.Observer import Observer


# update的定义和ExecutorWnd的方法重名
# 因此定义一个适配器类以回避这个问题
class ObserverAdapter(Observer):
    def __init__(self, wnd):
        self.wnd = wnd

    # 转接Observer通知
    def update(self, invoker, req, params):
        self.wnd.on_update(invoker, req, params)
