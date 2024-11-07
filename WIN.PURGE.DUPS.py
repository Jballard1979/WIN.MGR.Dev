#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- *************************************************************************************************************:
#-- ******************************************* SEARCH DUPLICATE FILES ******************************************:
#-- *************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                     :
#-- Date:     2023.3.07                                                                                          :
#-- Script:   WIN-PURGE.DUPS.py                                                                                  :
#-- Purpose:  A python script that scans a SCANDir & moves all the duplicate files.                              :
#-- Class:    python -m pip install hashlib                                                                      :
#-- Class:    python -m pip install shutil                                                                       :
#-- Version:  1.0                                                                                                :
#-- *************************************************************************************************************:
#-- *************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import os
import hashlib
import shutil
#--
#-- DEFINE SCAN & BACKUP DIRECTORIES:
SCANDir = "E:\FILE.MGT.Src\DUPS"
BAKDir  = "E:\FILE.MGT.Src\DUPBACKUP"
#--
#-- GENERATE A NEW SCANDir FOR STORING DUPLICATE FILES:
hashes = {}
#--
#-- LOOP THROUGH ALL FILES IN SUB-SCANDir:
for filename in os.listdir(SCANDir):
    #--
    #-- RETRIEVE FULL PATH TO FILE:
    FPath = os.path.join(SCANDir, filename)
    if os.path.isfile(FPath):
        #--
        #-- CALCULATE MD5 HASH OF THE FILES CONTENT:
        with open(FPath, "rb") as f:
            FHash = hashlib.md5(f.read()).hexdigest()
            #--
            #-- CHECK DICTIONARY FOR FILE HASH:
            if FHash in hashes:
                #--
                #--  MOVE FILE TO BACKUP SCANDir:
                print(f"Moving {FPath} to {BAKDir}")
                shutil.move(FPath, BAKDir)
            else:
                #-- ADD ENTRY INTO DICTIONARY:
                hashes[FHash] = FPath
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: