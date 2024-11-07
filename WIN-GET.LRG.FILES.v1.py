#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ****************************************** RETRIEVE LARGE FILES ********************************************:
#-- ************************************************************************************************************:
#-- Author:  JBallard (JEB)                                                                                     :
#-- Date:    2024.8.15                                                                                          :
#-- Script:  WIN-GET.LRG.FILES.v1.py                                                                            :
#-- Purpose: A Python Script that retrieves the largest files within a chosen subdirectory (recursively).       :
#-- Class:   python -m pip install glob                                                                         :
#-- Class:   python -m pip install argparse                                                                     :
#-- Version: 1.0                                                                                                :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import os
import sys
import glob
import argparse
#--
#-- DEFINE SEARCH PATH:
SRCHDir = os.path.join("//JBALLARD-9520", "C$", "0_SVN", "2_DEV")
LOGFile = os.path.join("//JBALLARD-9520", "C$", "0_SVN", "7_LOGS", "WIN-GET.LRG.FILES.v1.jeb")
NFiles  = 5
#--
#-- FUNCTION - RETRIEVE LARGEST FILES WITHIN SUBDIRECTORY:
def RET_LARGE_Files(SRCHDir):
    FILESizes = []
    for dirpath, dirnames, filenames in os.walk(SRCHDir):
        for filename in filenames:
            FILEPath = os.path.join(dirpath, filename)
            FILESize = os.path.getsize(FILEPath)
            FILESizes.append((FILEPath, FILESize))
    #-- SORT FILES VIA DESC SIZE:
    FILESizes.sort(key=lambda x: x[1], reverse=True)
    #-- 
    #-- COPY "NFiles" LARGEST FILES TO THE DESTIANATION DIR::
    with open(LOGFile, "w") as log:
        for filepath, filesize in FILESizes[:NFiles]:
            log.write(f"{filepath}\t\t{filesize} BYTES\n")
#--
#-- MAIN:
if __name__ == "__main__":
    LRGFiles = RET_LARGE_Files(SRCHDir)
    #-- PRINT FILEPATH & SIZE:
    for FILEPath, FILESize in LRGFiles:
        print(FILEPath, FILESize)
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: