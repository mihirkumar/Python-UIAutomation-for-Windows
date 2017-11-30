#!python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import uiautomation as automation

level = int(sys.argv[1])

def firefox():
    firefoxWindow = automation.WindowControl(searchDepth = 1, ClassName = 'MozillaWindowClass')
    print (firefoxWindow.getChildren())
    # for i in range(1,level):
    #     print ('\n')
    #     print ('-------Level ' + str(i) + ': -------')
    #
    #     print (firefoxWindow)

def desktop_root():
    root = automation.WindowControl(ClassName = 'MozillaWindowClass')
    for i in root.GetChildren():
        for j in i.GetChildren():
            for k in j.GetChildren():
                for l in k.GetChildren():
                    print(l)

desktop_root()
