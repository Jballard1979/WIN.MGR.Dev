#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************** RECORD WIN ACTIONS ********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBallard (JEB)                                                                                    :
#-- Date:     2024.9.10                                                                                         :
#-- Script:   SYS-REC.ACTIONS.py                                                                                :
#-- Purpose:  A Python script that captures the users ACTIONS & writes them to a log file.                      :
#-- Class:    python -m pip install pyautogui pygetwindow                                                       :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import pyautogui
import pygetwindow as gw
import time
#--
#-- FUNCTION -RECORD ACTION EVERY DURATION:
def REC_Acts(duration=30):
    #-- INITILIZES EMPTY LIST TO STORE ACTIONS:
    actions = []
    start_time = time.time()
    print("NOTE - RECORDING ACTIONS...")
    #--
    #-- LOOP UNTIL END OF DURATION INPUT:
    while time.time() - start_time < duration:
        x, y = pyautogui.position()
        actions.append((time.time() - start_time, x, y))
        time.sleep(0.1)
    #- RETURN LIST CONTAINING "TUPLES" OF RECORDED MOUSE ACTIONS:
    return actions
#--
#-- FUNCTION - WRITES RECORDED ACTIONS TO FILE:
def SAV_Acts(filename, actions):
    with open(filename, 'w') as f:
        for action in actions:
            f.write(f"{action[0]},{action[1]},{action[2]}\n")
#--
#-- MAIN FUNCTION:
if __name__ == "__main__":
    #--
    #-- PROMPT USER FOR SPECIFIED TIME DURATION:
    duration = int(input("ENTER RECORDING DURATION (SEC): "))
    actions  = REC_Acts(duration)
    #-- SAVE RECORDED ACTIONS TO FILE:
    SAV_Acts("SYS-REC.WIN.ACTIONS.jeb", actions)
    print("NOTE - RECORDED ACTIONS SAVED TO .\SYS-REC.WIN.ACTIONS.jeb")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
