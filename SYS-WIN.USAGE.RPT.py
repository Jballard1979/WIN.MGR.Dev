#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ***************************************** RETRIEVE DAILY WIN USAGE *****************************************:
#-- ************************************************************************************************************:
#-- Author:   JBallard (JEB)                                                                                    :
#-- Date:     2023.9.14                                                                                         :
#-- Script:   SYS-WIN.USAGE.RPT.py                                                                              :
#-- Purpose:  A Python script that retrieves the daily usage of your WIN system.                                :
#-- Class:    python -m pip install time                                                                        :
#-- Class:    python -m pip install datetime                                                                    :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import time
from datetime import datetime
#--
#-- FUNCTION - RETRIEVE DAILY WIN USAGE:
def WINUSAGERpt():
    #--
    #-- LOG USAGE EVERY MIN:
    with open('SYS-WIN.USAGE.RPT.jeb', 'a') as log:
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"Computer started at {start_time}\n")
        try:
            while True:
                time.sleep(60)
        except KeyboardInterrupt:
            end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"Computer shutdown at {end_time}\n")
#--
WINUSAGERpt()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
