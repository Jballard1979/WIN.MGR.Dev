' **************************************************************************************************************:
' ********************************************* PURGE SYSTEM EVENTS ********************************************:
' **************************************************************************************************************:
' Author: 	JBallard (JEB)																						:
' Date:		2018.3.08																							:
' Script:	SYSTEM-PURGE.EVENTS.vbs																				:
' Purpose:	A VBScript that calls a batch command script & runs it via administrative mode						:
' Version:	1.0																									:
' **************************************************************************************************************:
' **************************************************************************************************************:
'
' **************************************************: 
' DEFINE PARAMETERS	& CONFIGURATION PATHS			:
' **************************************************:
Option Explicit
'
DIM WshShell, oShell, ScriptDir
'
SET oShell = CreateObject("Shell.Application")
SET WshShell = WScript.CreateObject("WScript.Shell")
'
ScriptDir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(Wscript.ScriptFullName)
If WScript.Arguments.length = 0 Then
	oShell.ShellExecute "wscript.exe", """" & WScript.ScriptFullName & """" & " RunAsAdministrator", , "runas", 1
Else
	oShell.ShellExecute ScriptDir & "\SYSTEM-WIN.EVENTS.cmd", , , "runas", 1
End If
'
' **********************************:
' END OF SCRIPT						:
' **********************************: