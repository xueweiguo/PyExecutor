#sys.path.append('..')
from Framework.Connector import *
from Framework.Block import *
from Framework.Note import *
from Foundation.StateMachine import *
from Foundation.Transition import *
from Foundation.InitialState import *
from Foundation.ChangeTrigger import *

from IdleState import *
from AddConnectorState import *
from MoveElementState import *
from MoveConnectorState import *


class CanvasStateMachine(StateMachine):
    def __init__(self, context):
        StateMachine.__init__(self, None, context)
        # 初始状态
        self.initial = InitialState(self, context)
        # 空闲状态
        idle = IdleState(self, context)
        initial2idle = Transition(self, context, self.initial, idle)
        # 移动要素状态
        move_element = MoveElementState(self, context)
        idel2move_element = Transition(self, context, idle, move_element)
        idel2move_element.add_trigger(ChangeTrigger(context, 'self.context.drawn'))
        idel2move_element.set_guard(
            lambda: isinstance(self.context.drawn, Block) or isinstance(self.context.drawn, Note))
        move_element2idle = Transition(self, context, move_element, idle)
        move_element2idle.add_trigger(ChangeTrigger(context, 'self.context.drawn'))
        # 添加链接线状态
        add_connector = AddConnectorState(self, context)
        idle2add_connector = Transition(self, context, idle, add_connector)
        idle2add_connector.add_trigger(ChangeTrigger(context, 'self.context.connector'))
        add_connector2idle = Transition(self, context, add_connector, idle)
        add_connector2idle.add_trigger(ChangeTrigger(context, 'self.context.connector'))
        # 移动连接线状态
        move_connector = MoveConnectorState(self, context)
        idel2move_line = Transition(self, context, idle, move_connector)
        idel2move_line.add_trigger(ChangeTrigger(context, 'self.context.drawn'))
        idel2move_line.set_guard(lambda: isinstance(self.context.drawn, Connector))
        move_line2idle = Transition(self, context, move_connector, idle)
        move_line2idle.add_trigger(ChangeTrigger(context, 'self.context.drawn'))


