from Framework.PropertyTab import *
from Framework.Note import *


class NoteTab(PropertyTab):
    def __init__(self, parent, name, note):
        PropertyTab.__init__(self, parent, name, note)
        self.note = note
        self.pack(side=TOP)
        self.text = Text(self, height=10, width=30)
        self.text.insert(INSERT, note.get_note())
        self.text.pack()

    def apply(self):
        note = self.text.get('1.0', END)
        if note != self.note.get_note():
            self.note.set_note(note)
