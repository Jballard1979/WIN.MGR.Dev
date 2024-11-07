#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************* WINDOWS FILE SEARCH ********************************************:
#-- ************************************************************************************************************:
#-- Author:  JBallard (JEB)                                                                                     :
#-- Date:    2023.9.14                                                                                          :
#-- Script:  WIN-SRCH.TXT.v2.py                                                                                 :
#-- Purpose: A Python Script that searches for specific strings within files located in all subdirectories.     :
#-- Class:   python -m pip install -U argparse                                                                  :
#-- Class:   python -m pip install -U pathlib                                                                   :
#-- Class:   python -m pip install -U Path                                                                      :
#-- Usage:   SCADA                                                                                              :
#-- Usage:   *.*                                                                                                :
#-- Usage:   C:\0_SVN                                                                                           :
#-- Version: 2.0                                                                                                :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import os
import argparse
from pathlib import Path
#--
LOGPath = "WIN-SRCH.TXT.v2.jeb"
#--
#-- FUNCTION - SEARCH FOR TEXT WITHIN FILES:
def SRCH_TXT_IN_File(FILEPath, SRCHText):
    try:
        with open(FILEPath, 'r', encoding='utf-8') as file:
            FILEContent = file.read()
            if SRCHText in FILEContent:
                return True
    except Exception as e:
        pass
    return False
#--
#-- ARG PARSER DESCRIPTION:
ARGParser = argparse.ArgumentParser(description=" SEARCH FOR FILE(s):")
#-- ADD FILE(s) ARG:
ARGParser.add_argument("--FILEName", nargs="?", help="FILE NAME (WILDCARDS FUNCTIONS ENABLED):", default=None)
#-- ADD DIR(s) ARG:
ARGParser.add_argument("--FLDir", help="FOLDER (DEFAULT: CURRENT)", default=None)
#-- TEXT STRING WITHIN FILE ARG:
ARGParser.add_argument("--FILEText", help="SEARCH FOR TEXT STRING WITHIN FILE(s):", default=None)
#-- FILE & FOLDER ARG:
ARG = ARGParser.parse_args()
#--
#-- VALIDATE TEXT STRING:
if ARG.FILEText is None:
    while True:
        SRCHText = input("USER - ENTER DESIRED SEARCH STRING:")
        if SRCHText.strip() == "":
            print("ERROR - THE TEXT STRING WAS INVALID:")
            continue
        else:
            ARG.FILEText = SRCHText
            break
#--
#- VALIDATE FILE NAME(s):
if ARG.FILEName is None:
    while True:
        ARG.FILEName = input("USER - ENTER FILE NAME (WILDCARDS ENABLED):")
        if ARG.FILEName == "":
            print("ERROR - FILE NAME INVALID:")
            continue
        break
#--
#-- PROCESS FOLDER PATH(s):
if ARG.FLDir:
    FLDir = ARG.FLDir
else:
    FLDAnswer = input("USER - ENTER DESIRED SEARCH PATH:")
    if FLDAnswer:
        FLDir = FLDAnswer
    else:
        FLDir = "."
#--
#-- OPEN LOG FILE FOR WRITING:
with open(LOGPath, 'w', encoding='utf-8') as LOGFile:
    #-- WRITE COMPLETE PATH & FILE NAME(s) TO LOG FILE:
    for path in Path(FLDir).rglob(ARG.FILEName):
        if ARG.FILEText:
            if SRCH_TXT_IN_File(path, ARG.FILEText):
                LOGFile.write(f"{path.absolute()}\n")
        else:
            LOGFile.write(f"{path.absolute()}\n")
#--
print(f"NOTE - SEARCH RESULTS LOGGED TO - {LOGPath}:")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: