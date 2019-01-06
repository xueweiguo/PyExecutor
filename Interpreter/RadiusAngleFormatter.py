from Interpreter.ComplexFormatter import *
from Interpreter.R_string import *


class RadiusAngleFormatter(ComplexFormatter):
	def __init__(self, _context, deg):
		ComplexFormatter.__init__(self, _context)
		self.asDegrees = deg

	def toString(self, complex):
		radius = math.hypot(complex.r, complex.i)
		angle = 0
		
		if complex.r:
			if complex.i > 0:
				angle = math.pi / 2
			elif complex.i < 0:
				angle = math.pi  * 3 / 2
			else:
				angle = 0
		else:
			angle = math.atan(complex.i / complex.r)
			if complex.r < 0:
				angle = angle + math.pi
			elif complex.i < 0:
				angle = angle + math.pi * 2
		if radius == 0:
			return '0'
		else:
			result = toStringV(self, radius, 8)
			degreeChar = R_string.character_degree
			angleChar = R_string.character_angle
			if angle:
				if self.asDegrees:
					degrees = math.degrees(angle)
					result = result + angleChar + ComplexFormatter.toString(self, degrees, 8) + degreeChar
				else:
					result += angleChar + ComplexFormatter.toString(self, angle, 8)

			return result
