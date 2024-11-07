#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************* GET WINDOWS VERSION ********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBallard (JEB)                                                                                    :
#-- Date:     2024.4.18                                                                                         :
#-- Script:   SYS-WIN.VERSION.py                                                                                :
#-- Purpose:  A Python script that retrieves the Windows version you're running.                                :
#-- Class:    python -m pip install wmi                                                                         :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import wmi
#--
#-- FUNCTION - RETRIEVE WIN VERSION:
def GETWINVer():
    try:
        data = wmi.WMI()
        for os_name in data.Win32_OperatingSystem():
            print(os_name.Caption)
    except Exception as e:
        print(f"ERROR - FAILED TO RETRIEVE WINDOWS VERSIONING: {e}")
#--
GETWINVer()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
