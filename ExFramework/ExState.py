class ExState:
    def __init__(self, owner, context):
        self.owner = owner
        self.context = context
        self.active = None
        self.initial = None
        self.final = None
        self.transitions = []
        print(self)

    def start(self):
        self.eventHandling(event)

    def addTransition(self, t):
        self.transitions.append(t)

    def entry(self):
        for t in self.transitions:
            t.entry()
        self.active = self.initial
        if self.active:
            self.active.entry()
        if self.owner:
            self.owner.active = self
        print(type(self), 'entry')

    def exit(self):
        self.active = self.final
        if self.owner:
            self.owner.active = None
        print(type(self), 'exit')

    def eventHandling(self, type, event):
        for t in self.transitions:
            if t.eventHandling(type, event):
                return True
        if self.active:
            return self.active.eventHandling(type, event)
        return False

