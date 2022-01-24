#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# python GUI wxpython
# 

import requests
import wx
# import win32api
import sys, os

'''
   
'''

#-*- coding: utf-8 -*-




APP_TITLE = '基本框架'
APP_ICON = './static/logo.icon' # 请更换成你的icon

class mainFrame(wx.Frame): # 当前类继承自wx.Frame，类中参数即是继承对象
    '''程序主窗口类，继承自wx.Frame'''
    
    def __init__(self):
        '''构造函数'''
        wx.Frame.__init__(self, None, -1, APP_TITLE, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        # 默认style是下列项的组合：wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN 
        
        self.SetBackgroundColour(wx.Colour(224, 224, 224))# 背景色
        self.SetSize((800, 600))# 窗口大小
        self.Center()# 居中显示
        
        # # 以下代码处理图标
        # if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
        #     exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
        #     icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        # else :
        #     icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        # self.SetIcon(icon)
        
        # 以下可以添加各类控件
        pass
        
class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame()
        self.Frame.Show()
        return True

if __name__ == "__main__":
    # 将调试信息定位到了debug.txt文件。如果mainApp()不使用任何参数，则调试信息输出到控制台
    app = mainApp(redirect=True, filename="debug.txt")
    app.MainLoop()

