#sys.path.append('..')
from ExFramework.ExElement import *
from ExFramework.ExConnector import *
from ExFramework.ExStateMachine import *
from ExFramework.ExTransition import *
from ExFramework.ExInitialState import *
from ExFramework.ExChangeTrigger import *

from IdleState import *
from AddConnectorState import *
from MoveElementState import *
from MoveLineState import *


class PyCanvasStateMachine(ExStateMachine):
    def __init__(self, context):
        ExStateMachine.__init__(self, None, context)

        initial = ExInitialState(self, context)

        idle = IdleState(self, context)
        initial2normal = ExTransition(self, context, initial, idle)

        move_element = MoveElementState(self, context)
        idel2move_element = ExTransition(self, context, idle, move_element)
        idel2move_element.addTrigger(ExChangeTrigger(context, 'self.context.drawn'))
        idel2move_element.setGuard(lambda: isinstance(self.context.drawn, ExElement))
        move_element2idle = ExTransition(self, context, move_element, idle)
        move_element2idle.addTrigger(ExChangeTrigger(context, 'self.context.drawn'))

        move_line = MoveLineState(self, context)
        idel2move_line = ExTransition(self, context, idle, move_line)
        idel2move_line.addTrigger(ExChangeTrigger(context, 'self.context.drawn'))
        idel2move_line.setGuard(lambda: isinstance(self.context.drawn, ExConnector))
        move_line2idle = ExTransition(self, context, move_line, idle)
        move_line2idle.addTrigger(ExChangeTrigger(context, 'self.context.drawn'))

        add_connector = AddConnectorState(self, context)
        idle2add_connector = ExTransition(self, context, idle, add_connector)
        idle2add_connector.addTrigger(ExChangeTrigger(context, 'self.context.connector'))
        add_connector2idle = ExTransition(self, context, add_connector, idle)
        add_connector2idle.addTrigger(ExChangeTrigger(context, 'self.context.connector'))

        self.initial = initial

    def eventHandling(self, event_type, event):
        ExStateMachine.eventHandling(self, event_type, event)

