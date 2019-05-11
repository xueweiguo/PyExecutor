from Interpreter.Token import *
from Interpreter.TerminalExpr import *
from Interpreter.NumberExpr import *

class PrimaryExpr(TerminalExpr):
    @staticmethod
    #def buildExpr(cls):
    def buildExpr(context):
        if (len(context.tokenList) == 0):
            context.errorMessage = "Expression is't complete"
            return None
        token = context.tokenList[0]

        if token.getType() == TokenType.Number:
            return NumberExpr.buildExpr(context)
        elif token.getType() == TokenType.Parenthese:
            if token.getContent()== '(':
                context.tokenList.pop(0)
                from Interpreter.AdditiveExpr import AdditiveExpr
                expr = AdditiveExpr.buildExpr(context)
                if (expr == None):
                    return None

                if (len(context.tokenList) > 0):
                    token = context.tokenList.pop(0)
                    if token.getType() == TokenType.Parenthese and token.getContent()==')':
                        return expr
                context.errorMessage = "\')\'is necessary"
                return None
            else:
                context.errorMessage = "\'(\'is necessary"
                return None

        elif token.getType() == TokenType.FunctionName:
            from Interpreter.FunctionExpr import FunctionExpr
            return FunctionExpr.buildExpr(context)
        elif token.getType() == TokenType.Parameter:
            return ParameterExpr.buildExpr(context)
        else:
            context.errorMessage = R_string.error_invalid_input
            return None
