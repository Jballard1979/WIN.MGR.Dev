#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ********************************************* DUPLICATE FILES **********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.1.05                                                                                         :
#-- Script:   WIN.DUP.FILES.py                                                                                  :
#-- Purpose:  A python script that retrieves duplicate files within directory.                                  :
#-- Class:    python -m pip install hashlib logging                                                             :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import os
import hashlib
import logging
#--
#-- CONFIGURE LOGGING:
logging.basicConfig(filename='WIN.DUP.FILES.jeb', level=logging.INFO, format='%(asctime)s: %(message)s')
#--
#-- SEARCH DIR:
DIRPaths = os.path.join("//JBALLARD-9520", "C$", "0_SVN", "2_DEV", "0_SCRIPTS.Src")
#--
#-- FUNCTIONS - FILE HASH:
def HASH_File(filename):
    h = hashlib.md5()
    with open(filename, 'rb') as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()
#--
#-- FUNCTIONS - RETRIEVE DUPLICATE FILES:
def RETR_Dups(folder):
    Hashes = {}
    for dirpath, _, filenames in os.walk(folder):
        for f in filenames:
            FULLPath = os.path.join(dirpath, f)
            FILEHash = HASH_File(FULLPath)
            if FILEHash in Hashes:
                logging.info(f"NOTE - DUPLICATE FILE FOUND @ {FULLPath} == {Hashes[FILEHash]}")
            else:
                Hashes[FILEHash] = FULLPath
#--
#-- RETRIEVE DUPLICATE FILES:
RETR_Dups(DIRPaths)
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: