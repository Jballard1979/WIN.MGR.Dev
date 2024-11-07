#-- ************************************************************************************************************:
#-- ************************************** PURGE WIN OF TEMP & BROWS HIST **************************************:
#-- ************************************************************************************************************:
#-- Author:   JBallard (JEB)											  										:
#-- Date:     2014.5.12											      										    :
#-- Script:   SYS-WIN.PURGE.ps1																			        :
#-- Purpose:  A script that purges windows systems of temp, history, & browser cache.                           :
#-- Version:  1.0		  																						:
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ****************************************************:
#-- ISSUE COMMANDS TO PURGE WIN OF TEMP & CACHE FILES   :
#-- ****************************************************:
#-- VERIFY SCRIPT HAS BEEN RAN USING ADMIN PREV:
if (-not ([Security.Principal.WindowsPrincipal] -
	[Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))
{
	#--
    #-- RESTART SCRIPT AS AN ADMIN:
    START-PROCESS POWERSHELL.exe "-FILE `"$PSCommandPath`"" -VERB RUNAS
    EXIT
}
#--
#-- REMOVE WIN TEMP FILES:
REMOVE-ITEM -PATH "$env:systemroot\Temp\*" -RECURSE -FORCE
#--
#-- REMOVE IE TEMP FILES:
RUNDll32.exe InetCpl.cpl, ClearMyTracksByProcess 8
#--
##--REMOVE MOZILLA FIREFOX TEMP FILES:
REMOVE-ITEM -PATH "$env:LOCALAPPDATA\Mozilla\Firefox\Profiles\*\cache2\entries\*" -RECURSE -FORCE
#--
#-- REMOVE MS EDGE TEMP FILES:
REMOVE-ITEM -PATH "$env:LOCALAPPDATA\Packages\Microsoft.MicrosoftEdge*\AC\MicrosoftEdge\Cache\*" -RECURSE -FORCE
#--
#-- REMOVE GOOGLE CHROME TEMP FILES:
REMOVE-ITEM -PATH "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Cache\*" -RECURSE -FORCE
#--
#-- CLEAN WINDOWS EVENT LOGS:
#--WEVTUTIL.exe cl Application
#--WEVTUTIL.exe cl System
#--WEVTUTIL.exe cl Security
#--WEVTUTIL.exe cl Setup
#--
#-- REMOVE FILES FROM RECYCLE BIN:
CLEAR-RECYCLEBIN -FORCE
#--
#-- ****************************************************:
#-- END OF SCRIPT										:
#-- ****************************************************: