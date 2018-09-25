# from pywinauto.findwindows    import find_window
# from pywinauto.win32functions import *
# import time
#
# # time.sleep(3)
# # idid0 = GetForegroundWindow()
# # print(idid0)
# # time.sleep(3)
# # idid = GetForegroundWindow()
# # print(idid)
# time.sleep(3)
# idid = GetForegroundWindow()
# print(idid)
# # SetForegroundWindow(idid0)
# # ShowWindow(idid0)
# time.sleep(1)
# print(GetCaretPos(idid))
# time.sleep(1)
# print(GetCaretPos(idid))
# time.sleep(1)
# print(GetCaretPos(idid))
#
# from ctypes import *
# import win32gui
# import win32api
# import win32con
# # import time
# #
# # user32 = windll.user32
# # kernel32 = windll.kernel32
# #
# # class RECT(Structure):
# #  _fields_ = [
# #      ("left", c_ulong),
# #      ("top", c_ulong),
# #      ("right", c_ulong),
# #      ("bottom", c_ulong)
# #  ]
# #
# # class GUITHREADINFO(Structure):
# #  _fields_ = [
# #      ("cbSize", c_ulong),
# #      ("flags", c_ulong),
# #      ("hwndActive", c_ulong),
# #      ("hwndFocus", c_ulong),
# #      ("hwndCapture", c_ulong),
# #      ("hwndMenuOwner", c_ulong),
# #      ("hwndMoveSize", c_ulong),
# #      ("hwndCaret", c_ulong),
# #      ("rcCaret", RECT)
# #  ]
# #
# #
# #
# # def get_selected_text_from_front_window(): # As String
# #     ''' vb6 to python translation '''
# #
# #     gui = GetForegroundWindow()#GUITHREADINFO(cbSize=sizeof(GUITHREADINFO))
# #     txt=''
# #     ast_Clipboard_Obj=None
# #     Last_Clipboard_Temp = -1
# #
# #     print(gui)
# #
# #     user32.GetGUIThreadInfo(0, byref(gui))
# #
# #     txt = GetCaretWindowText(gui.hwndCaret, True)
# #
# #     '''
# #     if Txt = "" Then
# #         LastClipboardClip = ""
# #         Last_Clipboard_Obj = GetClipboard
# #         Last_Clipboard_Temp = LastClipboardFormat
# #         SendKeys "^(c)"
# #         GetClipboard
# #         Txt = LastClipboardClip
# #         if LastClipboardClip <> "" Then Txt = LastClipboardClip
# #         RestoreClipboard Last_Clipboard_Obj, Last_Clipboard_Temp
# #         print "clbrd: " + Txt
# #     End If
# #     '''
# #     return txt
# #
# #
# #
# # def GetCaretWindowText(hWndCaret, Selected = False): # As String
# #
# #     startpos =0
# #     endpos =0
# #
# #     txt = ""
# #
# #     if hWndCaret:
# #
# #         buf_size = 1 + win32gui.SendMessage(hWndCaret, win32con.WM_GETTEXTLENGTH, 0, 0)
# #         if buf_size:
# #             buffer = win32gui.PyMakeBuffer(buf_size)
# #             win32gui.SendMessage(hWndCaret, win32con.WM_GETTEXT, buf_size, buffer)
# #             txt = buffer[:buf_size]
# #
# #         if Selected and buf_size:
# #             selinfo  = win32gui.SendMessage(hWndCaret, win32con.EM_GETSEL, 0, 0)
# #             endpos   = win32api.HIWORD(selinfo)
# #             startpos = win32api.LOWORD(selinfo)
# #             return txt[startpos: endpos]
# #
# #     return txt
# #
# # if __name__ == '__main__':
# #     time.sleep(5)
# #     print("run")
# #     print (get_selected_text_from_front_window())

#
# import win32con
# import ctypes
# import ctypes.wintypes
#
# FindWindow = ctypes.windll.user32.FindWindowW
# SendMessage = ctypes.windll.user32.SendMessageW
#
# class COPYDATASTRUCT(ctypes.Structure):
#     _fields_ = [
#         ('dwData', ctypes.wintypes.LPARAM),
#         ('cbData', ctypes.wintypes.DWORD),
#         ('lpData', ctypes.c_wchar_p)
#         #formally lpData is c_void_p, but we do it this way for convenience
#     ]
#
# hwnd = FindWindow('Home - Internet Explorer', None)
# cds = COPYDATASTRUCT()
# cds.dwData = 0
# str = 'boo'
# cds.cbData = ctypes.sizeof(ctypes.create_unicode_buffer(str))
# cds.lpData = ctypes.c_wchar_p(str)
#
# SendMessage(hwnd, win32con.WM_COPYDATA, 0, ctypes.byref(cds))


#
# from pywinauto.win32functions import *
# import win32con
# import win32gui
# import time
# time.sleep(5)
# hwnd = win32gui.GetForegroundWindow()
# print(hwnd)
# print(win32gui.GetClassName(hwnd))
# print(win32gui.GetWindowText(hwnd))
# print(GetCaretPos(hwnd))
# print(win32gui.SendMessage(hwnd, win32con.WM_COPY,None,None))
#
# time.sleep(2)
#
# import struct
# import array
# char_buffer = array.array('B', b'api do new sticky hello, world')
# char_buffer_address, char_buffer_size = char_buffer.buffer_info()
# copy_struct = struct.pack("PLP", 12345, char_buffer_size, char_buffer_address)
# # hwnd = win32gui.FindWindow(None, "ZhornSoftwareStickiesMain")
# win32gui.SendMessage(hwnd, win32con.WM_COPYDATA, None, copy_struct)




import win32clipboard as cb
import time
# while (1):
#     time.sleep(0.01)
#     cb.OpenClipboard()
#     cb_now = cb.GetClipboardData()
#     cb.CloseClipboard()
#     print(cb_now)
#
#
#

print(time.localtime(time.time()))
print(time.time())
time.sleep(3)
print(time.time())