#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- *************************************************************************************************************:
#-- ********************************************* MON WIN FILE SYSTEM *******************************************:
#-- *************************************************************************************************************:
#-- Author:  JBallard (JEB)                                                                                      :
#-- Date:    2024.1.02                                                                                           :
#-- Script:  SYS.WIN.FS.MON.py                                                                                   :
#-- Purpose: A python script that monitors the File System of a Windows System.                                  :
#-- Class:   python -m pip install win32file                                                                     :
#-- Class:   python -m pip install win32security                                                                 :
#-- Class:   python -m pip install win32con                                                                      :
#-- Class:   python -m pip install time                                                                          :
#-- Ver:     1.0                                                                                                 :
#-- *************************************************************************************************************:
#-- *************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import win32file
import win32security
import win32con
import time
#--
def FILESYSMon(path):
    FILE_LIST_DIRECTORY = 0x0001
    BUFFER_SIZE = 1024
    FILE_NOTIFY_CHANGE_LAST_WRITE = 0x00000010
    #--
    hDir = win32file.CreateFile(
        path,
        FILE_LIST_DIRECTORY,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_FLAG_BACKUP_SEMANTICS,
        None
    )
    #--
    while True:
        try:
            results = win32file.ReadDirectoryChangesW(
                hDir,
                BUFFER_SIZE,
                True,
                win32con.FILE_NOTIFY_CHANGE_LAST_WRITE,
                None,
                None
            )
            #--
            for action, file_name in results:
                if action == win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES:
                    try:
                        user, _, _, _ = win32security.GetFileSecurity(path, win32security.OWNER_SECURITY_INFORMATION)
                        user_name, domain, _ = win32security.LookupAccountSid(None, user)
                        print(f"FILE '{file_name}' MODIFIED BY {user_name} FROM {domain}")
                    except Exception as e:
                        print(f"ERROR - FAILED TO RETRIEVE USER INFO: {e}")
        except Exception as e:
            print(f"ERROR - FAILED TO MONITOR WIN FILE SYSTEM: {e}")
        time.sleep(1)
    win32file.CloseHandle(hDir)
#--
#-- PATH TO MONITOR:
if __name__ == '__main__':
    MONPath = r'C:\0_SVN' 
    FILESYSMon(MONPath)
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: