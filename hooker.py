
# for pywinauto
from pywinauto.win32_hooks import *
import time
import threading

class Hooker():
    def __init__(self, print_en=True):
        self.print_en = print_en
        self.search_en = False
        self.copy_en = False
        self.copy_time = time.time()
        self.tk_en = False
        self.add_en = False
        self.opendict_en = False
        self.closetk_en = False
        self.hook_en = False
        self.action_en = False
        self.secs = 0.3

        self.hk = Hook()
        self.hk.handler = self.on_event

        self.action_dict = {}

    def set_actions(self, ad):
        self.print("set_actions")
        self.action_dict = ad
        # print(self.action_dict)

    def print(self, txt):
        if self.print_en:
            print(txt)
    def on_event(self, args):
        """Callback for keyboard and mouse events"""
        if isinstance(args, KeyboardEvent):
            self.print([args.current_key, args.pressed_key])
            args = self.remove_duplicated(args)
            self.print([args.current_key, args.pressed_key])
            self.checkSearch(args)
            self.checkRunTK(args)
            # self.checkSearch2(args)

            if args.pressed_key and self.action_en:
                self.print("HK: run action!")
                self.action_en = False
                time.sleep(self.secs)
                self.run_action()

    def _hook(self):
        self.hook_en = True
        self.print("now hooking...")
        self.hk.hook(keyboard=True, mouse=False)

    def hook(self):
        t = threading.Thread(target=self._hook)
        t.start()
        self.print("Hooker Thread is started")

    def check_stop(self):
        if self.hook_en:
            self.stop()


    def stop(self):
        self.print("stop hooking...")
        self.hk.stop()
        self.hook_en = False

    def remove_duplicated(self, args):
        if args.event_type == 'key up' and args.current_key in args.pressed_key:
            while args.current_key in args.pressed_key:
                args.pressed_key.remove(args.current_key)
        return args

    # def checkSearch2(self, args):
    #     checkwd = 'Z'
    #     if args.current_key == checkwd and args.event_type == 'key down' and \
    #             'Lwin' in args.pressed_key:
    #             # 'Lcontrol' in args.pressed_key and \
    #             # 'Lshift' in args.pressed_key and \
    #             # 'Lmenu' in args.pressed_key and \
    #         self.action_en = True
    #         self.run_action = self.action_dict["searchword2"]
    #         print("search_en")

    def checkSearch(self, args):
        chkcp = 'C'
        checkwd = 'V'
        tmargin = 1
        if args.current_key == chkcp and args.event_type == 'key down' and \
                'Lcontrol' in args.pressed_key:
            self.copy_en = True
            self.copy_time = time.time()
            self.print("copy_en")
        if self.copy_en:
            tnow = time.time()
            if tnow-self.copy_time > tmargin:
                self.copy_en = False
                self.print("copy_dis")
            if args.current_key == checkwd and args.event_type == 'key down' and \
                    'Lcontrol' in args.pressed_key:
                self.action_en = True
                self.run_action = self.action_dict["searchword"]
                self.print("search_en")
                self.copy_en = False

    def checkRunTK(self, args):
        checkwd = 'O'
        if args.current_key == checkwd and args.event_type == 'key down' and \
                'Lwin' in args.pressed_key:
            self.action_en = True
            self.run_action = self.action_dict["runTK"]
            self.print("tk_en")


# self.hk_dict = {"runTK": self.runTK,
#                 "searchword": self.searchHK,
#                 "adddict": self.adddict,
#                 "opendict": self.opendict,
#                 "closeTK": self.closeTK
#                 }