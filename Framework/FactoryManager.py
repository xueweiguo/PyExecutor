class FactoryManager(object):
    # 私有的静态成员，用于管理本类唯一的实例
    __instance = None

    # 申请内存空间的静态方法
    # 控制只生成本类的唯一的实例
    def __new__(cls):
        if not FactoryManager.__instance:
            cls.__instance = super(FactoryManager, cls).__new__(cls)
            # 初始化工厂字典
            cls.__instance.__factory_dict = {}
            # 初始化模式集合
            cls.__instance.__mode_set = set()
            # 初始化当前模式
            cls.__instance.mode = None
        return FactoryManager.__instance

    # 对象初始化函数
    # 每次构建时都会被调用，因此成员初始化在__new__中实现
    def __init__(self):
        pass

    # 工厂登录方法
    # mode:模式，name:名称，factory：工厂对象
    def register(self, mode, name, factory):
        self.__factory_dict[self.__key(mode, name)] = factory
        self.__mode_set.add(mode)

    # 取得工厂
    # name:工厂名称
    # 模式有使用者指定
    def factory(self, name):
        return self.__factory_dict.get(self.__key(self.mode, name))

    # 取得已经登录过的所有模式
    # 列表按照字母排序
    def modes(self):
        modes = list(self.__mode_set)
        modes.sort()
        return modes

    # 检索Key合成方法
    # 私有方法
    def __key(self, mode, name):
        return mode + ',' + name


