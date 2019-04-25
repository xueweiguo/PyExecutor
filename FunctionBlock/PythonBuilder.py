class PythonBuilder:
    def __init__(self):
        self.registers = []
        self.funs = []
        self.current = None

    # 生成功能模块数据
    # t:模块类型，n:模块名称
    def build_fun(self, t, n):
        if self.current:
            self.end_fun()
        self.funs.append('# 功能模块' + n)
        self.current = 'e.add(' + self.type(t) + '('

    # 生成功能模块输入数据
    # n：端口名称，data_tag：数据id
    def build_input(self, n, data_tag):
        if self.current[len(self.current)-1] != '(':
            self.current = self.current + ', '
        self.current = self.current + 'Variable(dm, \'' + data_tag + '\')'

    # 生成功能模块参数数据
    # n：端口名称，value:参数值
    def build_param(self, n, value):
        if self.current[len(self.current)-1] != '(':
            self.current = self.current + ', '
        self.current = self.current + 'ConstValue(' + str(value) + ')'

    # 生成功能模块输出数据
    # n：端口名称，data_tag：数据id
    def build_output(self, n, data_tag):
        self.registers.append('dm.register(\'' + data_tag + '\')')
        if self.current[len(self.current)-1] != '(':
            self.current = self.current + ', '
        self.current = self.current + 'StorageProxy(dm, \'' + str(data_tag) + '\')'

    # 生成功能模块其他设定信息
    # n:信息名称
    # contents:信息内容
    def build_config(self, n, contents):
        if self.current[len(self.current) - 1] != '(':
            self.current = self.current + ', '
        self.current = self.current + 'Config("' + str(n) + '", "' + str(contents) + '")'

    def end_fun(self):
        self.current = self.current + ')'
        self.funs.append(self.current)
        self.current = None

    def get_result(self):
        if self.current:
            self.end_fun()

        print('# Python source code created by PyExecutor.')
        self.output_classes()

        print('# 数据存储配置')
        print(r'dm = DataStorage("C:\DataStorage.db")')
        self.registers.sort()
        for r in self.registers:
            print(r)

        print('')
        print('# 定义计算引擎')
        print('e = ExecuteEngine()')
        print('# 配置计算引擎')
        for f in self.funs:
            print(f)

        print('')
        print('# 执行计算')
        print('e.run()')

    def type(self, t):
        t = str(t)
        dot_pos = t.rfind('.')
        if dot_pos != -1:
            return t[dot_pos + 1:len(t)-2]
        else:
            return t

    def output_classes(self):
        print(r'# Import necessary libraries.')
        print(r'from ExecuteEnging import *')
        print(r'from DataStorage import *')
        print(r'from DataManager import *')
        print(r'from ConstValue import *')
        print(r'from Variable import *')
        print(r'from Storage import *')
        print(r'from GeneratorFun import *')
        print(r'from MathFun import *')
        print(r'from ValpanelFun *')
        print(r'from GraphFun import *')
        print(r'')


