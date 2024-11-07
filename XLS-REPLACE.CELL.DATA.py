#--
#-- ************************************************************************************************************:
#-- ********************************************* REPLACE EXCEL DATA *******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.2.18                                                                                         :
#-- Script:   XLS-REPLACE.CELL.DATA.py                                                                          :
#-- Purpose:  A python script that replaces particular text within an EXCEL spreadsheet.                        :
#-- Class:    python -m pip install Spire.Pdf; python3 -m pip install Spire.Pdf                                 :
#-- Class:    python -m pip install Spire.Xls; python3 -m pip install Spire.Xls                                 :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
from spire.pdf import *
from spire.xls import *
from spire.xls.common import *
#--
#-- GENERATE WORKBOOK OBJECT:
workbook   = Workbook()
workbook.LoadFromFile("2024.6-MS.SECURITY.xlsx")
sheetCount = 8
#--
#-- RETRIEVE CELLS CONTAINING SPECIFIED TEXT:
for i in range(sheetCount):
    sheet  = workbook.Worksheets[i]
    ranges = sheet.FindAll("KB5", FindType.Text, ExcelFindOptions.none) #-- MatchEntireCellContent)
    #-- ITERATE THROUGH RETRIEVED CELLS:
    for range in ranges:
        #-- REPLACE TEXT:
        range.Text = ""
        range.Style.Color = Color.get_Yellow()
#--  
#-- SAVE NEW EXCEL FILE:
workbook.SaveToFile("2024.7-MS.SECURITY.xlsx", ExcelVersion.Version2016)
workbook.Dispose()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: