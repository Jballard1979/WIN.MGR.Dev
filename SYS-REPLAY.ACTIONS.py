#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************** REPLAY WIN ACTIONS ********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBallard (JEB)                                                                                    :
#-- Date:     2024.9.10                                                                                         :
#-- Script:   SYS-REPLAY.ACTIONS.py                                                                             :
#-- Purpose:  A Python script that loads the Recorded Actions output file & replays it.                         :
#-- Class:    python -m pip install pyautogui time                                                              :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import pyautogui
import time
#--
#-- FUNCTION - LOAD USERS ACTIONS FROM FILE:
def LOAD_Acts(filename):
    actions = []
    with open(filename, 'r') as f:
        for line in f:
            t, x, y = line.strip().split(',')
            actions.append((float(t), int(x), int(y)))
    return actions

#-- FUNCTION - REPLAY ACTIONS:
def REPLAY_Acts(actions):
    start_time = time.time()
    for action in actions:
        while time.time() - start_time < action[0]:
            time.sleep(0.01)
            pyautogui.moveTo(action[1], action[2])
#--
#-- MAIN FUNCTION:
if __name__ == "__main__":
    actions = LOAD_Acts("SYS-REC.WIN.ACTIONS.jeb")
    print("REPLAYING ACTIONS...")
    REPLAY_Acts(actions)
    print("NOTE - SUCCESSFULLY REPLAYED ACTIONS:")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
