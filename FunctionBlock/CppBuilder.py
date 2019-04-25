class CppBuilder:
    def __init__(self):
        self.macros = []
        self.funs = []
        self.current = None
        self.type = ""

    # 生成功能模块数据
    # t:模块类型，n:模块名称
    def build_fun(self, t, n):
        if self.type != 'fun':
            self.end_row()
            if self.type:
                self.end_fun()
            self.type = 'fun'
        else:
            self.end_fun()
        self.funs.append('//增加功能模块,模块名称：' + str(n))
        self.funs.append('f = new ' + self.short_type(t) + '();')

    # 生成功能模块输入数据
    # n：端口名称，data_tag：数据id
    def build_input(self, n, data_tag):
        if self.type != 'input':
            self.end_row()
            self.type = 'input'
        if self.current:
            self.current = self.current + ', '
        else:
            self.current = 'f->set_input('
        self.current = self.current + 'new Variable(' + data_tag + ')'

    # 生成功能模块参数数据
    # n：端口名称，value:参数值
    def build_param(self, n, value):
        if self.type != 'input':
            self.end_row()
            self.type = 'input'

        if self.current:
            self.current = self.current + ', '
        else:
            self.current = 'f->set_input('
        self.current = self.current + 'new ConstValue(' + str(value) + ')'

    # 生成功能模块输出数据
    # n：端口名称，data_tag：数据id
    def build_output(self, n, data_tag):
        self.macros.append('#define ' + data_tag + ' ')
        if self.type != 'output':
            self.end_row()
            self.type = 'output'

        if self.current:
            self.current = self.current + ', '
        else:
            self.current = 'f->set_output('
        self.current = self.current + 'new OutputStorage(' + str(data_tag) + ')'

    # 生成功能模块其他设定信息
    # n:信息名称
    # contents:信息内容
    def build_config(self, n, contents):
        if self.type != 'config':
            self.end_row()
            self.type = 'config'
        self.funs.append('f->add_config(new Config("' + str(n) + '", "' + str(contents) + '"));')

    def end_row(self):
        if self.current:
            if self.current[len(self.current) - 1] != ';':
                self.current = self.current + ');'
            self.funs.append(self.current)
            self.current = None

    def end_fun(self):
        self.end_row()
        self.funs.append('e->add(f);')

    def get_result(self):
        if self.current:
            self.end_fun()
        print('//C++ source code created by PyExecutor.')
        print(r'#include"executeenging.h"')
        print(r'#include"generatorfun.h"')
        print(r'#include"mathfun.h"')
        print(r'#include"valpanelfun.h"')
        print(r'#include"graphfun.h"')
        print(r'#include"constvalue.h"')
        print(r'#include"variable.h"')
        print(r'#include"outputstorage.h"')
        print('')
        print('//数据ID宏定义')
        self.macros.sort()
        macro_value = 0
        for m in self.macros:
            print(m, macro_value)
            macro_value = macro_value + 1
        print('')
        print('//定义计算引擎')
        print('ExecuteEngine* e = new ExecuteEngine();')
        print('Fun* f = NULL;')
        for f in self.funs:
            print(f)
        print('//执行计算')
        print('e->run();')

    def short_type(self, t):
        t = str(t)
        dot_pos = t.rfind('.')
        if dot_pos != -1:
            return t[dot_pos + 1:len(t)-2]
        else:
            return t

