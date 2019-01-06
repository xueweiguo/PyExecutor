from Interpreter.Token import *
from Interpreter.TerminalExpr import *
from Interpreter.AdditiveExpr import *

class PrimaryExpr(TerminalExpr):
    @staticmethod
    def buildExpr(cls, context):
        if (len(context.tokenList) == 0):
            context.errorMessage = "Expression is't complete"
            return None
        token = context.tokenList[0]

        if token.getType() == TokenType.Number:
            return NumberExpr.buildExpr(context)
        elif token.getType() == TokenType.Parenthese:
            if (token.getContent().compareTo("(") == 0):
                context.tokenList.removeFirst()
                expr = AdditiveExpr.buildExpr(context)
                if (expr == None):
                    return None

                if (len(context.tokenList) > 0):
                    token = context.tokenList.removeFirst()
                    if (token.getType() == TokenType.Parenthese and token.getContent().compareTo(")") == 0):
                        return expr
                context.errorMessage = "\')\'is necessary"
                return None
            else:
                context.errorMessage = "\'(\'is necessary"
                return None

        elif token.getType() == TokenType.casecFunctionName:
            return FunctionExpr.buildExpr(context)
        elif token.getType() == TokenType.Parameter:
            return ParameterExpr.buildExpr(context)
        else:
            context.errorMessage = R_string.error_invalid_input
            return None
