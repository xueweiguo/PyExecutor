import abc


class TokenPatternFactory(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def createPatterns(self, funcitonManager, constManager):
		pass
