from Interpreter.ComplexFormatter import *
from Interpreter.R_string import *
from Interpreter.RadiusAngleFormatter import *

class DegreesFormatter(ComplexFormatter):
	def __init__(self, _context):
		ComplexFormatter.__init__(self, _context)

	def toString(self, complex):
		if complex.i:
			return self.toStringV(math.degrees(complex.r), 12) + R_string.character_degree
		else:
			formatter = RadiusAngleFormatter(self.view, True)
			return formatter.toString(complex)
