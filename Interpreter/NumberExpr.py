import math
from Interpreter.Complex import *
from Interpreter.TerminalExpr import *
class NumberExpr(TerminalExpr):
    def __init__(self, val = None):
        TerminalExpr.__init__(self)
        self.complex = val

    @staticmethod
    #def buildExpr(cls):
    def buildExpr(context):
        #value = context.tokenList.removeFirst().getContent()
        value = context.tokenList.pop(0).getContent()
        constValue = context.constManager.find(value)
        if constValue:
            return NumberExpr(constValue)
        else:
            #index = value.indexOf("∠")
            index = value.find("∠")
            if (index != -1):
                radius = float(value.substring(0, index))
                angle = 0
                if (value.substring(value.length() - 1).compareTo("°") == 0):
                    degrees = float(value.substring(index + 1, value.length() - 1))
                    cycles = math.floor(degrees / 360)
                    if (degrees < 0):
                        cycles = cycles + 1
                    angle = math.radians(degrees - cycles * 360)
                else:
                    angle = float(value.substring(index + 1))
                return NumberExpr(Complex(radius * math.cos(angle), radius * math.sin(angle)))
            #elif (value.substring(value.length() - 1).compareTo("i") == 0):
            elif (value[len(value) - 1]==("i")):
                if (value.length() == 1):
                    return NumberExpr(Complex(0, 1))
                else:
                    return NumberExpr(Complex(0, float(value.substring(0, value.length() - 1))))
            #elif (value.substring(value.length() - 1).compareTo("°") == 0):
            elif (value[len(value) - 1]==("°")):
                return NumberExpr(Complex(math.radians(float(value.substring(0, value.length() - 1)))))
            #elif (value.substring(value.length() - 1).compareTo("%") == 0):
            elif (value[len(value) - 1]==("%")):
                return NumberExpr(Complex(float(value.substring(0, value.length() - 1)) / 100))
            else:
                return NumberExpr(Complex(float(value)))

    def evaluate(self, context):
        context.setCurrentResult(self.complex)
        return True
