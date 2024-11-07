#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- *************************************************************************************************************:
#-- ********************************************** PURGE DIRECTORY **********************************************:
#-- *************************************************************************************************************:
#-- Author:  JBallard (JEB)                                                                                      :
#-- Date:    2017.3.11                                                                                           :
#-- Script:  WIN-PURGE.DIRS.py                                                                                   :
#-- Purpose: A python script that purges all files & folders in specified directory.                             :
#-- Class:   python -m pip install win32con                                                                      :
#-- Class:   python -m pip install win32api                                                                      :
#-- Ver:     1.0                                                                                                 :
#-- *************************************************************************************************************:
#-- *************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import os
import win32con
import win32api
#-
def del_dir(self,path):
	for file in os.listdir(path):
		file_or_dir = os.path.join(path,file)
		if os.path.isdir(file_or_dir) and not os.path.islink(file_or_dir):
			del_dir(file_or_dir)
		else:
			try:
				os.remove(file_or_dir)
			except:
				win32api.SetFileAttributes(file_or_dir, win32con.FILE_ATTRIBUTE_NORMAL)
				os.remove(file_or_dir)
		os.rmdir(path)
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
