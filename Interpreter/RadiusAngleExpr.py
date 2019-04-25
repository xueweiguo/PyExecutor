import math
from Interpreter.NonterminalExpr import *
from Interpreter.R_string import *
from Interpreter.ValueOperator import *
from Interpreter.UnaryExpr import *


class RadiusAngleExpr(NonterminalExpr):
    @staticmethod
    #def buildExpr(cls):
    def buildExpr(context):
        class MyProxy(ChildExprBuildProxy):
            def buildExpr(self, context):
                return UnaryExpr.buildExpr(context)
        class MyCreater(ParentCreater):
            def newInstance(self):
                return RadiusAngleExpr()

        #exprOperator = context.getSystemContext().getText(R_string.character_angle)
        exprOperator = '∠'
        return NonterminalExpr.buildExpr4(MyProxy(), MyCreater(), context, "[" + exprOperator + "]")

    def getValueOperator(self, content):
        class MyOperator(ValueOperator):
            def evaluate(self, value1, value2):
                if (value1.i != 0) or (value2.i != 0):
                    self.errorMessage = R_string.error_invalid_input
                    return False
                self.evaluateResult = Complex(value1.r * math.cos(value2.r), value1.r * math.sin(value2.r))
                return True

        return MyOperator(content)
