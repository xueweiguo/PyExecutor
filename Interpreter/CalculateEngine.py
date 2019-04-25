import math
from Interpreter.FunctionManager import *
from Interpreter.ConstManager import *
from Interpreter.R_string import *
from Interpreter.Complex import *
from Interpreter.PreDefineFunction import *
from Interpreter.TokenPatternFactory import *
from Interpreter.PatternBuilder import *
from Interpreter.TokenPattern import *
from Interpreter.TokenAnalyzer import *

from Interpreter.AcosFun import *
from Interpreter.AcoshFun import *
from Interpreter.AsinFun import *
from Interpreter.AsinhFun import *
from Interpreter.AtanFun import *
from Interpreter.AtanhFun import *
from Interpreter.AverageFun import *
from Interpreter.CosFun import *
from Interpreter.CoshFun import *
from Interpreter.Log10Fun import *
from Interpreter.LogeFun import *
from Interpreter.LogeFun import *
from Interpreter.PowerFun import *
from Interpreter.RootFun import *
from Interpreter.SinFun import *
from Interpreter.SinhFun import *
from Interpreter.SumFun import *
from Interpreter.TanFun import *
from Interpreter.FactorialFun import *
from Interpreter.ConvertFormatFun import *
from Interpreter.RadiusAngleFormatter import *
from Interpreter.DegreesFormatter import *

class CalculateEngine:
	CUSTOM_FUN_COUNT = 12

	class Record:
		def __init__(self):
			self.success = None
			self.question = None
			self.result = None

	def __init__(self, context):
		self.systemContext = context
		self.functionManager = FunctionManager(context)
		self.constManager = ConstManager()
		self.currentRecord = None
		self.recordList = []
		self.registerConst()
		self.registerStandardFunctions()

	def registerConst(self):
		self.constManager.registerConst("PI", Complex(math.pi))
		self.constManager.registerConst("e", Complex(math.e))

	def registerStandardFunctions(self):
		self.functionManager.registerFunction(AcosFun())
		self.functionManager.registerFunction(AcoshFun())
		self.functionManager.registerFunction(AsinFun())
		self.functionManager.registerFunction(AsinhFun())
		self.functionManager.registerFunction(AtanFun())
		self.functionManager.registerFunction(AtanhFun())
		self.functionManager.registerFunction(AverageFun())
		self.functionManager.registerFunction(CosFun())
		self.functionManager.registerFunction(CoshFun())
		self.functionManager.registerFunction(Log10Fun())
		self.functionManager.registerFunction(LogeFun())
		self.functionManager.registerFunction(PowerFun())
		self.functionManager.registerFunction(RootFun())
		self.functionManager.registerFunction(SinFun())
		self.functionManager.registerFunction(SinhFun())
		self.functionManager.registerFunction(SumFun())
		self.functionManager.registerFunction(TanFun())
		self.functionManager.registerFunction(FactorialFun())
				
		self.functionManager.registerFunction(ConvertFormatFun("to" + str(R_string.character_angle),
										RadiusAngleFormatter(self.systemContext, False)))
		self.functionManager.registerFunction(ConvertFormatFun("to" + str(R_string.character_degree),
										DegreesFormatter(self.systemContext)))

		self.functionManager.registerFunction(PreDefineFunction("x2", "pow(#1,2)"))
		self.functionManager.registerFunction(PreDefineFunction("x3", "pow(#1,3)"))
		self.functionManager.registerFunction(PreDefineFunction("2" + str(R_string.character_sqrt), "root(#1,2)"))
		self.functionManager.registerFunction(PreDefineFunction("3" + str(R_string.character_sqrt), "root(#1,3)"))
		self.functionManager.registerFunction(PreDefineFunction("ex", "pow(e,#1)"))

	def analyzeToken(self, strQuestion):
		patern_list = []
		funPattern = PatternBuilder.build(self.functionManager.functions())

		if len(funPattern) > 0:
			#patern_list.append(TokenPattern(TokenType.FunctionName, funPattern))
			#patern_list.append(TokenPattern(TokenType.Parameter, "#[1-9]"))

			#constPattern = PatternBuilder.build(self.constManager.consts())
			#patern_list.append(TokenPattern(TokenType.Number, "(" + constPattern + ")"))

			numberPattern = r"(((\.[0-9]+)|([0-9]+(\.[0-9]*)?))[eE][+-]?[0-9]+)"
			numberPattern = numberPattern + "|"
			numberPattern = numberPattern +  r"((\.[0-9]+)|([0-9]+\.[0-9]*))"
			numberPattern = numberPattern + "|"
			numberPattern = numberPattern + "([0-9]+)"

			#degree ='\°'
			#patern_list.append(TokenPattern(TokenType.Number, r"((\.[0-9]+)|([0-9]+\.[0-9]*)|([0-9]+))%"))
			#patern_list.append(TokenPattern(TokenType.Number, "(" + numberPattern + ")[" + str(degree) + "i]?"))
			patern_list.append(TokenPattern(TokenType.Number, "(" + numberPattern + ")"))
			#patern_list.append(TokenPattern(TokenType.Number, "[i]"))
			#angle = R_string.character_angle
			#patern_list.append(TokenPattern(TokenType.Operator, "[-+×/" + str(angle) + "]"))
			patern_list.append(TokenPattern(TokenType.Operator, r"[-+*/]"))
			#patern_list.append(TokenPattern(TokenType.Parenthese, "[()]"))
			#patern_list.append(TokenPattern(TokenType.Comma, ","))

		return TokenAnalyzer().analyzeToken(strQuestion, patern_list)

	def calculate(self, strQuestion, convertFormat):
		if not self.currentRecord:
			self.currentRecord = self.Record()

		tokenList = self.analyzeToken(strQuestion)
		if not convertFormat:
			self.currentRecord.question = strQuestion

		result = self.calculate1(tokenList)
		return result

	def isFunction(self, name):
		return (self.functionManager.getFunction(name) != None)
	
	def getCustomFunctionItems(self):
		items = []
		
		for i in range(1, self.CUSTOM_FUN_COUNT + 1):
			key = "F" + str(i)
			item = None
			udf = self.functionManager.getUserDefineFunction(key)
			if udf:
				item = udf.getName() + ":" + udf.getExprString()
			else:
				item = key + ":Empty"
			items.append(item)

		return items

	def saveCustomFunction(self, key, funName, funText):
		return self.functionManager.registerUserDefineFunction(key, funName, funText)

	def clearCustomFunctions(self):
		for i in range(1, self.CUSTOM_FUN_COUNT + 1):
			UserDefineFunction.clear(self.systemContext, "F" + str(i))

	def getConstManager(self):
		return self.constManager

	def getConstItems(self):
		count = self.constManager.getConstCount()
		items = []
		
		list = self.constManager.consts()
		
		formatter = StandardFormatter(self.systemContext)
		
		index = 0
		for key in list:
			item = key + ":" + formatter.toString(self.constManager.find(key))
			items.append(item)
			index = index + 1

		return items

	def getRecordCount(self):
		return len(self.recordList)

	def getRecord(self, index):
		if(index >= 0) and (index < len(self.recordList)):
			return self.recordList[index]
		else:
			return None

	def saveRecord(self):
		if(self.currentRecord != None) and (self.currentRecord.success):
			self.recordList.append(self.currentRecord)
			self.currentRecord = None
			return True
		else:
			return False
	
	def getRecordItems(self):
		formator = StandardFormatter(self.systemContext)
		record_count = self.getRecordCount()
		items = []
		for i in range(0, record_count):
			record = self.getRecord(i)
			recordString = formator.toString(record.result) + ":" + record.question
			items.append(recordString)
		return items

	def clearRecord(self, index):
		if(index >= 0) and (index < len(self.recordList)):
			self.recordList.pop(index)
			return True
		else:
			return False
	
	def clearAllRecord(self):
		self.recordList.clear()
		return True
	
	def getSystemContext(self):
		return self.systemContext

	def calculate1(self, tokenList):
		result = ''
		unknownToken = ''
		for token in tokenList:
			if token.getType() == TokenType.NoType:
				if len(unknownToken) > 0:
					unknownToken = unknownToken + ','
				unknownToken += token.getContent()

		if len(unknownToken) > 0:
			self.currentRecord.success = False
			return str(R_string.error_unknown_keyword) + unknownToken

		bContext = BuildContext(self.systemContext, self.constManager, tokenList)
		expr = AdditiveExpr.buildExpr(bContext)
		if expr:
			if len(bContext.tokenList) > 0:
				tokenString = ''
				for token in tokenList:
					if len(tokenString) != 0:
						tokenString += ","
					tokenString += token.getContent()
				self.currentRecord.success = False
				result = R_string.error_unnecessary_keyword + tokenString
			else:
				eContext = EvaluateContext(self.systemContext, self)
				eContext.pushResult(Complex(0))
				if expr.evaluate(eContext):
					value = eContext.popResult()
					result = eContext.getFormatter().toString(value)
					if result:
						self.currentRecord.success = True
						self.currentRecord.result = value
					else:
						self.currentRecord.success = False
						result = R_string.error_invalid_input
				else:
					self.currentRecord.success = False
					result = eContext.getErrorMessage()
		else:
			self.currentRecord.success = False
			result = bContext.errorMessage
		return result

	def isSuccess(self):
		return self.currentRecord.success
