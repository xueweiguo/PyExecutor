from Interpreter.CalculateFunction import *
from Interpreter.UserDefineFunction import *
class FunctionManager:
	def __init__(self, context):
		self.systemContext = context
		self.functionMap = dict()
		self.userDefineMap = dict()

	def registerFunction(self, fun):
		if not self.functionMap.get(fun.get_name()):
			self.functionMap[fun.get_name()] = fun
			return True
		else:
			return False

	def registerUserDefineFunction(self, key, funName, funText):
		fun = self.getFunction(funName)
		if(fun != None):
			if not isinstance(fun, UserDefineFunction):
				# Has been registered as a system function.
				return R_string.error_used_fun_name

			if fun.getKey().compareTo(key) != 0 :
				# The name has been used by other UserDefineFunctio.
				return R_string.error_used_fun_name

			self.functionMap.pop(fun.get_name())
			self.userDefineMap.pop(key)

		# Now, we can register the UserdefineFunction safety.
		udf_new = UserDefineFunction(key, funName, funText)
		udf_new.saveMe(self.systemContext)
		return self.registerUserDefineFunction1(udf_new)

	def registerUserDefineFunction1(self, udf):
		self.userDefineMap[udf.getKey()] = udf
		self.functionMap[udf.get_name()] = udf

	def getUserDefineFunction(self, key):
		return self.userDefineMap.get(key)

	def functions(self):
		return self.functionMap.keys()

	def getFunction(self, name):
		return self.functionMap.get(name)

