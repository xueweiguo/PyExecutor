import abc


# 抽象观察者类
class Observer(metaclass=abc.ABCMeta):
    # 更新通知方法
    # invoker:通知者
    # event:事件
    # params:事件参数
    @abc.abstractmethod
    def update(self, invoker, event, params):
        pass
