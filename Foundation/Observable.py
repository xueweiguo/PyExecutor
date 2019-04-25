
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
    def notify(self, component, req, params):
        for o in self.__observers:
            o.update(component, req, params)
