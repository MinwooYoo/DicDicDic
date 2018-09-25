# import ctypes
# from ctypes import wintypes
#
# kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
# kernel32.FreeLibrary.argtypes = [wintypes.HMODULE]

import json
import os

import win32clipboard as cb
# from pywinauto import keyboard as kb

from src.dictTK import TkGUI
from src.hooker import Hooker
from src.websearch import WebSearch
# for word_list_check ,,word_exist





class DictBot():
    def __init__(self, print_en=False):
        self.print_en = print_en
        self.filepath = 'dic.txt'
        # self.filepath = os.getcwd() + '\\' + self.filepath
        # if not os.path.isfile(self.filepath):
        #     open(self.filepath, 'a').close()
        self.wordnow = ""
        self.resnow = ""
        self.dictkv = {}
        self.loaddict()
        self.myWeb = WebSearch(print_en = print_en)
        self.myHK = Hooker(print_en = print_en)

        # [self.searchword, self.adddict, self.opendict, self.closeTK]
        self.action_dict = {"searchword": self.searchTK,
                            "adddict": self.adddict,
                            "opendict": self.opendict,
                            "closeTK": self.closeTK,
                            "saveandcloseTK": self.saveandcloseTK,
                            "distroydict": self.destroyDict
                            }

        self.myTK = TkGUI(self.action_dict, print_en = print_en)

        self.hk_dict = {"runTK": self.runTK,
                        "searchword": self.searchHK,
                        # "searchword2": self.searchHK2,
                        # "adddict": self.adddict,
                        # "opendict": self.opendict,
                        # "closeTK": self.closeTK,
                        # "destroydict": self.destroyDict
                        }
        self.myHK.set_actions(self.hk_dict)

    def print(self, txt):
        if self.print_en:
            print(txt)
    def check_TK(self):
        self.myTK.check_init()
        self.myTK.get_forward()

    # search words using bs4
    def searchTK(self):
        self.check_TK()
        self.wordnow = self.myTK.strWord.get()
        self.resnow = self.myWeb.search(self.wordnow)
        self.myTK.strRes.set(self.resnow)

    def searchHK(self):
        self.print("searchHK")
        # kb.SendKeys('^c')
        cb.OpenClipboard()
        cb_now = cb.GetClipboardData()
        cb.CloseClipboard()
        self.print(cb_now)
        self.wordnow = cb_now
        self.resnow = self.myWeb.search(self.wordnow)
        self.check_TK()
        self.myTK.strWord.set(self.wordnow)
        self.myTK.strRes.set(self.resnow)
        self.runTK()

    # def searchHK2(self):
    #     self.check_TK()
    #     self.print("searchHK")
    #     kb.SendKeys('^c')
    #     cb.OpenClipboard()
    #     cb_now = cb.GetClipboardData()
    #     cb.CloseClipboard()
    #     self.print(cb_now)
    #     self.wordnow = cb_now
    #     self.resnow = self.myWeb.search(self.wordnow)
    #     self.myTK.strWord.set(self.wordnow)
    #     self.myTK.strRes.set(self.resnow)
    #     self.runTK()

    def adddict(self):
        self.print("add dict")
        if self.checkword(self.wordnow):
            self.dictkv[self.wordnow] = self.resnow
        self.savedict()

    def savedict(self):
        # jsonStr = json.dumps(self.dictkv)
        # df = open('data.txt', 'w')
        # df.write(jsonStr)
        # df.close
        with open(self.filepath, 'w', encoding='UTF8') as df:
            json.dump(self.dictkv, df, ensure_ascii=False)

    def loaddict(self):
        # jsonStr = json.dumps(self.dictkv)
        # df = open('data.txt', 'w')
        # df.write(jsonStr)
        # df.close
        # self.print(self.filepath)
        if not os.path.isfile(self.filepath):
            self.print("make new dictionary file!!")
            with open(self.filepath, 'w', encoding='UTF8') as df:
                json.dump({}, df, ensure_ascii=False)
        with open(self.filepath, encoding='UTF8') as df:
            self.dictkv = json.load(df)

    # true if not contained
    def checkword(self, word):
        keys = self.dictkv.keys()
        if word not in keys and word is not "":
            return True
        else:
            return False

    # 이 함수가 불려지면 단어장을 열어서 윈도우창에 보여주도록 하자.
    def opendict(self):
        self.print("Open notedpad!")
        os.startfile(self.filepath)

    def closeTK(self):
        self.print("stop gui")
        self.myTK.stop()

    def runTK(self):
        self.print("run gui")
        self.myTK.run()

    def saveandcloseTK(self):
        self.adddict()
        self.print("stop gui")
        self.myTK.stop()

    def destroyTK(self):
        # self.adddict()
        self.print("stop gui")
        self.myTK.destroy()

    def runHK(self):
        self.print("run hook")
        self.myHK.hook()

    def stopHK(self):
        self.print("stop hook")
        self.myHK.stop()

    def runDict(self):
        self.print("run Dict")
        self.runHK()
        self.runTK()

    def destroyDict(self):
        self.print("stop dict all")
        self.destroyTK()
        self.stopHK()

    def check_end(self):
        self.myTK.check_destroyed()
        self.myHK.check_stop()

    def run(self):
        self.runDict()
        self.check_end()

if __name__ == "__main__":
    mydict = DictBot()
    mydict.run()
    print("prgm end")