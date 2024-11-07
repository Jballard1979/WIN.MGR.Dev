#--
#-- ************************************************************************************************************:
#-- ****************************************** AUTOMATE PROOFREADING: ******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.3.07                                                                                         :
#-- Script:   PROOFREAD.TXT.FILES.py                                                                            :
#-- Purpose:  A python script that proofreads text for grammatical & spelling errors.                           :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#--python -m pip install lmproof
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
import lmproof as lm
#--
#-- AUTOMATE PROOFREADING:
def ProofRead(text):
    proof = lm.load("en")
    corrections = proof.proofread(text)
    print("PROOFREAD: ", corrections)
ProofRead("The brow fox jumpe the lazy dog.")
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: