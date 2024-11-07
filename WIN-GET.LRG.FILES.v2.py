#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ****************************************** RETRIEVE LARGE FILES ********************************************:
#-- ************************************************************************************************************:
#-- Author:  JBallard (JEB)                                                                                     :
#-- Date:    2024.8.15                                                                                          :
#-- Script:  WIN-GET.LRG.FILES.v2.py                                                                            :
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
LOGFile = os.path.join("//JBALLARD-9520", "C$", "0_SVN", "7_LOGS", "WIN-GET.LRG.FILES.v2.jeb")
NFiles  = 5
#--
#-- FUNCTION - RETRIEVE LARGEST FILES WITHIN SUBDIRECTORY:
def main():
    #-- RETRIEVE SIZE-SORTED LIST OF ALL FILES WITHIN SOURCE DIRECTORY:
    FILESizes = sorted([(os.path.join(root, f), os.path.getsize(os.path.join(root, f))) for root, dirs, files in os.walk(SRCHDir) for f in files], key=lambda x: -x[1])
    #--
    #-- COPY "NFiles" LARGEST FILES TO THE DESTIANATION DIR::
    with open(LOGFile, "w") as log:
        for filepath, filesize in FILESizes[:NFiles]:
            log.write(f"{filepath}\t\t{filesize} BYTES\n")
#--
#-- MAIN:
if __name__ == '__main__':
    main()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: