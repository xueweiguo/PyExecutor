from Interpreter.NonterminalExpr import *
from Interpreter.AdditiveExpr import *
from Interpreter.Complex import *


class FunctionExpr(NonterminalExpr):
	def __init__(self,  name):
		NonterminalExpr.__init__(self)
		self.functionName = name

	@staticmethod
	def buildExpr(context):
		token = context.tokenList[0]
		if token.getType() != TokenType.FunctionName:
			context.errorMessage = "Invalid function name:" + token.getContent()
			return None

		functionName = token.getContent()
		context.tokenList.pop(0)

		if len(context.tokenList) == 0:
			context.errorMessage = "Expression is't complete"
			return None

		token = context.tokenList[0]
		if (token.getType() != TokenType.Parenthese) or (token.getContent()!='('):
			# != "(")
			context.errorMessage = '\'(\'is necessary'
			return None
		context.tokenList.pop(0)

		if len(context.tokenList) == 0:
			context.errorMessage = "Expression is't complete"
			return None

		funExpr = FunctionExpr(functionName)

		token = context.tokenList[0]
		if(token.getType() == TokenType.Parenthese) and (token.getContent().compareTo(")") == 0):
			# == ")")
			context.tokenList.pop(0)
			return funExpr

		while(True):
			expr = AdditiveExpr.buildExpr(context)
			if not expr:
				break
			funExpr.appendExpr(expr)

			if len(context.tokenList) == 0:
				context.errorMessage = "Expression is't complete"
				break

			token = context.tokenList[0]
			if token.getType() == TokenType.Comma:
				context.tokenList.pop(0)
			elif (token.getType() == TokenType.Parenthese) and (token.getContent()==')'):
				context.tokenList.pop(0)
				return funExpr
			else:
				context.errorMessage = functionName + " parameter error"
				break

		return None

	def evaluate(self, context):
		context.pushResult(Complex(0))
		paraList = []
		for expr in self.exprList:
			if expr.evaluate(context):
				paraList.append(context.getCurrentResult())
			else:
				return False
		context.popResult()
		fun = context.getFunctionManager().getFunction(self.functionName)
		if not fun:
			context.setErrorMessage("Can't found the function:" + self.functionName)
			return False
		return fun.execute(context,paraList)

