from Foundation.State import *
from Framework.Block import *
from Framework.Connector import *
from Framework.OutputPort import *
from Framework.FactoryManager import *


class IdleState(State):
    def __init__(self, owner, context):
        State.__init__(self, owner, context)
        self.event = None

    def entry(self):
        self.event = None
        self.context.drawn = None
        self.context.new_connector = None
        State.entry(self)

    def event_handling(self, event_type, event):
        if event_type == 'LButtonDown':
            self.context.drawn = self.context.find_overlapping(event.x, event.y)
            self.context.select(self.context.drawn)
            self.context.start = event
            self.context.after(500, self.reset_element_type)
        elif event_type == 'LButtonUp':
            self.context.canvas.configure(cursor='arrow')
            self.context.after(500, self.reset_element_type)
        elif event_type == 'RButtonDown':
            self.hit = self.context.find_overlapping(event.x, event.y)
            if self.hit:
                self.context.select(self.hit)
                menu = self.hit.create_popup(self)
            else:
                menu = self.context.create_popup()
            if menu:
                menu.post(event.x_root, event.y_root)
            self.event = event
            self.reset_element_type()
        elif event_type == 'LButtonDoubleClick':
            if self.context.element_type:
                factory = FactoryManager().factory('element')
                element = factory.make_element(self.context.dict,
                                               self.context.diagram,
                                               self.context.element_type)
                element.set_position(event.x, event.y)
                self.context.append_element(element)
                self.context.element_type = None
            else:
                hit = self.context.find_overlapping(event.x, event.y)
                if hit:
                    if isinstance(hit, OutputPort):
                        factory = FactoryManager().factory('element')
                        connector = factory.make_connector(self.context.dict, self.context.diagram)
                        connector.add_begin()
                        self.context.append_element(connector)
                        connector.attach_output(hit)
                        self.context.connector = connector
                    else:
                        dlg = hit.create_property_dlg()
                        if dlg:
                            dlg.do_modal()
            self.context.canvas.configure(cursor='arrow')
            self.reset_element_type()
        elif event_type == 'Key':
            self.reset_element_type()
        elif event_type == 'Command':
            self.on_command(event)
        State.event_handling(self, type, event)

    def on_command(self, event):
        if event == 'Delete':
            selected = self.context.selected()
            self.context.select(None)
            self.context.remove_element(selected)
            self.context.update_ui()
        elif event == 'Copy':
            self.context.src_tag = self.context.selected().tag
            self.context.update_ui()
        elif event == 'Paste':
            src = self.context.diagram.dict[self.context.src_tag]
            if src:
                des = src.clone()
                if self.event:
                    des.set_position(self.event.x, self.event.y)
                else:
                    des.set_position(0, 0)
                self.context.append_element(des)

        elif event == 'SetProperty':
            self.hit.create_property_dlg().do_modal()

    def reset_element_type(self):
        self.context.element_type=None



