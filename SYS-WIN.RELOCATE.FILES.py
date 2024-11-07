#--
#-- ************************************************************************************************************:
#-- ********************************************** RELOCATE FILES **********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.9.12                                                                                         :
#-- Script:   SYS-WIN.RELOCATE.FILES.py                                                                         :
#-- Dir:      \\JBALLARD-9520\C$\0_SVN\2_DEV\0_SCRIPTS.Src\0_USEFUL.Dev\3_CLEAN.Dev\                            :
#-- Purpose:  A python script that creates a new folder & copies all Desktop files into that folder.            :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
import os, shutil
#--
lis=[]
i=1
#-- DESTINATION DIR:
DESTDir = '/Users/NAME/Desktop/Everything'
#--
#-- LOOP:
while os.path.exists(DESTDir):
    DESTDir+=str(i)
    i+=1
#-- MAKE NEW DIR:
os.makedirs(DESTDir)
lis=os.listdir('/Users/NAME/Desktop')
#-- MOVE FILES INTO DIR:
for x in lis:
    print x
    if x==__file__:
        continue
    shutil.move(x,DESTDir)
#--
#-- ********************************************************:
#-- END OF SCRIPT                                           :
#-- ********************************************************: