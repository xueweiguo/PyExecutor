import math
import copy

class Complex:
    def __init__(self, r = 0, i = 0):
        self.r = r
        self.i = i

    def addBy(self, other):
        self.r = self.r + other.r
        self.i = self.i + other.i

    @staticmethod
    def add(c1, c2):
        result = copy.copy(c1)
        result.addBy(c2)
        return result

    def subBy(self, other):
        self.r = self.r - other.r
        self.i = self.i - other.i

    @staticmethod
    def sub(c1, c2):
        result = copy.copy(c1)
        result.subBy(c2)
        return result

    def mulBy(self, other):
        if self.i != 0 or other.i != 0:
            temp = self.r * other.r - self.i * other.i
            self.i = self.r * other.i + self.i * other.r
            self.r = temp
        else:
           self.r = self.r * other.r

    @staticmethod
    def mul(c1, c2):
        result = copy.copy(c1)
        result.mulBy(c2)
        return result

    def divBy(self, other):
        if self.i != 0 or other.i != 0:
            temp = (self.r * other.r + self.i * other.i) / (other.r * other.r + other.i * other.i)
            self.i = (self.i * other.r - self.r * other.i) / (other.r * other.r + other.i * other.i)
            self.r = temp
        else:
            self.r = self.r / other.r
    @staticmethod
    def div(c1, c2):
        result = copy.copy(c1)
        result.divBy(c2)
        return result

    def getAbs(self):
        return math.hypot(self.r, self.i)

