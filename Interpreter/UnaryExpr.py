from Interpreter.TerminalExpr import *
from Interpreter.PrimaryExpr import *
from Interpreter.Token import *

class UnaryExpr(TerminalExpr):
    def __init__(self):
        self.primaryExpr = PrimaryExpr()

    def setPrimaryExpr(self, expr):
        self.primaryExpr = expr

    @staticmethod
    #def buildExpr(cls):
    def buildExpr(context):
        minusCount = 0
        while (len(context.tokenList) > 0) and (context.tokenList[0].getType() == TokenType.Operator):
            content = context.tokenList[0].getContent()
            if (content.compareTo("-") == 0): # == "-")
                minusCount = minusCount + 1
            elif content.compareTo("+"): # != "+")
                context.errorMessage = "Invalid token:" + content
                return None
            context.tokenList.removeFirst()

        if (len(context.tokenList) == 0):
            context.errorMessage = "Expression is't complete"
            return None
        expr = UnaryExpr.method_name(context)
        if expr == None:
            return None
        if ((minusCount % 2) == 1):
            unary = UnaryExpr()
            unary.setPrimaryExpr(expr)
            return unary
        else:
            return expr

    @staticmethod
    def method_name(context):
        expr = PrimaryExpr.buildExpr(context)
        return expr

    def evaluate(self, context):
        if (self.primaryExpr.evaluate(context)):
            result = context.popResult()
            result.r = -result.r
            result.i = -result.i
            context.pushResult(result)
            return True
        else:
            return False
