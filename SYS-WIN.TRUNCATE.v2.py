#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- ********************************************** TRUNCATE FILES **********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2021.9.12                                                                                         :
#-- Script:   SYS-WIN.TRUNCATE.v2.py                                                                            :
#-- Purpose:  A python script that scans directory paths for purging files/folders older than x days.           :
#-- Class:    python -m pip install -U shutil                                                                   :
#-- Class:    python -m pip install -U tqdm                                                                     :
#-- Class:    python -m pip install -U datetime                                                                 :
#-- Class:    python -m pip install -U Pool                                                                     :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import os
import shutil
import datetime
import tqdm
from tqdm import tqdm
from multiprocessing.pool import Pool
#--
#-- DIRECTORIES TO PURGE:
DIRPaths = [
    'C:/WINDOWS/Temp/',
    'C:/WINDOWS/SystemTemp/',
    'C:/WINDOWS/Prefetch/',
    'C:/WINDOWS/SoftwareDistribution/DOWNLOAD/',
    'C:/Users/jballard/AppData/Local/Downloaded Installations/',
    'C:/Users/jballard/AppData/Local/TEMP/',
    'C:/Users/jballard/Pictures/',
    'C:/Users/jballard/Videos/',
    'C:/Users/jballard-admin/AppData/Local/TEMP/',
    'C:/Users/jballard-admin/AppData/Local/Downloaded Installations/',
    'C:/Users/jballard-admin/Pictures/',
    'C:/Users/jballard-admin/Videos/',
]
#--
#-- AGE OF ITEMS PURGE & POOL SIZE:
MAXAGEDays = 0
POOLSize   = 8
#--
#-- CALCULATE DATE & ITERATE THRU FILES/FOLDERS:
CUTOFFDate = datetime.datetime.now() - datetime.timedelta(days=MAXAGEDays)
#--
#-- FUNCTION - PURGE ITEM PROCESS:
def PURGEItem(item):
    #-- VERIFY DIR EXISTS:
    if os.path.isdir(item):
        DIRMTime = datetime.datetime.fromtimestamp(os.path.getmtime(item))
        if DIRMTime < CUTOFFDate:
            shutil.rmtree(item)
    elif os.path.isfile(item):
        FILEMTime = datetime.datetime.fromtimestamp(os.path.getmtime(item))
        if FILEMTime < CUTOFFDate:
            os.remove(item)
#--
#-- MAIN:
if __name__ == '__main__':
    #-- BUILD A POOL OF WORKER PROCESSES:
    WRKRPool = Pool(POOLSize)
    #-- ITERATE THRU DIRS TO PURGE & SUBMIT ITEMS TO POOL:
    for DIRPath in tqdm(DIRPaths, desc="NOTE - DIRECTORIES BEING PROCESSED:"):
        if os.path.exists(DIRPath):
            pbar = tqdm(total=len(os.listdir(DIRPath)), desc=f"PROCESSING PURGE {DIRPath}:")
            for item in os.listdir(DIRPath):
                ITEMPath = os.path.join(DIRPath, item)
                WRKRPool.apply_async(PURGEItem, (ITEMPath,))
                pbar.update(1)
            pbar.close()
    #--
    #-- CLOSE POOL & WAIT FOR TASK COMPLETION:
    WRKRPool.close()
    WRKRPool.join()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: