#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- *************************************************************************************************************:
#-- ********************************************* MON WIN FILE SYSTEM *******************************************:
#-- *************************************************************************************************************:
#-- Author:  JBallard (JEB)                                                                                      :
#-- Date:    2024.1.02                                                                                           :
#-- Script:  SYS-WIN.FS.WATCHDOG.py                                                                              :
#-- Purpose: A python script that monitors the File System of a Windows System.                                  :
#-- Class:   python -m pip install watchdog                                                                      :
#-- Class:   python -m pip install watchdog.observers                                                            :
#-- Class:   python -m pip install Observer                                                                      :
#-- Class:   python -m pip install watchdog.events                                                               :
#-- Class:   python -m pip install FileSystemEvent                                                               :
#-- Class:   python -m pip install FileSystemEventHandler                                                        :
#-- Ver:     1.0                                                                                                 :
#-- *************************************************************************************************************:
#-- *************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers.polling import PollingObserver as Observer
#--
#-- CLASS - CHECK FOR MODS, CREATION, & DELETED FILES:
class MyHandler(FileSystemEventHandler):
    #--
    #-- FUNCTION - CHECK FILE MODIFICATIONS:
    def on_modified(self, event):
        print(f'NOTE - FILE {event.src_path} HAS BEEN MODIFIED:')
    #--    
    #-- FUNCTION - CHECK FOR FILE CREATION:
    def on_created(self, event):
        print(f'NOTE - FILE {event.src_path} HAS BEEN CREATED:')
    #--
    #-- FUNCTION - CHECK FOR FILE DELETION:
    def on_deleted(self, event):
        print(f'NOTE - FILE {event.src_path} HAS BEEN DELETED:')
#--
observer = Observer()
observer.schedule(MyHandler(), path='C:/Windows/System32', recursive=True)
observer.start()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: