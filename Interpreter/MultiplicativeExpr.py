from Interpreter.NonterminalExpr import *
from Interpreter.ValueOperator import *
from Interpreter.RadiusAngleExpr import *

class MultiplicativeExpr(NonterminalExpr):
    @staticmethod
    def buildExpr(cls, context):
        class MyProxy(ChildExprBuildProxy):
            def buildExpr(self, context):
                return RadiusAngleExpr.buildExpr(context)

        class MyCreater(ParentCreater):
            def newInstance(self):
                return MultiplicativeExpr()

        return NonterminalExpr.buildExpr4(MyProxy(), MyCreater(), context, "[×/]")

    def getValueOperator(self, operatorContent):
        class MyOperator(ValueOperator):
            def evaluate(self, value1, value2):
                if(self.operatorString.compareTo("×") == 0):
                    self.evaluateResult = Complex.mul(value1, value2)
                    return True
                else: #operatorString.compareTo("/") == 0
                    self.evaluateResult = Complex.div(value1, value2)
                    return True
        return MyOperator(operatorContent)
