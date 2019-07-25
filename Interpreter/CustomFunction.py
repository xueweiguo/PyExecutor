from Interpreter.CalculateFunction import *
from Interpreter.Token import *
from Interpreter.BuildContext import *
from Interpreter.AdditiveExpr import *
from Interpreter.EvaluateContext import *

class CustomFunction (CalculateFunction):
	def __init__(self, name):
		self.funName = name

	def get_name(self):
		return self.funName

	def getExprString(self):
		return None

	def execute(self, paraList):
		functionString = self.getExprString()

		if(not functionString) or (len(functionString) == 0):
			context.setErrorMessage(self.get_name(), R_string.error_undefined_custom_function)
			return False

		engine = context.getCalculateEngine()
		tokenList = engine.analyze_token(functionString)
		unknownToken = ''
		for token in tokenList:
			if(token.getType() == TokenType.NoType):
				if(len(unknownToken) > 0):
					unknownToken = unknownToken + ","
				unknownToken = unknownToken + token.getContent()

		if(len(unknownToken) > 0):
			context.setErrorMessage(context.getSystemContext().getText(R_string.error_invalid_token) + " in " + self.get_name() + ":" + unknownToken)
			return False

		bContext = BuildContext(engine.getSystemContext(), engine.getConstManager(), tokenList)

		expr = AdditiveExpr.buildExpr(bContext)

		if expr:
			eContext = EvaluateContext(context, engine)
			eContext.pushResult(Complex(0))
			if not eContext.pushCustomCall(self.get_name(), paraList):
				context.setErrorMessage(eContext.getErrorMessage())
				return False

			success = expr.evaluate(eContext)
			eContext.popCustomCall()
			if(success):
				context.setCurrentResult(eContext.popResult())
				context.setFormatter(eContext.getFormatter())
				return True
			else:
				context.setErrorMessage(eContext.getErrorMessage())
				return False
		else:
			context.setErrorMessage(bContext.errorMessage)
			return False

