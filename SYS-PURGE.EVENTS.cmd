@ECHO OFF
COLOR 1
:: *************************************************************************************************************:
:: ****************************************** PURGE EVENT LOGS SCRIPT ******************************************:
:: *************************************************************************************************************:
:: Author:  JBallard (JEB)                                                                                      :
:: Date:    2016.10.19                                                                                          :
:: Script:  SYSTEM-PURGE.EVENTS.cmd                                                                             :
:: Effort:  A script that clears out all Event Logs from the Systems Event Viewer.                              :
:: Ver:	    1.0                                                                                                 :
:: *************************************************************************************************************:
:: *************************************************************************************************************:
::
:: *****************************************:
:: STEP INTO PURGE EVENTS LOOP              :
:: *****************************************:
FOR /F "tokens=1,2*" %%V IN ('BCDEDIT') DO SET Admin=%%V
	IF (%Admin%)==(Access) GOTO AdminFail
		:: WEVTUTIL RETRIEVES INFO ABOUT PUBLISHERS & EVENT LOGS:
		FOR /F "tokens=*" %%G IN ('WEVTUTIL EL') DO (call :ClearLogs "%%G")
			ECHO SUCCESSFULLY PURGED ALL EVENT LOG(s)!:
			ECHO ^<PRESS SPACE BAR TO EXIT^>
		GOTO ENDPURGE
			:ClearLogs
				ECHO CLEARING EVENT LOGS @ %1
				WEVTUTIL CL %1
		GOTO :EOF
			:AdminFail
				ECHO MUST USE ADMINISTRATIVE PRIVILEDGES!:
				ECHO ^<PRESS SPACE BAR TO EXIT^>
	:ENDPURGE
EXIT
::
:: *****************************************:
:: END OF SCRIPT                            :
:: *****************************************: