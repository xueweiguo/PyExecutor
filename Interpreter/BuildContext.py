class BuildContext:
    def __init__(self, context, _manager, list):
        self.systemContext = context
        self.constManager = _manager
        self.tokenList = list

    def getSystemContext(self):
        return self.systemContext

