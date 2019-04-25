import abc
import math


class ComplexFormatter(metaclass=abc.ABCMeta):
	MIN_NUMBER = 1e-15

	def __init__(self,  _context):
		self.view = _context

	def toStringC(self, complex):
		return None
	
	def toStringV(self, value, length):
		if(math.fabs(value) < self.MIN_NUMBER):
			value = 0

		#format_str = "%." + "%d".format(length) + "g"
		#real = format_str.format(value)
		real = str(value)

		#remove the 0 at the end of number.
		before = None
		after = None
		e_index = real.find("e")
		if(e_index != -1):
			before = real[0:e_index]
			after = real[e_index:]
		else:
			before = real

		point_index = before.find(".")
		if(point_index != -1):
			index = len(before) - 1
			while(index >= point_index and
					(before[index] == '0' or before[index] == '.')):
				index = index - 1
			real = before[0:index + 1]
		else:
			real = before

		if after:
			real = real + after

		return real
