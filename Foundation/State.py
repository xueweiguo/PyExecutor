class State:
    def __init__(self, owner, context):
        self.owner = owner
        self.context = context
        self.transitions = []

    def add_transition(self, t):
        self.transitions.append(t)

    def entry(self):
        for t in self.transitions:
            t.entry()
        if self.owner:
            self.owner.active = self

    def exit(self):
        if self.owner:
            self.owner.active = None

    def event_handling(self, e_type, event):
        for t in self.transitions:
            if t.event_handling(e_type, event):
                return True

