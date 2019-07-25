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

    # 对表达是进行语法分析
    def analyze_token(self, strInput, pattern_list):
        # 初始化Token列表2
        tokenList = []
        # 导入原始文字序列
        tokenList.append(Token(strInput))
        # 用全部TokenPattern输入字符序列进行拆分
        for pattern in pattern_list:
            index = 0
            #对表达式进行语法范式解释
            while index < len(tokenList):
                if tokenList[index].isNoType():
                    # Token内容拆分
                    index = self.analyze_content(tokenList, index, pattern)
                else:
                    index = index + 1
        return tokenList

    # 拆分Token
    def analyze_content(self, tokenList, index, pattern):
        token = tokenList[index]
        content = token.getContent()
        # 检查匹配部分
        m = re.search(pattern.pattern, content)
        if m:
            start = m.start()
            end = m.end()
            if start > 0:
                # 开始位置不是最开始，截取开始位置之前的内容插入TokenList
                str = content[0:start]
                tokenList.insert(index, Token(str))
                index = index + 1
            if end < len(content):
                # 结束位置之后还有其他内容
                tokenList.insert(index, Token(pattern.type, content[start:end]))
                token.setContent(content[end:len(content)])
                return index + 1  # 下次解析剩余部分
            else:
                # 结束位置没有其他内容
                token.setContent(content[start:end])
                token.setType(pattern.type)
                return index + 1  # 下次解析下一个Token
        else:
            return index + 1
