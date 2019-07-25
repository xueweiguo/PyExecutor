from Interpreter.CalculateEngine import *
from Interpreter.AcosFun import *
from Interpreter.AcoshFun import *
from Interpreter.AsinFun import *
from Interpreter.AsinhFun import *
from Interpreter.AtanFun import *
from Interpreter.AtanhFun import *
from Interpreter.AverageFun import *
from Interpreter.CosFun import *
from Interpreter.CoshFun import *
from Interpreter.Log10Fun import *
from Interpreter.LogeFun import *
from Interpreter.LogeFun import *
from Interpreter.PowerFun import *
from Interpreter.RootFun import *
from Interpreter.SinFun import *
from Interpreter.SinhFun import *
from Interpreter.SumFun import *
from Interpreter.TanFun import *
from Interpreter.FactorialFun import *
from Interpreter.MinFun import *
from Interpreter.MaxFun import *
from Interpreter.SqrtFun import *


class SimpleEngine(CalculateEngine):
    def __init__(self, context):
        CalculateEngine.__init__(self, context)

    def registerConst(self):
        self.constManager.registerConst("PI", Complex(math.pi))
        self.constManager.registerConst("e", Complex(math.e))

    def registerStandardFunctions(self):
        self.functionManager.registerFunction(AcosFun())
        self.functionManager.registerFunction(AcoshFun())
        self.functionManager.registerFunction(AsinFun())
        self.functionManager.registerFunction(AsinhFun())
        self.functionManager.registerFunction(AtanFun())
        self.functionManager.registerFunction(AtanhFun())
        self.functionManager.registerFunction(CosFun())
        self.functionManager.registerFunction(CoshFun())
        self.functionManager.registerFunction(Log10Fun())
        self.functionManager.registerFunction(LogeFun())
        self.functionManager.registerFunction(PowerFun())
        self.functionManager.registerFunction(RootFun())
        self.functionManager.registerFunction(SinFun())
        self.functionManager.registerFunction(SinhFun())
        self.functionManager.registerFunction(TanFun())
        self.functionManager.registerFunction(MaxFun())
        self.functionManager.registerFunction(MinFun())
        self.functionManager.registerFunction(SqrtFun())

    def create_patterns(self):
        patern_list = []
        funPattern = PatternBuilder.build(self.functionManager.functions())

        if len(funPattern) > 0:
            patern_list.append(TokenPattern(TokenType.FunctionName, funPattern))
            # patern_list.append(TokenPattern(TokenType.Parameter, "#[1-9]"))

            # constPattern = PatternBuilder.build(self.constManager.consts())
            # patern_list.append(TokenPattern(TokenType.Number, "(" + constPattern + ")"))
            numberPattern = r"(((\.[0-9]+)|([0-9]+(\.[0-9]*)?))[eE][+-]?[0-9]+)"
            numberPattern = numberPattern + "|"
            numberPattern = numberPattern + r"((\.[0-9]+)|([0-9]+\.[0-9]*))"
            numberPattern = numberPattern + "|"
            numberPattern = numberPattern + "([0-9]+)"

            # patern_list.append(TokenPattern(TokenType.Number, r"((\.[0-9]+)|([0-9]+\.[0-9]*)|([0-9]+))%"))
            patern_list.append(TokenPattern(TokenType.Number, "(" + numberPattern + ")"))
            # patern_list.append(TokenPattern(TokenType.Number, "[i]"))
            patern_list.append(TokenPattern(TokenType.Operator, r"[-+*/]"))
            patern_list.append(TokenPattern(TokenType.Parenthese, "[()]"))
            patern_list.append(TokenPattern(TokenType.Comma, ","))
        return patern_list
