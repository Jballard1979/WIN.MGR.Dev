#--
#-- ************************************************************************************************************:
#-- *********************************************** PURGE EVENTS ***********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.9.12                                                                                         :
#-- Script:   SYS-PURGE.EVENTS.py                                                                               :
#-- Purpose:  A python script that purges all the Windows Events.                                               :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- *************************************************:
#-- DEFINE PARAMS, CONFIG PATHS, IMPORT CLASSES      :
#-- *************************************************:
import os
import subprocess
#--
#-- FUNTION TO CLEAR WIN EVENT LOGS:
def clear_logs(log_name):
    print(f"CLEARING EVENT LOGS @ {log_name}")
    subprocess.run(["wevtutil", "cl", log_name], capture_output=True, text=True)
#--
def main():
    #--
    #-- VERIFY SCRIPT IS RUNNING WITH ADMIN PRIVILEGES:
    try:
        subprocess.check_call(["bcdedit"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("NOTICE - MUST USE ADMINISTRATIVE PRIVILEGES!")
        input("<PRESS SPACE BAR TO EXIT>")
        return
    #--
    #-- RETRIEVE LIST OF WIN EVENT LOGS:
    try:
        logs_output = subprocess.check_output(["wevtutil", "el"], text=True)
    except subprocess.CalledProcessError as e:
        print("FAILURE - ERROR RETRIEVING WIN EVENT LOGS:", e)
        return
    #--
    #-- SPLIT OUTPUT INTO LINES & CLEAR EACH EVENT LOG:
    for log in logs_output.splitlines():
        clear_logs(log.strip())
    #--
    print("NOTICE - SUCCESSFULLY PURGED ALL EVENT LOG(s)!")
    input("<PRESS SPACE BAR TO EXIT>")
#--
if __name__ == "__main__":
    main()
#-- *************************************************:
#-- END OF SCRIPT                                    :
#-- *************************************************: