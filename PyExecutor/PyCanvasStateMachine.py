import sys
sys.path.append('..')
from ExFramework.ExStateMachine import *
from ExFramework.ExTransition import *
from ExFramework.ExInitialState import *
from ExFramework.ExChangeTrigger import *

from PyCanvasIdleState import *
from PyCanvasAddConnectorState import *
from PyCanvasMoveElementState import *

class PyCanvasStateMachine(ExStateMachine):
    def __init__(self, context):
        ExStateMachine.__init__(self, None, context)

        initial = ExInitialState(self, context)

        idle = PyCanvasIdleState(self, context)
        initial2normal = ExTransition(self, context, initial, idle)

        move_element = PyCanvasMoveElementState(self, context)
        idel2move_element = ExTransition(self, context, idle, move_element)
        idel2move_element.addTrigger(ExChangeTrigger(context, 'self.context.drawn'))
        move_element2idle = ExTransition(self, context, move_element, idle)
        move_element2idle.addTrigger(ExChangeTrigger(context, 'self.context.drawn'))

        add_connector = PyCanvasAddConnectorState(self, context)
        idle2add_connector = ExTransition(self, context, idle, add_connector)
        idle2add_connector.addTrigger(ExChangeTrigger(context, 'self.context.connector'))
        add_connector2idle = ExTransition(self, context, add_connector, idle)
        add_connector2idle.addTrigger(ExChangeTrigger(context, 'self.context.connector'))

        self.initial = initial

    def eventHandling(self, type, event):
        ExStateMachine.eventHandling(self, type, event)

