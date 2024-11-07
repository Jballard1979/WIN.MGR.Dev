#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************* MONITOR SYS RESOURCES ******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBallard (JEB)                                                                                    :
#-- Date:     2023.9.14                                                                                         :
#-- Script:   SYS-MON.RESOURCES.py                                                                              :
#-- Purpose:  A Python script that SYSMons a systems Disk, Memory, & CPU status.                                :
#-- Class:    python -m pip install psutil                                                                      :
#-- Class:    python -m pip install time                                                                        :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import psutil
import time
#--
#-- FUNCTION - RETRIEVE DISK USAGE:
def GETDSKUsage():
    DISKUsage = psutil.disk_usage('/')
    return {
        'TOTAL': DISKUsage.total,
        'USED': DISKUsage.used,
        'FREE': DISKUsage.free,
        'PERCENT': DISKUsage.percent
    }
#--
#-- FUNCTION - RETRIEVE MEMORY USAGE:
def GETMEMUsage():
    MEMInfo = psutil.virtual_memory()
    return {
        'TOTAL': MEMInfo.total,
        'AVAILABLE': MEMInfo.available,
        'USED': MEMInfo.used,
        'PERCENT': MEMInfo.percent
    }
#--
#-- FUNCTION - RETRIEVE CPU USAGE:
def GETCPUUsage():
    return psutil.cpu_percent(interval=1)
#--
#-- FUNCTION - DISPLAY USAGE:
def GETDISPUsage():
    DISKUsage = GETDSKUsage()
    MEMUsage  = GETMEMUsage()
    CPUUsage  = GETCPUUsage()
    #--
    #-- PRINT DISK USAGE:
    print(f"DISK USAGE: {DISKUsage['PERCENT']}%")
    print(f"    TOTAL: {DISKUsage['TOTAL'] / (1024 ** 3):.2f} GB")
    print(f"    Used: {DISKUsage['USED'] / (1024 ** 3):.2f} GB")
    print(f"    Free: {DISKUsage['FREE'] / (1024 ** 3):.2f} GB\n")
    #-- PRINT MEMORY:
    print(f"MEMORY USAGE: {MEMUsage['PERCENT']}%")
    print(f"    TOTAL: {MEMUsage['TOTAL'] / (1024 ** 3):.2f} GB")
    print(f"    USED: {MEMUsage['USED'] / (1024 ** 3):.2f} GB")
    print(f"    AVAILABLE: {MEMUsage['AVAILABLE'] / (1024 ** 3):.2f} GB\n")
    #-- PRINT CPU:
    print(f"CPU Usage: {CPUUsage}%\n")
#--
#-- FUNCTION - SYSTEM SYSMonING INTERVAL:
def SYSMon(interval=5):
    try:
        while True:
            GETDISPUsage()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("NOTE - SYSTEM MONITORING HAS STOPPED:")

if __name__ == "__main__":
    SYSMon()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
