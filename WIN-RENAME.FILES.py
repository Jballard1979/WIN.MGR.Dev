#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- **************************************************************************************************************:
#-- ************************************************* RENAME FILES ***********************************************:
#-- **************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                      :
#-- Date:     2024.1.05                                                                                           :
#-- Script:   WIN-RENAME.FILES.py                                                                                 :
#-- Dir:      \\JBALLARD-9520\C$\0_SVN\2_DEV\3_PYTHON.Src\1_USEFUL.Dev\WINDOWS.Src\FILES.FOLDERS.Src\             :
#-- Purpose:  A python script that renames all files within the specified directory.                              :
#-- Version:  1.0                                                                                                 :
#-- **************************************************************************************************************:
#-- **************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES         :
#-- ********************************************************:
import os
#--
DIRPath     = 'D:\0_REPO\1_JEB.PERSONAL\1_AUDIO.BOOKS\SCIENCE.RELIGION\CARL.SAGAN\DEBATES.&.PODCASTS'
NEWFileName = 'PYTHON-'
#--
#-- ITERATE THRU EACH FILE WITHIN DIR:
for filename in os.listdir(DIRPath):
    #-- VERIFY FILE IS A FILE:
    if os.path.isfile(os.path.join(DIRPath, filename)):
        #--
        #-- RETRIEVE FIRST 9 CHARS & FILE EXT:
        FILEExt = os.path.splitext(filename)[1]
        NEWName = NEWFileName + filename[9:] + FILEExt
        #--
        #-- EXECUTE RENAME:
        os.rename(os.path.join(DIRPath, filename), os.path.join(DIRPath, NEWName))
#--
print("EVENT - SUCCESSFULLY RENAMED ALL FILES:")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: