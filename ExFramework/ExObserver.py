import abc
class ExObserver(metaclass=abc.ABCMeta):
    # 更新通知方法
    # invoker:通知者
    # exe:扩展信息
    @abc.abstractmethod
    def update(self, invoker, ext):
        pass
