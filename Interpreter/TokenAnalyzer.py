import re
from Interpreter.Token import *

class TokenAnalyzer:
    class Context:
        def __init__(self):
            self.tokenList = []
            self.index = 0
            self.pattern = None
            self.content = None

    def analyzeContent(self, context):
        token = context.tokenList[context.index]
        m = re.match(context.pattern, context.content)
        if m.find():
            start = m.start()
            end = m.end()
            if start > 0:
                context.tokenList.insert(context.index, Token(context.content.substring(0, start)))
            if end < len(context.content):
                context.tokenList.insert(context.index, Token(context.pattern.type, context.content.substring(start, end)))
                context.content = context.content.substring(end, context.content.length())
                self.analyzeContent(context)
            else:
                token.setContent(context.content.substring(start, end))
                token.setType(context.pattern.type)
                context.content = context.content.substring(end, context.content.length())
        else:
            token.setContent(context.content)

    
    def analyzeToken(self, strInput, pattern_list):
        tokenList = []
        tokenList.append(Token(strInput))
        for pattern in pattern_list:
            index = 0
            while index < len(tokenList):
                token = tokenList[index]
                if token.isNoType():
                    content = token.getContent()
                    context = self.Context()
                    context.tokenList = tokenList
                    context.index = index
                    context.pattern = pattern
                    context.content = content
                    self.analyzeContent(context)
                index = index + 1
        return tokenList


