
class ExObservable:
    def __init__(self):
        self.__observers = []

    # 绑定ExObserver
    def attach(self, observer):
        self.__observers.append(observer)

    # 解绑ExObserver
    def detach(self, observer):
        self.__observers.remove(observer)

    # 通知所有的观察者
    def notify(self, component, ext):
        for o in self.__observers:
            o.update(component, ext)
