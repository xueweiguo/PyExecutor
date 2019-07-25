import re
from Interpreter.Complex import *
from Interpreter.Expr import *
from Interpreter.Token import *


class NonterminalExpr(Expr):
    def __init__(self):
        self.exprList = []
        self.operatorList = []

    def appendExpr(self, expr):
        self.exprList.append(expr)

    def appendOperator(self, token):
        self.operatorList.append(token)

    def evaluate(self, context):
        if len(self.exprList) - len(self.operatorList) != 1:
            context.clearResult()
            context.setErrorMessage('Operator count and Expr count is not match.')
            return False

        ex_index = 0
        context.pushResult(Complex())
        if not self.exprList[ex_index].evaluate(context):
            return False

        ex_index = ex_index + 1
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

    @staticmethod
    def buildExpr4(context, ParentExpr, ChildExpr, operators):
        # 构建第一个下级表达式
        first_expr = ChildExpr.buildExpr(context)
        if first_expr == None:
            return None
        if not len(context.tokenList):
            return first_expr
        token = context.tokenList[0]
        if ((token.getType() != TokenType.Operator)
            and (token.getType() != TokenType.Parenthese)
            and (token.getType() != TokenType.Comma)):
            context.errorMessage = 'Invalid token'
            return None

        # 下一个Token不是期待的操作符，则退出当前表达式的解析
        content = token.getContent()
        m = re.match(operators, content)
        if not m:
            return first_expr

        # 构建父表达式
        parentExpr = ParentExpr()
        # 添加第一个子表达式
        parentExpr.appendExpr(first_expr)
        # 添加操作符
        parentExpr.appendOperator(token)
        context.tokenList.pop(0)
        while True:
            # 构建想下一个子表达式
            expr = ChildExpr.buildExpr(context)
            if not expr:
                break
            # 添加子表达式
            parentExpr.appendExpr(expr)

            if (len(context.tokenList) == 0):
                return parentExpr

            token = context.tokenList[0]
            if ((token.getType() != TokenType.Operator)
                and (token.getType() != TokenType.Parenthese)):
                return parentExpr

            # 取得下一个操作符
            content = token.getContent()
            m = re.match(operators, content)
            if not m: return parentExpr

            #添加操作符
            parentExpr.appendOperator(token)
            context.tokenList.pop(0)

            # 异常退出
            if len(context.tokenList) == 0:
                context.errorMessage = "Expression is't complete!"
                break
        return None

    def getValueOperator(self, operatorContent):
        return None


