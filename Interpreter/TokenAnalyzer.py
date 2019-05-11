import re
from Interpreter.Token import *

#语法分析
class TokenAnalyzer:
    class Context:
        def __init__(self):
            self.tokenList = []
            self.index = 0
            self.pattern = None
            self.content = None
    #分析上下文
    def analyzeContent(self, context):
        token = context.tokenList[context.index]
        m = re.search(context.pattern.pattern, context.content)
        if m:
            start = m.start()
            end = m.end()
            if start > 0:
                str = context.content[0:start]
                context.tokenList.insert(context.index, Token(str))
                context.index = context.index + 1
            if end < len(context.content):
                context.tokenList.insert(context.index, Token(context.pattern.type,context.content[start:end]))
                context.index = context.index + 1
                context.content = context.content[end:len(context.content)]
                self.analyzeContent(context)
            else:
                token.setContent(context.content[start:end])
                token.setType(context.pattern.type)
                context.content = context.content[end:len(context.content)]
        else:
            token.setContent(context.content)

    #对表达是进行语法分析
    def analyzeToken(self, strInput, pattern_list):
        tokenList = []
        #设定初始状态
        tokenList.append(Token(strInput))
        #进行递归语法分析，返回语法树
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


