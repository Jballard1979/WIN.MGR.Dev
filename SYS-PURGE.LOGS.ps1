#--
#-- ************************************************************************************************************:
#-- ******************************************* PURGE LISTEN ONLY LOG ******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.11.10                                                                                        :
#-- Script:   SYS-PURGE.LOGS.ps1                                                                                :
#-- Dir:      C:\SchneiderElectricData\OASyS\Servers\tools\NetworkListener\                                     :
#-- Purpose:  A PowerShell script that purges the TCP Listen Only Log File.                                     :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- RUN POWERSHELL SCRIPT WITH ADMIN PRIVILEGES             :
#-- ********************************************************:
if (-Not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))
{
    WRITE-HOST "NOTE - REQUIRES ADMIN PRIVILEGES:"
    EXIT
}
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
$PURGEPaths = "C:\SchneiderElectricData\OASyS\Servers\tools\NetworkListener\TcpListener.log"
#--
# DOES LOG FILE EXIST?:
if (TEST-PATH $PURGEPaths)
{
    try 
	{
        #-- PURGE LOG FILE:
        REMOVE-ITEM -PATH $PURGEPaths -FORCE
        WRITE-HOST "THE NETWORK LISTEN ONLY LOG '$PURGEPaths' HAS BEEN PURGED:"
    }
	catch
	{
        WRITE-HOST "ERROR: FAILED TO PURGE LOG FILE: $($error[0].Exception.Message)"
    }
}
else
{
    WRITE-HOST "THE LOG FILE '$PURGEPaths' WAS NOT FOUND:"
}
#--
#-- ********************************************************:
#-- END OF SCRIPT                                           :
#-- ********************************************************: