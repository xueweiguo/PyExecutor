import json
from Framework.FactoryManager import *
from Framework.TagFactory import *


class ComponentDict(object):
    def __init__(self):
        self.__dict = {}
        factory = TagFactory('tag_factory')
        self.register(factory)

    def register(self, component):
        #print('register,', component, component.tag)
        self.__dict[component.tag] = component

    def unregister(self, component):
        #print('unregister,', component, component.tag)
        if self[component.tag] == component:
            self.__dict.pop(component.tag)
        else:
            print('Unregister a component not in dict, tag:', component.tag)

    def __getitem__(self, tag):
        return self.__dict.get(tag)

    @property
    def dict(self):
        return self.__dict

    def create_tag(self):
        return self.dict['tag_factory'].createTag()

    def clear(self):
        self.__dict.clear()
        self.register(TagFactory('tag_factory'))

    def new(self):
        from Framework.TopDiagram import TopDiagram
        self.clear()
        TopDiagram(self, 'Top', FactoryManager().mode).construct(None)

    def save(self, fn):
        if fn:
            f = open(fn.name, 'w', encoding='utf-8')
            f.write(self.to_string())
            f.close()
            return True
        else:
            return False

    def to_string(self):
        from Framework.JsonAdapter import JsonAdapter
        self.clean()
        adapter = JsonAdapter()
        jsonDict = adapter.ToJsonDict(self)
        return json.dumps(jsonDict, ensure_ascii=False, indent=4)

    def load(self, fn):
        if fn:
            f = open(fn.name, 'r', encoding='utf-8')
            jsonString = f.read()
            self.from_string(jsonString)
            f.close()
            return True
        else:
            return False

    def from_string(self, string):
        from Framework.JsonAdapter import JsonAdapter
        json_dict = json.loads(string)
        JsonAdapter().ToComponentDict(json_dict, self)
        for c in self.__dict.values():
            c.set_dict(self)

    def clean(self):
        from Framework.DiagramTreeVisitor import DiagramTreeVisitor
        top = self['Ex1']
        # 检索有效元素
        tv = DiagramTreeVisitor()
        top.accept(tv)

        # 确认无效元素
        remove_list = []
        for key,value in self.dict.items():
            if not tv.in_set(key):
                if key != 'tag_factory':
                    remove_list.append(key)
        # 排除无效元素
        for key in remove_list:
            self.dict.pop(key)






