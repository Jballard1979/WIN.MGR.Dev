#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- *************************************************************************************************************:
#-- ********************************************* MON WIN EVENT LOGS ********************************************:
#-- *************************************************************************************************************:
#-- Author:  JBallard (JEB)                                                                                      :
#-- Date:    2024.1.02                                                                                           :
#-- Script:  SYS-WIN.RETURN.EVNT.LOGS.py                                                                         :
#-- Purpose: A python script that analyzes Widnows Event Logs & returns suspicious activity.                     :
#-- Class:   python -m pip install win32evtlog                                                                   :
#-- Ver:     1.0                                                                                                 :
#-- *************************************************************************************************************:
#-- *************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import win32evtlog
#--
#-- FUNCTION - ANALYZE WIN EVENT LOGS:
def read_event_log(log_type='Security'):
    #--
    server = 'localhost'
    handle = win32evtlog.OpenEventLog(server, log_type)
    total  = win32evtlog.GetNumberOfEventLogRecords(handle)
    #--
    flags  = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(handle, flags, 0)
    #--
    for event in events:
        print(f"NOTE - EVENT ID: {event.EventID}, SOURCE: {event.SourceName}:")
#--
read_event_log()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: