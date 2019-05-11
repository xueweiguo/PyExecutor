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

#计算引擎
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
		self.patterns = []
		self.build_basic_patterns()
	# 创建四则运算规则
	def build_basic_patterns(self):
		numberPattern = r"(((\.[0-9]+)|([0-9]+(\.[0-9]*)?))[eE][+-]?[0-9]+)"
		numberPattern = numberPattern + "|"
		numberPattern = numberPattern + r"((\.[0-9]+)|([0-9]+\.[0-9]*))"
		numberPattern = numberPattern + "|"
		numberPattern = numberPattern + "([0-9]+)"
		self.patterns.append(TokenPattern(TokenType.Number, "(" + numberPattern + ")"))
		self.patterns.append(TokenPattern(TokenType.Operator, r"[-+*/]"))
		self.patterns.append(TokenPattern(TokenType.Parenthese, "[()]"))
		self.patterns.append(TokenPattern(TokenType.Comma, ","))

	def register_const(self, name, value):
		self.constManager.registerConst(name, value)

	def register_function(self, fun):
		self.functionManager.registerFunction(fun)

	# 计算表达式
	def calculate(self, strQuestion, convertFormat):
		if not self.currentRecord:
			self.currentRecord = self.Record()
		# 替换表达式中的变量名
		strSrc = strQuestion
		strAnalyze = strQuestion
		for k, v in self.systemContext.get_values().items():
			strAnalyze = strSrc.replace(k, v)
			strSrc  = strAnalyze
		# 对表达式进行分析，返回语法树
		tokenList = self.analyzeToken(strAnalyze)
		if not convertFormat:
			self.currentRecord.question = strQuestion
		# 对语法树进行计算，返回运算结果
		return self.calculate1(tokenList)

	# 表达式分析
	def analyzeToken(self, strQuestion):
		# 生成分析语法对象集合
		patterns = []
		fun_pattern = PatternBuilder.build(self.functionManager.functions())
		if len(fun_pattern) > 0:
			#函数语法定义
			patterns.append(TokenPattern(TokenType.FunctionName, fun_pattern))
		#基本语法定义
		patterns.extend(self.patterns)
		# 对表达式进行分析，返回语法树
		return TokenAnalyzer().analyzeToken(strQuestion, patterns)

	def isFunction(self, name):
		return (self.functionManager.getFunction(name) != None)
	
	def getCustomFunctionItems(self):
		items = []
		
		for i in range(1, self.CUSTOM_FUN_COUNT + 1):
			key = "F" + str(i)
			item = None
			udf = self.functionManager.getUserDefineFunction(key)
			if udf:
				item = udf.get_name() + ":" + udf.getExprString()
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
