from Foundation.UndoController import *

from Framework.ChangeMemberAction import *
from Framework.AppendAction import *
from Framework.RemoveAction import *
from Framework.DragElementAction import *
from Framework.AttachConnectorAction import *
from Framework.DetachConnectorAction import *
from Framework.SetConnectorAction import *
from Foundation.MacroAction import *
from Framework.CustomBlock import *


class DiagramUC(UndoController):
    def __init__(self, key):
        UndoController.__init__(self)
        self.diagram = key

    # 处理Action生成请求
    def handle_request(self, component, req, params):
        from Framework.Diagram import Diagram
        if component.get_ancestor(Diagram).tag != self.diagram:
            return

        if not self.in_action:
            # print(component, req, 'params:', params)
            new_action = None
            if req == 'begin_macro':
                self.macro_action = MacroAction()
            elif req == 'end_macro':
                new_action = self.macro_action
                self.macro_action = None
            elif req == 'cancel_macro':
                self.macro_action = None
            elif req == 'change_member':
                new_action = ChangeMemberAction(component, params['getter'], params['setter'])
            if req == 'drag_begin':
                new_action = DragElementAction(component)
            elif req == 'drag_end':
                pass
            else:
                if isinstance(component, DataPort):
                    if req == 'attach_connector':
                        new_action = AttachConnectorAction(component, params['connector'])
                    elif req == 'detach_connector':
                        new_action = DetachConnectorAction(component, params['connector'])
                    elif req == 'set_connector':
                        new_action = SetConnectorAction(component, params['prev'], params['new'])
                    elif req == 'append':
                        if isinstance(component.parent, CustomBlock):
                            new_action = AppendAction(component)
                    elif req == 'remove':
                        if isinstance(component.parent, CustomBlock):
                            new_action = RemoveAction(component, params['index'])
                    else:
                        pass
                else:
                    if req == 'append':
                        new_action = AppendAction(component)
                    elif req == 'remove':
                        new_action = RemoveAction(component, params['index'])
                    else:
                        pass
            if new_action:
                if self.macro_action:
                    self.macro_action.add_action(new_action)
                else:
                    self._add_action(new_action)
        # self.__print()

