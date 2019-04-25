#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter.filedialog import *
from ExFramework.JsonAdapter import *
from FunctionBlockDiagram.SinFun import *

class TestCBase(JsonAdapter):
    def __init__(self):
        JsonAdapter.__init__(self)
        self.numBase = 0
        self.strBase = "Base"
    def tostring(self):
        return str(self.numBase)+self.strBase
    def Speak(self):
        print("TestBase")
        self.SpeakInside()

    def SpeakInside(self):
        print("TestBase::SpeakInside")

class TestC(TestCBase):
    def __init__(self):
        TestCBase.__init__(self)
        self.numC = 0
        self.strC = ""

class Test2(TestC):
    def __init__(self, parent = None):
        TestC.__init__(self)
        self.__parent = parent
        self.str2 = ""

class Test(JsonAdapter):
    def __init__(self):
        self.num = 0
        self.str = ""
        #self.sinFun = SinFun(None, "EX0")
        self.test = Test2(self)
        self.list = [SinFun(None, "EX0"), SinFun(None, "EX1")]
        #self.test = Test2()
        #self.list = [Test2(), Test2()]
        #self.list2 = ["東京", TestC(), TestC()]
        #self.test2 = Test2()
        #self.testC = TestC()

    def Counter(self):
        self.num +=1



if __name__ == "__main__":

    jasonString = """{"test2": {"num": 200, "str": "def"}, "num": 100, "str": "abc"}"""

    '''
    fn = askopenfile(mode='r', filetypes=(("JSON files", "*.json"), ("PyExecutor configure data", '*.' + 'fbd')),defaultextension='json')
    jasonString = fn.read()
    '''
    '''
    fn = askopenfile(mode='r', filetypes=(("JSON files", "*.json"), ("PyExecutor configure data", '*.' + 'fbd')),defaultextension='json')
    if fn:
        f = open(fn.name, 'r', encoding='utf-8')
        jasonString = f.read()
    '''
    test = Test()
    # 初期状態
    #print(test.ToJson())
    #test.Serialize(jasonString)
    test.Counter()
    #シリアライズした後
    #print(test.ToJson())
    jasonString = test.ToJson()
    #dict = {}
    #dict = json.loads(jasonString)
    #jasonString = json.dumps(dict, ensure_ascii=False, indent=4)
    fn = asksaveasfile(mode='w', filetypes=(("JSON files", "*.json"), ("PyExecutor configure data", '*.' + 'fbd')),defaultextension='json')
    if fn:
        f = open(fn.name, 'w', encoding='utf-8')
        f.write(jasonString)
        f.close()
