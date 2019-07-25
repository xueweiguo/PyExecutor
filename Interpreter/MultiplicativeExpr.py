from Interpreter.NonterminalExpr import *
from Interpreter.ValueOperator import *
from Interpreter.UnaryExpr import *


class MultiplicativeExpr(NonterminalExpr):
    @staticmethod
    def buildExpr(context):
        return NonterminalExpr.buildExpr4(context, MultiplicativeExpr, UnaryExpr, "[*/]")

    def getValueOperator(self, operatorContent):
        class MyOperator(ValueOperator):
            def evaluate(self, value1, value2):
                if self.operatorString == '*':
                    self.evaluateResult = Complex.mul(value1, value2)
                    return True
                else: #operatorString.compareTo("/") == 0
                    self.evaluateResult = Complex.div(value1, value2)
                    return True
        return MyOperator(operatorContent)
