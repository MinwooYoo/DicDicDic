
#  이거 tkinter gui 로 쓰면됨.
import tkinter as tk
# from tkinter import *
from tkinter import ttk
from tkinter.tix import ScrolledWindow

class TkGUI():
    def __init__(self, ad, print_en = True):
        self.print_en = print_en
        self.isrunning = False
        self.isdestroyed = True
        self.action_dict = ad
        self.init()

    def init(self):
        self.isdestroyed = False
        self.root = tk.Tk()
        self.root.wm_title('Dictionary')

        w = 640  # width for the Tk root
        h = 480  # height for the Tk root

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # self.frame = tk.Frame(width="500",height="500")
        # self.frame.pack()
        # self.swin = ScrolledWindow(self.frame, width=500, height=500)
        # self.swin.pack()
        self.win = self.root

        # self.win = Tk()
        # print(self.win.winfo_exists())
        #
        # self.win.title("Dictionary")
        # self.win.geometry('500x500-0+20')
        self.strWord = tk.StringVar()
        self.strRes = tk.StringVar()
        self.strKey = tk.StringVar()

        textbox = ttk.Entry(self.win, font="Times 20 bold", width=20, textvariable=self.strWord)
        textbox.grid(column=0, row=0)

        # lbl = Label(win, text="단어장 열기")
        # lbl.grid(column=0, row=2)
        lbl = tk.Label(self.win, wraplength=300, textvariable=self.strRes, justify=tk.LEFT)
        lbl.grid(column=0, row=1)
        self.strRes.set("Open Notes")

        lbl = tk.Label(self.win, wraplength=300, textvariable=self.strKey, justify=tk.LEFT)
        lbl.grid(column=0, row=2)
        self.strKey.set("LCtrl+C->V: search blocked word, \nLWin+O: open this window")
        # self.strKey.set("Ctrl+Alt+Shift+Z: search blocked word, \nCtrl+Alt+Shift+I: open this window")
        self.win.bind('<Key>', self.hotkey_call)

        self.set_actions(self.action_dict)

    def print(self, txt):
        if self.print_en:
            print(txt)
    def check_init(self):
        self.print("TkGUI Check Init!")
        if self.isdestroyed:
            self.init()

    def get_forward(self):
        self.win.iconify()
        self.win.update()
        self.win.deiconify()

    def check_destroyed(self):
        if not self.isdestroyed:
            self.destroy()

    def set_actions(self, ad):
        self.action1 = ttk.Button(self.win, text="Search(F)", command=ad["searchword"])
        self.action1.grid(column=1, row=0)
        self.action2 = ttk.Button(self.win, text="Save(S)", command=ad["adddict"])
        self.action2.grid(column=1, row=1)
        self.action4 = ttk.Button(self.win, text="Minimize(Q)", command=ad["closeTK"])
        self.action4.grid(column=1, row=2)
        self.action3 = ttk.Button(self.win, text="Open Dict(D)", command=ad["opendict"])
        self.action3.grid(column=2, row=0)
        self.action5 = ttk.Button(self.win, text="Save & Minimize(W)", command=ad["saveandcloseTK"])
        self.action5.grid(column=2, row=1)
        self.action6 = ttk.Button(self.win, text="Exit(P)", command=ad["distroydict"])
        self.action6.grid(column=2, row=2)
        self.root.protocol('WM_DELETE_WINDOW', ad["distroydict"])

    def hotkey_call(self, event):
        # self.check_init()
        # use ctrl+'a-z'
        #  a 'a', alt + a = 'a', shift + a = 'a'
        #  ctrl+a '\x01'
        #  ctrl+b '\x02'
        #  ctrl+c '\x03'
        #  ctrl+z '\x1a'
        #  ctrl+i '\t'
        #  ctrl+j '\n'
        #  ctrl+m '\r'
        if event.char == '\x06':  # f
            self.action_dict["searchword"]()
        if event.char == '\x13':  # s
            self.action_dict["adddict"]()
        if event.char == '\x04':  # d
            self.action_dict["opendict"]()
        if event.char == '\x11':  # q
            self.action_dict["closeTK"]()
        if event.char == '\x17':  # w
            self.action_dict["saveandcloseTK"]()
        if event.char == '\x10':  # p
            self.action_dict["distroydict"]()

    def run(self):
        self.check_init()
        if self.isdestroyed:
            self.print("tkinter is not running...")
            self.print("run tkinter...")
            # self.isrunning = True
            self.isdestroyed = False
            self.win.mainloop()
            # self.win.winfo_exists()
        else:
            self.print("tkinter is running...")
            self.get_forward()

    def stop(self):
        self.check_init()
        if self.isdestroyed:
            self.print("tkinter is destroyed")
        else:
            self.print("quit tkinter...")
            self.win.iconify()
            # self.isrunning = False

    def destroy(self):
        self.check_init()
        if self.isdestroyed:
            self.print("tkinter is already destroyed")
        else:
            self.print("destroy tkinter...")
            self.stop()
            self.win.destroy()
            self.isdestroyed = True