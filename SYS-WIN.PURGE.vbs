' **************************************************************************************************************:
' ********************************************* PURGE TEMP & HIS DIR *******************************************:
' **************************************************************************************************************:
' Author:   JBallard (JEB)                                                                                      :
' Date:     2018.9.05                                                                                           :
' Script:   SYS-WIN.PURGE.vbs                                                                                   :
' Dir:      \\JBALLARD-9520\C$\0_SVN\2_DEV\0_SCRIPTS.Src\0_USEFUL.Dev\3_CLEAN.Dev                               :
' Purpose:  A VBScript that purges out all Windows TEMP, History, PREFETCH, & Cache Directories                 :
' Version:  1.0                                                                                                 :
' **************************************************************************************************************:
' **************************************************************************************************************:
'
' **************************************************:
' DEFINE PARAMS, CONFIG PATHS, IMPORT CLASSES       :
' **************************************************:
DIM FileSystem
'
CONST DeleteReadOnly = TRUE
CONST DeleteFolder   = TRUE
CONST DeleteFile     = TRUE
'
Sub RunApplication(ByVal StrFile)
    DIM WShell : SET WShell = CreateObject("WScript.Shell")
    WShell.Run Chr(34) & StrFile & Chr(34), 8, FALSE
End Sub
'
SET ObjectFSO = CreateObject("Scripting.FileSystemObject")
SET ObjectLog = ObjectFSO.CreateTextFile("\\JBALLARD-9520\C$\0_SVN\7_LOGS\SYS-WIN.PURGE.jeb")
' 
' **************************************************:
' FUNCTION - DELETE ALL TEMP USER & SYSTEM FILES    :
' **************************************************:
SET OShell     = CreateObject("WScript.Shell")
SET FileSystem = CreateObject("Scripting.FileSystemObject")
SET ObjFSO     = CreateObject("Scripting.FileSystemObject")
'
' **************************************************:
' FILE DIRECTORIES TO BE PURGED                     :
' **************************************************:
SET MEDIA    = FileSystem.GetFolder("\\JBALLARD-9520\C$\Users\jballard\Pictures")
SET MEDIA2   = FileSystem.GetFolder("\\JBALLARD-9520\C$\Users\jballard-admin\Pictures")
SET DOWNLOAD = FileSystem.GetFolder("\\JBALLARD-9520\C$\Windows\SoftwareDistribution\DOWNLOAD")
SET ENVTEMP  = FileSystem.GetFolder("\\JBALLARD-9520\C$\Users\jballard\AppData\Local\TEMP")
SET ENVTEMP2 = FileSystem.GetFolder("\\JBALLARD-9520\C$\Users\jballard-admin\AppData\Local\TEMP")
SET ENVTEMP3 = FileSystem.GetFolder("\\JBALLARD-9520\C$\Users\Administrator\AppData\Local\TEMP")
SET TEMP     = FileSystem.GetFolder("\\JBALLARD-9520\C$\Windows\TEMP")
SET PREFETCH = FileSystem.GetFolder("\\JBALLARD-9520\C$\Windows\PREFETCH")
SET LOGS     = FileSystem.GetFolder("\\JBALLARD-9520\C$\0_SVN\7_LOGS\BACKUP")
'
WSCRIPT.ECHO "" & date & ": " & time & " - " & " NOTICE - PURGING WIN SYSTEM OF ALL CLUTTER: "
'
' **************************************************:
' CHECK IF SOFTWARE DISTRIBUTION DIRECTORY EXISTS   :
' **************************************************:
If FileSystem.FolderExists(MEDIA) Then
	' DELETE ALL ROOT FILES:
	For Each FLDR In MEDIA.Files
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(MEDIA), DeleteReadOnly 
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & MEDIA & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & MEDIA & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
	' DELETE SUBFOLDERS & FILES:
	For Each FLDR In MEDIA.SubFolders
		On Error Resume Next
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(MEDIA), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & MEDIA & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & MEDIA & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
End If
'
If FileSystem.FolderExists(MEDIA2) Then
	' DELETE ALL ROOT FILES:
	For Each FLDR In MEDIA2.Files
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(MEDIA2), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & MEDIA2 & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & MEDIA2 & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
	' DELETE SUBFOLDERS & FILES:
	For Each FLDR In MEDIA2.SubFolders
		On Error Resume Next
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(MEDIA2), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & MEDIA2 & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & MEDIA2 & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
End If
'
' **************************************************:
' CHECK IF DOWNLOAD DIRECTORY EXISTS                :
' **************************************************:
If FileSystem.FolderExists(DOWNLOAD) Then
	' DELETE ALL ROOT FILES:
	For Each FLDR In DOWNLOAD.Files
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(DOWNLOAD), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & DOWNLOAD & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & DOWNLOAD & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
	' DELETE SUBFOLDERS & FILES:
	For Each FLDR In DOWNLOAD.SubFolders
		On Error Resume Next
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(DOWNLOAD), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & DOWNLOAD & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & DOWNLOAD & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
End If
'
' **************************************************:
' CHECK IF APPDATA DIRECTORY EXISTS                 :
' **************************************************:
If FileSystem.FolderExists(ENVTEMP) Then
	' DELETE ALL ROOT FILES:
	For Each FLDR In ENVTEMP.Files
		NAME = FLDR.NAME
		ObjFSO.DeleteFile(ENVTEMP), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
	' DELETE SUBFOLDERS & FILES:
	For Each FLDR In ENVTEMP.SubFolders
		On Error Resume Next
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(ENVTEMP), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
End If
'
If FileSystem.FolderExists(ENVTEMP2) Then
	' DELETE ALL ROOT FILES:
	For Each FLDR In ENVTEMP2.Files
		NAME = FLDR.NAME
		ObjFSO.DeleteFile(ENVTEMP2), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP2 & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP2 & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
	' DELETE SUBFOLDERS & FILES:
	For Each FLDR In ENVTEMP2.SubFolders
		On Error Resume Next
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(ENVTEMP2), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP2 & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP2 & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
End If
'
If FileSystem.FolderExists(ENVTEMP3) Then
	' DELETE ALL ROOT FILES:
	For Each FLDR In ENVTEMP3.Files
		NAME = FLDR.NAME
		ObjFSO.DeleteFile(ENVTEMP3), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP3 & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP3 & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
	' DELETE SUBFOLDERS & FILES:
	For Each FLDR In ENVTEMP3.SubFolders
		On Error Resume Next
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(ENVTEMP3), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP3 & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & ENVTEMP3 & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
End If
'
' **************************************************:
' CHECK IF TEMP DIRECTORY EXISTS                    :
' **************************************************:
If FileSystem.FolderExists(TEMP) Then
	' DELETE ALL ROOT FILES:
	For Each FLDR In TEMP.Files
		NAME = FLDR.NAME
		'FLDR.Delete TRUE
		ObjFSO.DeleteFile(TEMP), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & TEMP & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & TEMP & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
	' DELETE SUBFOLDERS & FILES:
	For Each FLDR In TEMP.SubFolders
		On Error Resume Next
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(TEMP), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & TEMP & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & TEMP & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
End If
'
' **************************************************:
' CHECK IF PREFETCH DIRECTORY EXISTS                :
' **************************************************:
If FileSystem.FolderExists(PREFETCH) Then
	' DELETE SUBFOLDERS & FILES:
	For Each FLDR In PREFETCH.SubFolders
		On Error Resume Next
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(PREFETCH), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & PREFETCH & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & PREFETCH & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
	' DELETE ALL ROOT FILES:
	For Each FLDR In PREFETCH.Files
		NAME = FLDR.NAME
		ObjFSO.DeleteFile(PREFETCH), DeleteReadOnly
		'ObjFSO.DeleteFile(PREFETCH & \*.pf), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & PREFETCH & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & PREFETCH & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
End If
'
' **************************************************:
' CHECK IF LOGS DIRECTORY EXISTS                    :
' **************************************************:
If FileSystem.FolderExists(LOGS) Then
	' DELETE SUBFOLDERS & FILES:
	For Each FLDR In LOGS.SubFolders
		On Error Resume Next
		NAME = FLDR.NAME
		FLDR.Delete TRUE
		ObjFSO.DeleteFile(LOGS), DeleteReadOnly
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & LOGS & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & LOGS & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
	' DELETE ALL ROOT FILES:
	For Each FLDR In LOGS.Files
		NAME = FLDR.NAME
		ObjFSO.DeleteFile(LOGS), DeleteFile
		If Err Then
			ObjectLog.WriteLine "" & date & ": " & time & " - " & LOGS & " - "  & NAME & " - " & "PURGING ERROR:"
		Else
			ObjectLog.WriteLine "" & date & ": " & time & " - " & LOGS & " - " & NAME & " - " & "PURGED:"
		End If
		On Error GoTo 0
	Next
End If
'
WSCRIPT.ECHO "" & date & ": " & time & " - " & " SUCCESS - PURGED WIN SYSTEM OF ALL CLUTTER: "
'
' **************************************************: 
' END OF SCRIPT										:
' **************************************************: