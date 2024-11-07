#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- *************************************************************************************************************:
#-- ********************************************* MON WIN FILE SYSTEM *******************************************:
#-- *************************************************************************************************************:
#-- Author:  JBallard (JEB)                                                                                      :
#-- Date:    2024.1.02                                                                                           :
#-- Script:  SYS-WIN.FS.WATCHDOG.v2.py                                                                           :
#-- Purpose: A python script that monitors the File System of a Windows System.                                  :
#-- Class:   python -m pip install watchdog                                                                      :
#-- Class:   python -m pip install watchdog.observers                                                            :
#-- Class:   python -m pip install Observer                                                                      :
#-- Class:   python -m pip install watchdog.events                                                               :
#-- Class:   python -m pip install FileSystemEventHandler                                                        :
#-- Ver:     1.0                                                                                                 :
#-- *************************************************************************************************************:
#-- *************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import time
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers.polling import PollingObserver as Observer
#--
#-- CLASS - CHECK FOR MODS, CREATION, & DELETED FILES:
class MyHandler(FileSystemEventHandler):
    #--
    #-- FUNCTION - CHECK FILE MODIFICATIONS:
    def on_any_event(self, event: FileSystemEvent) -> None:
        print(event)
#--    
event_handler = FileSystemEventHandler()
observer      = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: