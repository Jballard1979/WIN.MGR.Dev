#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************* PYTHON ALERT REMINDER ******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBallard (JEB)                                                                                    :
#-- Date:     2023.9.14                                                                                         :
#-- Script:   SYS-ALERTS.REM.py                                                                                 :
#-- Purpose:  A Python alert reminder that allows the user to set reminders.                                    :
#-- Class:    python -m pip install time                                                                        :
#-- Class:    python -m pip install tkinter                                                                     :
#-- Class:    python -m pip install messagebox                                                                  :
#-- Class:    python -m pip install simpledialog                                                                :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import time
import tkinter as tk
from tkinter import messagebox, simpledialog
#--
#-- GLOBAL VAR TO HOLD SET ALARM REF:
ALMLSTBox = None
#--
#-- FUNCTION - UPDATE TIME:
def UPTime():
    CURTime = time.strftime("%H:%M:%S")
    TIMELbl.config(text=CURTime)
    CKAlarm(CURTime)
    root.after(1000, UPTime)
#--
#-- FUNCTION - VERIFY ALARM:
def CKAlarm(CURTime):
    if ALMSet and CURTime > ALMSet:
        messagebox.showwarning("ALARM", "REFOCUS YOUR EFFORTS ON ANOTHER PROJECT!")
        CLRAlarm()
#--
#-- FUNCTION - MAIN WINDOW:
def GENMAINWin():
    global ALMLSTBox
    window_width  = 680
    window_height = 380
    root.geometry(f'{window_width}x{window_height}')
    screen_width  = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x      = int(screen_width / 2 - window_width / 2)
    center_y      = int(screen_height / 2 - window_height / 2)
    root.geometry(f'+{center_x}+{center_y}')
    #--
    #-- CREATE A LISTBOX:
    ALMLSTBox = tk.Listbox(root, font=('Helvetica', 12), bg='WHITE', fg='BLACK')
    ALMLSTBox.pack(expand=True, fill='both')
#--
#-- FUNCTION - SET ALARM:
def SETAlarm():
    global ALMLSTBox
    ALMTime = simpledialog.askstring("SET ALERT", "ENTER TIME IN HH:MM FORMAT:")
    if ALMTime:
        try:
            time.strptime(ALMTime, "%H:%M")
            if ALMTime < time.strftime("%H:%M"):
                messagebox.showerror("ERROR", "ALERT TIME MUST BE SET IN THE FUTURE:")
                return
            global ALMSet
            ALMSet = ALMTime
            ALMLbl.config(text=f"ALARM: {ALMTime}")
            #-- PASS THE SET ALARM TIME TO THE LISTBOX OBJECT:
            ALMLSTBox.insert(tk.END, ALMTime)
        except ValueError as value:
            messagebox.showerror("ERROR", "PLEASE SET TIME IN HH:MM FORMAT:")
#--
#-- FUNCTION - GENERATE LABLE:
def GENLbls():
    _TIMELbl = tk.Label(root, font=('Helvetica', 50), bg='BLUE', fg='WHITE')
    _TIMELbl.pack(expand=True, fill='both')
    _ALM_LBL = tk.Label(root, font=('Helvetica', 25), bg='BLUE', fg='GREEN')
    return _TIMELbl, _ALM_LBL
#--
#-- FUNCTION - GENERATE OBJECT BUTTONS:
def GENBtns():
    button_frame     = tk.Frame(root)
    button_frame.pack(fill='x', expand=True)
    SETAlarm_button = tk.Button(button_frame, text="SET ALERT:", command=SETAlarm, font=('Helvetica', 18))
    SETAlarm_button.pack(side='left', padx=5, pady=20)
    CLRAlarm_button  = tk.Button(button_frame, text="CLEAR ALERT:", command=CLRAlarm, font=('Helvetica', 18))
    CLRAlarm_button.pack(side='right', padx=5, pady=20)
#--
#-- FUNCTION - CLEAR ALARM:
def CLRAlarm():
    global ALMSet
    ALMSet = None
    ALMLbl.config(text="")
    ALMLSTBox.delete(0, tk.END)
#--
#-- MAIN PROGRAM:
if __name__ == '__main__':
    #-- CREATE MAIN WINDOW:
    root = tk.Tk()
    root.title("ALERT REMINDER v1.0:")
    GENMAINWin()
    ALMSet = None
    TIMELbl, ALMLbl = GENLbls()
    GENBtns()
    UPTime()
    root.mainloop()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************:
