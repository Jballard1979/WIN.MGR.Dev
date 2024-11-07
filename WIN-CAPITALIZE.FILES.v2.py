#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- **************************************************************************************************************:
#-- ************************************************ CAP FILE NAMES **********************************************:
#-- **************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                      :
#-- Date:     2024.1.05                                                                                           :
#-- Script:   WIN-CAPITALIZE.FILES.v2.py                                                                          :
#-- Dir:      \\JBALLARD-9520\C$\0_SVN\2_DEV\3_PYTHON.Src\1_USEFUL.Dev\WINDOWS.Src\FILES.FOLDERS.Src\             :
#-- Purpose:  A python script that recursively capitalizes all files names & removes spaces.                      :
#-- Version:  1.0                                                                                                 :
#-- **************************************************************************************************************:
#-- **************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
import os
import re
#--
#-- WORKING DIR:
DIRPath = r'D:\0_REPO\1_JEB.PERSONAL\1_AUDIO.BOOKS\SCIENCE.RELIGION\ALEX.OCONNER\DEBATES.&.PODCASTS'
#--
#-- INSERT PERIOD (.) AFTER EVERY WORD:
def INSERTPeriod(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '.', name).replace('..', '')
#--
#-- RECURSIVELY PROCESS FILES WITH DIR:
def PROCFiles(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            try:
                FILEPath = os.path.join(root, file_name)
                if os.path.isfile(FILEPath):
                    BASEName, FILEExt = os.path.splitext(file_name)
                    FILEExt = FILEExt.lower()
                    NEWBASEName = INSERTPeriod(BASEName.upper().replace(' ', ''))
                    NEWName = NEWBASEName + FILEExt
                    NEWPath = os.path.join(root, NEWName)
                    os.rename(FILEPath, NEWPath)
                    print(f"EVENT - RENAMED: {FILEPath} -> {NEWPath}")
            except Exception as e:
                print(f"ERROR - FAILED TO PROCESSING {FILEPath}: {e}")
#--
if __name__ == "__main__":
    PROCFiles(DIRPath)
    print("EVENT - SUCCESSFULLY RENAMED ALL FILES")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: