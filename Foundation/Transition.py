class Transition:
    def __init__(self, owner, context, s, t):
        self.owner = owner
        self.context = context
        self.source = s
        s.add_transition(self)
        self.target = t
        self.triggers = []
        self.__guard = None

    def add_trigger(self, t):
        self.triggers.append(t)

    def set_guard(self, g):
        self.__guard = g

    def entry(self):
        for t in self.triggers:
            t.entry()

    def effect(self):
        pass

    def event_handling(self, type_str, event):
        if self.__guard:
            if not self.__guard():
                return

        for t in self.triggers:
            if t.check():
                self.transition()
                break

    def transition(self):
        self.source.exit()
        self.target.entry()


