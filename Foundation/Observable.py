# 观察对象类
class Observable:
    def __init__(self):
        self.__observers = []

    # 绑定Observer
    def attach(self, observer):
        self.__observers.append(observer)

    # 解绑Observer
    def detach(self, observer):
        self.__observers.remove(observer)

    # 通知所有的观察者
    # invoker:通知发起者
    # event：事件
    # params：通知参数
    def notify(self, invoker, event, params):
        for o in self.__observers:
            o.update(invoker, event, params)
