from Interpreter.NonterminalExpr import *
from Interpreter.ValueOperator import *
from Interpreter.MultiplicativeExpr import *


class AdditiveExpr(NonterminalExpr):
    # 构建表达式
    @staticmethod
    def buildExpr(context):
        # 构建加法表达式
        return NonterminalExpr.buildExpr4(context, AdditiveExpr, MultiplicativeExpr, "[-+]")

    def getValueOperator(self, operatorContent):
        class MyOperator(ValueOperator):
            def evaluate(self, value1, value2):
                if self.operatorString == "+":
                    self.evaluateResult = Complex.add(value1, value2)
                    return True
                else: #if (operatorString.compareTo("-") == 0)
                    self.evaluateResult = Complex.sub(value1, value2)
                    return True
        return MyOperator(operatorContent)
