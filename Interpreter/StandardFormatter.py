from Interpreter.ComplexFormatter import *


class StandardFormatter(ComplexFormatter):
	def __init__(self, _context):
		ComplexFormatter.__init__(self,_context)

	def toString(self, complex):
		valueString = ''
		if(complex.r != 0):
			if(complex.i != 0):
				valueString = valueString + ComplexFormatter.toStringV(self, complex.r, 8)
			else:
				valueString += valueString + ComplexFormatter.toStringV(self, complex.r, 12)

		imaginary = None
		if(len(valueString) > 0):
			imaginary = ComplexFormatter.toStringV(self, complex.i, 8)
		else:
			imaginary = ComplexFormatter.toStringV(self, complex.i, 12)

		#if(imaginary.compareTo("0") != 0):
		if imaginary != "0":
			if(complex.i > 0):
				valueString = valueString + "+"
				imaginary = imaginary + "i"
				valueString = valueString + imaginary

		if(len(valueString) == 0):
			valueString = "0"

		return valueString
