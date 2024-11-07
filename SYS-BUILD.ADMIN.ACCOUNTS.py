#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- ************************************************************************************************************:
#-- *************************************** CREATE LOCAL ADMIN ACCOUNTS ****************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.6.15                                                                                         :
#-- Script:   SYS-BUILD.ADMIN.ACCOUNTS.py                                                                       :
#-- Purpose:  A python script that remotely creates Local Admin Accounts on usr specific Systems.               :
#-- Class:    python -m pip install paramiko                                                                    :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import paramiko
#--
def BLD_LOC_ADMIN_Act(hostname, username, password, new_username, new_password):
    try:
        #-- CONNECT TO REMOTE SYS:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)
        #--
        #-- BUILD NEW LOCAL ADMIN ACT:
        command = f"net user {new_username} {new_password} /add"
        stdin, stdout, stderr = client.exec_command(command)
        #--
        #-- VERIFY SUCCESSFUL ACT CREATION:
        if "The command completed successfully" in stdout.read().decode():
            print(f"NOTE - SUCCESSFULLY CREATED LOCAL ADMIN ACCOUNT FOR {new_username} ON {hostname}:")
        else:
            print(f"ERROR - FAILED TO CREATE LOCAL ADMIN ACCOUNT ON {hostname}:")
        #--
        #-- CLOSE SSH CONNECTION:
        client.close()
    except Exception as e:
        print(f"ERROR - FAILED TO CREATE LOCAL ADMIN ACCOUNT ON {hostname}: {str(e)}")
#--
#-- DEFINE LIST OF DESIRED SYSTEMS TO CREATE LOCAL ACTS ON:
systems = [
    {
        "hostname": "SYSLP1.JBHOME.com",
        "username": "JBallard",
        "password": "NevrGuessPW@1",
        "new_username": "JBallardAdmin",
        "new_password": "NevrGuessAdPW@1"
    },
    {
        "hostname": "SYSLP2.JBHOME.com",
        "username": "JBallard",
        "password": "NevrGuessPW@1",
        "new_username": "JBallardAdmin",
        "new_password": "NevrGuessAdPW@1"
    },
]
#--
#-- CREATE LOCAL ADMIN ACTS FOR EACH SYS:
for system in systems:
    BLD_LOC_ADMIN_Act(system["hostname"], system["username"], system["password"], system["new_username"], system["new_password"])
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: