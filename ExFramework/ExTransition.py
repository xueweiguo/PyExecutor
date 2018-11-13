class ExTransition:
    def __init__(self, owner, context, s, t):
        self.owner = owner
        self.context = context
        self.source = s
        s.addTransition(self)
        self.target = t
        self.triggers = []
        print(self)

    def addTrigger(self, t):
        self.triggers.append(t)

    def entry(self):
        for t in self.triggers:
            t.entry()

    def guard(self):
        return True

    def effect(self):
        pass

    def eventHandling(self, type, event):
        for t in self.triggers:
            if t.check():
                self.transition()

    def transition(self):
        self.source.exit()
        self.target.entry()


