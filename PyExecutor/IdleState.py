from ExFramework.ExState import *
from ExFramework.ExBlock import *
from ExFramework.ExConnector import *
from ExFramework.ExOutputPort import *


class IdleState(ExState):
    def __init__(self, owner, context):
        ExState.__init__(self, owner, context)

    def entry(self):
        self.context.drawn = None
        self.context.new_connector = None
        ExState.entry(self)

    def eventHandling(self, event_type, event):
        if event_type == 'LButtonDown':
            self.context.drawn = self.context.find_overlapping(event.x, event.y)
            self.context.set_active(self.context.drawn)
            self.context.start = event
        if event_type == 'RButtonDown':
            self.hit = self.context.find_overlapping(event.x, event.y)
            if self.hit:
                self.context.set_active(self.hit)
                menu = self.hit.create_popup(self)
                if menu:
                    menu.post(event.x_root, event.y_root)
        elif event_type == 'LButtonDoubleClick':
            hit = self.context.find_overlapping(event.x, event.y)
            if hit:
                if isinstance(hit, ExOutputPort):
                    connector = self.context.factory.make_connector()
                    self.context.register_element(connector)
                    connector.attach(self.context.canvas)
                    connector.setOutputPort(hit)
                    self.context.connector = connector
            else:
                if self.context.element_type:
                    element = self.context.factory.make_element(self.context.element_type)
                    self.context.register_element(element)
                    element.attach(self.context.canvas, event.x, event.y)
                    self.context.canvas.configure(cursor='arrow')
        elif event_type == 'Key':
            pass

        ExState.eventHandling(self, type, event)

    def on_command(self, cmd):
        if cmd == 'Delete':
            if isinstance(self.hit, ExBlock):
                for port in self.hit.children:
                    if isinstance(port, ExInputPort):
                        if port.connector:
                            c = port.connector
                            c.disconnect()
                            self.context.remove_element(c)

                for port in self.hit.children:
                    if isinstance(port, ExOutputPort):
                        for c in port.connectors:
                            c.disconnect()
                            self.context.remove_element(c)
            elif isinstance(self.hit, ExConnector):
                self.hit.disconnect()
            else:
                pass

            self.context.remove_element(self.hit)
            self.hit = None
        if cmd == 'SetProperty':
            dlg = self.hit.create_property_dlg()
            dlg.do_modal()

