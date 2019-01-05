class ConstManager:
	def __init__(self):
		self.constMap = dict()
	
	def registerConst(self, key, value):
		self.constMap[key] = value

	def consts(self):
		return self.constMap.keys()

	def find(self, key):
		return self.constMap.get(key)

	def getConstCount(self):
		return len(self.constMap.keys())
