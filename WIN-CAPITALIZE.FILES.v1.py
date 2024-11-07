#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- **************************************************************************************************************:
#-- ************************************************ CAP FILE NAMES **********************************************:
#-- **************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                      :
#-- Date:     2024.1.05                                                                                           :
#-- Script:   WIN-CAPITALIZE.FILES.v1.py                                                                          :
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
#--
#-- WORKING DIR:
DIRPath = r'D:\0_REPO\1_JEB.PERSONAL\1_AUDIO.BOOKS\SCIENCE.RELIGION\1_DOCUMENTARY'
#--
#-- ITERATE THRU EACH FILE WITHIN DIR:
for root, _, files in os.walk(DIRPath):
    #--
    for FILEName in files:
        #-- RETRIEVE FULL PATH OF FILE:
        FILEPath = os.path.join(root, FILEName)
        #--
        #-- VERIFY OBJECT IS NOT A DIR:
        if os.path.isfile(FILEPath):
            #-- SPLIT FILE NAME & EXT:
            BASEName, extension = os.path.splitext(FILEName)
            #-- CONVERT EXT TO LC:
            extension = extension.lower()
            #-- CONVERT BASE TO UC, CONVERT SPACES, & ADD EXT:
            NEWName = BASEName.upper().replace(' ', '') + extension
            #-- EXECUTE RENAME PROCESS:
            os.rename(FILEPath, os.path.join(root, NEWName))
#--
print("EVENT - SUCCESSFULLY RENAMED ALL FILES:")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: