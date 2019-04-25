from tkinter import *

from Foundation.StateMachine import *
from Foundation.InitialState import *
from Foundation.FinalState import *
from Foundation.Transition import *
from Foundation.TimerTrigger import *
from Foundation.ValueTrigger import *

from Foundation.Timer import *


class TrafficLight:
    def __init__(self, parent):
        self.canvas = Canvas(parent, bg='#FFFFFF', relief=SUNKEN)
        self.canvas.config(width=300, height=100)
        self.canvas.pack()
        self.light = dict()
        self.light['red'] = \
            self.canvas.create_oval(10, 10, 90, 90, fill='#FF0000', disabledfill='#770000')
        self.light['yellow'] = \
            self.canvas.create_oval(110, 10, 190, 90, fill='#FFFF00', disabledfill='#777700')
        self.light['green'] = \
            self.canvas.create_oval(210, 10, 290, 90, fill='#00FF00', disabledfill='#007700')
        self.stop()

    def light_on(self, light):
        self.canvas.itemconfig(self.light[light], state=NORMAL)

    def light_off(self, light):
        self.canvas.itemconfig(self.light[light], state=DISABLED)

    def toggle(self, light):
        if self.canvas.itemcget(self.light[light], 'state') == NORMAL:
            self.light_off(light)
        else:
            self.light_on(light)

    def stop(self):
        self.light_off('red')
        self.light_off('yellow')
        self.light_off('green')
        self.run = False


class LightState(State):
    def __init__(self, owner, color, context, blink=False):
        State.__init__(self, owner, context)
        self.color = color
        self.blink = blink
        self.counter = 0

    def entry(self):
        State.entry(self)
        self.context.light_on(self.color)
        self.counter = 0

    def exit(self):
        State.exit(self)
        self.context.light_off(self.color)

    def event_handling(self, e_type, event):
        if self.blink:
            self.counter = self.counter + 1
            if self.counter >= 5:
                self.context.toggle(self.color)
                self.counter = 0
        State.event_handling(self, e_type, event)


class TrafficLightMachine(StateMachine):
    def __init__(self, context):
        StateMachine.__init__(self, None, context)

        # 初始状态
        self.initial = InitialState(self, context)
        # 红灯
        red = LightState(self, 'red', context)
        # 绿灯
        green = LightState(self, 'green', context)
        # 绿灯闪烁
        green5s= LightState(self, 'green', context, True)
        # 黄灯 1s间隔闪烁
        yellow = LightState(self, 'yellow', context)
        # 红灯 1s闪烁
        red5s = LightState(self, 'red', context, True)
        # 终止状态
        final = FinalState(self, context)

        # 初始状态-红灯 无条件迁移
        i2r = Transition(self, context, self.initial, red)

        # 红灯-绿灯
        r2g = Transition(self, context, red, green)
        #5s迁移
        r2g.add_trigger(TimerTrigger(context, 5))

        # 绿灯-绿灯闪
        g2g5 = Transition(self, context, green, green5s)
        # 5s迁移
        g2g5.add_trigger(TimerTrigger(context, 3))

        # 绿灯闪-黄灯
        g52y = Transition(self, context, green5s, yellow)
        #5s迁移
        g52y.add_trigger(TimerTrigger(context, 2))

        # 黄灯-红灯
        y2r = Transition(self, context, yellow, red)
        # 3s迁移
        y2r.add_trigger(TimerTrigger(context, 3))

        # 红灯-红灯闪
        r2f = Transition(self, context, red, red5s)
        # 监控context.run是否为False
        r2f.add_trigger(ValueTrigger(context, 'self.context.run', False))

        # 红灯闪-终了
        r5s2f = Transition(self, context, red5s, final)
        # 5s
        r5s2f.add_trigger(TimerTrigger(context, 5))

    def event_handling(self, event_type, event):
        StateMachine.event_handling(self, event_type, event)

    def stop(self):
        self.context.run = False

    def entry(self):
        StateMachine.entry(self)
        self.context.run = True

    def exit(self):
        self.context.stop()


if __name__ == '__main__':
    root = Tk()
    tl = TrafficLight(root)
    tlm = TrafficLightMachine(tl)
    Button(root, text='Start', command=tlm.entry).pack(side=LEFT, fill=X, expand=1)
    Button(root, text='Stop', command=tlm.stop).pack(side=LEFT, fill=X, expand=1)
    t = Timer(root, 100, lambda:tlm.event_handling('on_timer', ''))
    t.start()
    root.mainloop()

