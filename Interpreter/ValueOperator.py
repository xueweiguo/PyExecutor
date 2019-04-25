import abc
from Interpreter.Complex import *

class ValueOperator():
    def __init__(self, string):
        self.operatorString = string
        self.evaluateResult = Complex()
        self.errorMessage = 0

    def evaluate(self, value1, value2):
        return False

    def getResult(self):
        return self.evaluateResult

    def getErrorMessage(self):
        return self.errorMessage

    def getOperatorString(self):
        return self.operatorString
