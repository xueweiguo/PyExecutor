from Foundation.Timer import *
from Foundation.ScrollCanvas import *
from Framework.BuilderDirector import *
from Framework.ExecuteStarter import *
from Framework.ExecuteStopper import *
from Framework.ExecuteDriver import *


class DiagramView(ScrollCanvas):
    def __init__(self, parent, observer, color):
        ScrollCanvas.__init__(self, parent, ExecCanvas, color)
        self.canvas.observable().attach(observer)
        self.timer = Timer(parent, 10, self.on_timer)
        # 构建元素字典
        self._dict = ComponentDict()
        self.__diagram = None
        self.element_type = None
        self.drawn = None
        self.start = None
        self.__selected = None
        self.connector = None
        self.add = None
        self.context = None

    @property
    def dict(self):
        return self._dict

    @property
    def diagram(self):
        return self.__diagram

    @property
    def top_diagram(self):
        return self._dict['Ex1']

    @property
    def type(self):
        return self.top_diagram.type

    def set_diagram(self, diagram):
        if not self.__diagram == diagram:
            if self.__diagram:
                self.__diagram.detach_canvas()
            self.__diagram = diagram
            if self.__diagram:
                self.__diagram.attach_canvas(self.canvas)
        self.drawn = None
        self.element_type = None
        self.drawn = None
        self.start = None
        self.__selected = None
        self.connector = None
        self.update()

    def top_changed(self):
        FactoryManager().mode = self.top_diagram.type
        self.set_diagram(self.top_diagram)
        self.make_toolbar(self.master.toolbar)
        self.make_menu(self.master.top_menu)

    def new(self):
        self.stop_debug()
        self.set_diagram(None)
        self._dict.new()
        self.top_changed()

    def undo(self):
        self.select(None)
        if self.diagram:
            self.diagram.undo()
        self.update_ui()

    def redo(self):
        self.select(None)
        if self.diagram:
            self.diagram.redo()
        self.update_ui()

    def start_debug(self):
        self.context = FactoryManager().factory('element').make_context()
        starter = ExecuteStarter(self.context)
        self.top_diagram.accept(starter)
        self.timer.start()
        self.after(0, self.update_ui)

    def stop_debug(self):
        if self.is_running():
            self.timer.stop()
            stopper = ExecuteStopper(self.context)
            self.top_diagram.accept(stopper, 'LRD')
            self.context = None
            self.after(0, self.update_ui)

    def on_timer(self):
        driver = ExecuteDriver(self.context)
        self.top_diagram.accept(driver)

    def is_running(self):
        return self.timer.is_running()

    def build_source(self, type):
        builder = FactoryManager().factory('builder').make_builder(type)
        if builder:
            director = BuilderDirector(builder)
            self.top_diagram.accept(director)
            builder.get_result()

    def update_ui(self):
        pass

    def del_current(self):
        pass

    def append_element(self, element):
        self.diagram.append(element)
        if self.is_running():
            starter = ExecuteStarter(self.context)
            element.accept(starter)

    def remove_element(self, element):
        if self.is_running():
            element.stop(self.context)
        self.diagram.remove(element)

    # 根据tags查找要素
    def find_element(self, tags):
        tag_count = len(tags)
        if tag_count > 0:
            if tags[tag_count - 1] == 'current':
                tag_count = tag_count - 1
            if tag_count > 0:
                element = self.component(tags[0])
                if element != None:
                    if tag_count > 1:
                        child = element.find_child(tags[1])
                        if child:
                            return child
                return element
        return None

    def component(self, tag):
        dot_index = tag.find('.')
        if dot_index != -1:
            tag = tag[0: dot_index]
        return self.diagram.dict[tag]

    # 根据坐标查找要素
    def find_overlapping(self, x, y):
        ids = self.canvas.find_overlapping(x - 1, y - 1, x + 1, y + 1)
        # print('ids=', ids)
        count = len(ids)
        if count > 0:
            tags = self.canvas.gettags(ids[count - 1])
            if len(tags) > 0:
                return self.find_element(tags)
        return None

    def select(self, act):
        if self.__selected != act:
            if self.__selected:
                self.__selected.set_color('black')
                self.__selected = None
            if act:
                act.set_color('red')
                self.__selected = act

    def selected(self):
        return self.__selected

    def grid(self, event):
        event.x = self.canvas.canvasx(event.x, gridspacing=4)
        event.y = self.canvas.canvasy(event.y, gridspacing=4)
        return event

    def make_editbar(self, toolbar):
        raise NotImplementedError

    # 构建工具条
    def make_toolbar(self, toolbar):
        raise NotImplementedError

    # 构建菜单项
    def make_menu(self, menu):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def load(self, fn):
        self.new()
        self.dict.load(fn)
        self.top_changed()

    def save(self, fn):
        self.canvas.clear_state()
        self.dict.save(fn)

    def show_info(self):
        from Framework.StatsVisitor import StatsVisitor
        sv = StatsVisitor()
        self.top_diagram.accept(sv)
        sv.get_result()




