import re
from Interpreter.Complex import *
from Interpreter.Expr import *
from Interpreter.Token import *

class ChildExprBuildProxy:
    def buildExpr(self):
        return None

class ParentCreater:
    def newInstance(self):
        return None

class NonterminalExpr(Expr):
    def __init__(self):
        self.exprList = []
        self.operatorList = []

    def appendExpr(self, expr):
        self.exprList.append(expr)

    def appendOperator(self, token):
        self.operatorList.append(token)

    def evaluate(self, context):
        if (len(self.exprList) - len(self.operatorList) != 1):
            context.clearResult()
            context.setErrorMessage('Operator count and Expr count is not match.')
            return False

        #ListIterator < Expr > expr_it = exprList.listIterator()
        ex_index = 0

        context.pushResult(Complex())

        if not self.exprList[ex_index].evaluate(context):
            return False

        ex_index = ex_index + 1
        #ex_index = 0

        #ListIterator < Token > operator_it = operatorList.listIterator()
        op_index = 0
        while ex_index < len(self.exprList):
            expr = self.exprList[ex_index]
            token = self.operatorList[op_index]
            ex_index = ex_index + 1
            op_index = op_index + 1
            if op_index >= len(self.operatorList):
                op_index = len(self.operatorList) -1

            res_prev = context.getCurrentResult()
            if expr.evaluate(context):
                res_cur = context.popResult()
                valueOperator = self.getValueOperator(token.getContent())
                if valueOperator.evaluate(res_prev, res_cur):
                    context.pushResult(valueOperator.getResult())
                else:
                    context.clearResult()
                    context.setErrorMessage(valueOperator.getOperatorString(),
                                            valueOperator.getErrorMessage())
                    return False
            else:
                return False
        context.setCurrentResult(context.popResult())
        return True

    def getValueOperator(self, operatorContent):
        return None

    @staticmethod
    #def buildExpr4(proxy, creator, operatorRegex):
    def buildExpr4(proxy, creator, context, operatorRegex):
        firstExpr = proxy.buildExpr(context)
        if firstExpr == None:
            return None
        if not len(context.tokenList):
            return firstExpr
        token = context.tokenList[0]
        if ((token.getType() != TokenType.Operator)
            and (token.getType() != TokenType.Parenthese)
            and (token.getType() != TokenType.Comma)):
            context.errorMessage = 'Invalid token'
            return None

        content = token.getContent()
        m = re.match(operatorRegex, content)
        if not m:
            return firstExpr

        parentExpr = creator.newInstance()
        parentExpr.appendExpr(firstExpr)
        parentExpr.appendOperator(token)
        context.tokenList.pop(0)
        while True:
            expr = proxy.buildExpr(context)
            if not expr:
                break
            parentExpr.appendExpr(expr)

            if (len(context.tokenList) == 0): return parentExpr
            token = context.tokenList[0]
            if ((token.getType() != TokenType.Operator)
                and (token.getType() != TokenType.Parenthese)):
                return parentExpr

            content = token.getContent()
            m = re.match(operatorRegex, content)
            if not m: return parentExpr

            parentExpr.appendOperator(token)
            context.tokenList.pop(0)

            if len(context.tokenList) == 0:
                context.errorMessage = "Expression is't complete!"
                break
        return None





