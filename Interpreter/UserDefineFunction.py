from Interpreter.CustomFunction import *


class UserDefineFunction(CustomFunction):
	PREFS_NAME = "CustomFunction"
	
	def __init__(self, key, name, expr):
		CustomFunction.__init__(self, name)
		self.functionKey = key
		self.functionExpr = expr

	def getKey(self):
		return self.functionKey

	def getExprString(self):
		return self.functionExpr

	def load(self, key):
		settings = context.getSharedPreferences(self.PREFS_NAME, 0)
		funInfo = settings.getString(key, "")

		if len(funInfo) == 0:
			return None
		pre_expr = funInfo.index(":")
		if pre_expr >= 1 and pre_expr < (len(funInfo) - 1):
			#Must has name and expression
			return UserDefineFunction(key, funInfo[0:pre_expr], funInfo[pre_expr + 1:])
		else:
			return None

	@staticmethod
	def clear(cls, key):
		settings = context.getSharedPreferences(cls.PREFS_NAME, 0)
		editor = settings.edit()
		editor.putString(key, "")
		editor.commit()

	def saveMe(self):
		settings = context.getSharedPreferences(self.PREFS_NAME, 0)
		editor = settings.edit()
		editor.putString(self.functionKey, self.getName() + ":" + self.functionExpr)
		editor.commit()
