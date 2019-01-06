from enum import *

class TokenType(Enum):
    NoType = 1
    Operator = 2
    Parenthese = 3
    Comma = 4
    Number = 5
    Parameter = 6
    FunctionName = 7


class Token:
    def __init__(self, p1, p2=None):
        if p2 is None:
            self.mType = TokenType.NoType
            self.mContent = p1
        else:
            self.mType = p1
            self.mContent = p2

    def getType(self):
        return self.mType

    def getContent(self):
        return self.mContent

    def setType(self, type):
        self.mType = type

    def isNoType(self):
        return (self.mType == EType.NoType)

    def setContent(self, content):
        self.mContent = content
