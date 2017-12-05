#!python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import uiautomation as automation
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# level = int(sys.argv[1])

def firefox():
    ancestor = False
    showAllName = False
    showMore = False
    depth = 0xFFFFFFFF
    wait_time_in_seconds = 5

    edgeWindow = automation.WindowControl(searchDepth = 1, ClassName = 'ApplicationFrameWindow')
    control = edgeWindow
    if automation.WaitForExist(edgeWindow, wait_time_in_seconds):
        automation.Logger.WriteLine("There is an Edge window open :D", automation.ConsoleColor.Green)
    else:
        automation.Logger.WriteLine("There is no Edge window open :(", automation.ConsoleColor.Red)

    if ancestor:
        # control = ControlFromCursor()
        control = edgeWindow
        if control:
            automation.EnumAndLogControlAncestors(control, showAllName, showMore)
        else:
            automation.Logger.Write('IUIAutomation return null element under cursor\n', ConsoleColor.Yellow)
    else:
        if not control:
            control = edgeWindow
            controlList = []
            while control:
                controlList.insert(0, control)
                control = control.GetParentControl()
            if len(controlList) == 1:
                control = controlList[0]
            else:
                control = controlList[1]
        automation.EnumAndLogControl(control, depth, showAllName, showMore)
    automation.Logger.Log('Ends\n')
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

firefox()
