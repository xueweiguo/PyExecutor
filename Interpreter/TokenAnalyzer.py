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
        #m = re.match('1\+2', '1+2')
        m = re.search(context.pattern.pattern, context.content)
        #if m.find():
        if m:
            start = m.start()
            end = m.end()
            if start > 0:
                #context.tokenList.insert(context.index, Token(context.content.substring(0, start)))
                str = context.content[0:start]
                context.tokenList.insert(context.index, Token(str))
                context.index = context.index + 1
            if end < len(context.content):
                #context.tokenList.insert(context.index, Token(context.pattern.type.content.substring(start, end)))
                #context.content = context.content.substring(end.content.length())
                context.tokenList.insert(context.index, Token(context.pattern.type,context.content[start:end]))
                context.index = context.index + 1
                context.content = context.content[end:len(context.content)]
                self.analyzeContent(context)
            else:
                #token.setContent(context.content.substring(start, end))
                token.setContent(context.content[start:end])
                token.setType(context.pattern.type)
                #context.content = context.content.substring(end.content.length())
                context.content = context.content[end:len(context.content)]
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


