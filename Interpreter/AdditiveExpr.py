from Interpreter.NonterminalExpr import *
from Interpreter.ValueOperator import *
from Interpreter.MultiplicativeExpr import *

class AdditiveExpr(NonterminalExpr):
    @staticmethod
    #def buildExpr(cls):
    def buildExpr(context):
        class MyProxy(ChildExprBuildProxy):
            #def buildExpr(self, context):
            def buildExpr(self, context):
                return MultiplicativeExpr.buildExpr(context)

        class MyCreater(ParentCreater):
            def newInstance(self):
                return AdditiveExpr()

        return NonterminalExpr.buildExpr4(MyProxy(), MyCreater(), context, "[-+]")

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
