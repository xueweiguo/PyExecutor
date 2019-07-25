from Interpreter.SimpleEngine import *


# 解释器外观类
class Calculator:
    def __init__(self):
        self.values = {}
        self.engine = CalculateEngine(self)
        self.register_const()
        self.register_functions()

    # 设定环境变量
    def set_value(self, key, v):
        self.values[key] = v

    # 取得所有环境变量
    def get_values(self):
        return self.values

    # 对表达式求值
    def calculate(self, expr):
        result = self.engine.calculate(expr, False)
        try:
            return float(result)
        except Exception as e:
            print('Error:expr=', expr, ',error=', e, '.')
            return 0

    # 注册常数
    def register_const(self):
        self.engine.register_const("PI", Complex(math.pi))
        self.engine.register_const("e", Complex(math.e))

    # 注册函数
    def register_functions(self):
        self.engine.register_function(AcosFun())
        self.engine.register_function(AcoshFun())
        self.engine.register_function(AsinFun())
        self.engine.register_function(AsinhFun())
        self.engine.register_function(AtanFun())
        self.engine.register_function(AtanhFun())
        self.engine.register_function(CosFun())
        self.engine.register_function(CoshFun())
        self.engine.register_function(Log10Fun())
        self.engine.register_function(LogeFun())
        self.engine.register_function(PowerFun())
        self.engine.register_function(RootFun())
        self.engine.register_function(SinFun())
        self.engine.register_function(SinhFun())
        self.engine.register_function(TanFun())
        self.engine.register_function(MaxFun())
        self.engine.register_function(MinFun())
        self.engine.register_function(SqrtFun())


