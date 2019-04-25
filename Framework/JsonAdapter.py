#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
from Framework.Component import *
from Framework.TagFactory import *
from Framework.ExecContext import *


class JsonAdapter(object):
    __instance = None

    def __new__(cls):
        if not JsonAdapter.__instance:
            cls.__instance = super(JsonAdapter, cls).__new__(cls)
            # 自定义系列化类型
            cls.__instance.__serializable = []
        return JsonAdapter.__instance

    # 对象初始化函数
    # 每次构建时都会被调用，因此成员初始化在__new__中实现
    def __init__(self):
        pass

    def register_serializable(self, cls):
        self.__serializable.append(cls)

    def ToJsonDict(self, componentDict):
        jsonDict = {}
        for key, element in componentDict.dict.items():
            jsonDict.update({key: self.element2JsonDict(element)})
        return jsonDict

    def element2JsonDict (self, element):
        for cls in self.__serializable:
            if isinstance(element, cls):
                return self.element2JsonDictInner(element)

        if isinstance(element, Component):
            return self.element2JsonDictInner(element)
        elif isinstance(element, TagFactory):
            return self.element2JsonDictInner(element)
        elif isinstance(element, ExecContext):
            return {}
        elif isinstance(element, Canvas):
            return {}
        elif isinstance(element, ComponentDict):
            return {}
        else:
            return element

    def element2JsonDictInner (self, element):
        elementJsonDict = {}
        elementJsonDict.update({"__ModuleName__": element.__class__.__module__})
        elementJsonDict.update({"__ClassName__": element.__class__.__name__})
        elementJsonDict.update({"__ClassData__": self.elementData2JsonDict(element)})
        return elementJsonDict

    def elementData2JsonDict(self, element):
        elementDataJsonDict = {}
        for key in element.__dict__.keys():
           subElement =  getattr(element,key)
           elementDataJsonDict.update({key : self.element2JsonDict(subElement)})
        return elementDataJsonDict

    def ToComponentDict(self, jasonDict, objDict) :
        for key, element in jasonDict.items():
            self.emementToComponentDict(key, element, objDict)

    def emementToComponentDict(self, key, element, componentDict) :
        if "__ClassData__" in element:
            obj = self.createObject(element)
            componentDict.register(obj)
        else:
            componentDict.update({key: element})

    def createObject(self, element) :
        if element["__ClassName__"] in element["__ModuleName__"]:
            # 文件夹和文件名一样的时候的特别处理
            module_ = __import__(element["__ModuleName__"])
            module_ = getattr(module_, element["__ClassName__"])
        else:
            module_ = __import__(element["__ModuleName__"])
        class_ = getattr(module_, element["__ClassName__"])
        # print(class）
        try:
            obj = class_()
        except Exception as e:
            print(e, ',class=', class_)

        dataDict = element["__ClassData__"]
        for datakey, data in dataDict.items():
            #子对象有无
            if data != None and isinstance(data, dict) and "__ClassData__" in data:
                subObj = self.createObject(data)
                setattr(obj, datakey, subObj)
            else:
                # print(datakey, data)
                setattr(obj, datakey, data)
        return obj

