class BuildContext:
    def __init__(self, context, _manager, list):
        self.systemContext = context
        self.constManager = _manager
        self.tokenList = list
        self.errorMessage = ''

    def getSystemContext(self):
        return self.systemContext

