#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- **************************************************************************************************************:
#-- ************************************************* RENAME FILES ***********************************************:
#-- **************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                      :
#-- Date:     2024.1.05                                                                                           :
#-- Script:   WIN-RENAME.FILES.v2.py                                                                              :
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
FILEExt = [".txt", "jeb", ".pdf", ".docx", ".doc"]
#--
#-- FUNCTION - RENAME FILES IN DIR:
def rename_files(directory):
    for filename in os.listdir(directory):
        #-- FILTER FILES USING BELOW REQUIREMENTS:
        if (filename.startswith("MATHEMATICS-") and
            any(extension in filename for extension in FILEExt)):
            #-- REPLACE FILES USING BELOW REQUIREMENTS:
            NEWFName    = "MATH-" + filename[12:]
            FILESDir    = os.path.join(directory, filename)
            NEWFILESDir = os.path.join(directory, NEWFName)
            #-- RENAME FILES:
            os.rename(FILESDir, NEWFILESDir)
            print(f"NOTE - RENAMED {FILESDir} TO {NEWFILESDir}:")
#--
#-- DIRECTORY:
rename_files("//JBALLARD-9520/C$/0_SVN/1_DOCS/SELF.DEVELOPMENT.Doc/MATHEMATICS")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: