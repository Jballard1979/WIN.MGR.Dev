#--
#-- ************************************************************************************************************:
#-- ********************************************* EXTRACT PDF TABLES *******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.2.18                                                                                         :
#-- Script:   EXTRACT-PDF.2.EXCEL.py                                                                            :
#-- Purpose:  A python script that extracts PDF tables to EXCEL.                                                :
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
#--
#-- DEFINE FUNCTION TO EXTRACT TABLE DATA TO PDF:
def extract_table_data_to_excel(pdf_path, xls_path):
    doc = PdfDocument()
    try:
        #-- LOAD PDF PATH:
        doc.LoadFromFile(pdf_path)
        #-- POPULATE LIST TO STORE PDF TABLE DATA:
        extractor = PdfTableExtractor(doc)
        workbook = Workbook()
        workbook.Worksheets.Clear()
        #--
        #-- ITERATE THROUGH PDF DOCUMENT:
        for page_index in range(doc.Pages.Count):
             #-- RETRIEVE PDF TABLES:
            tables = extractor.ExtractTable(page_index)
            if tables is not None and len(tables) > 0:
                #--
                #-- ITERATE THROUGH TABLES:
                for table_index, table in enumerate(tables):
                    #-- BUILD NEW EXCEL WORKSHEET FOR EACH EXTRACTED PDF TABLE:
                    worksheet = workbook.CreateEmptySheet()
                    worksheet.Name = f"Table {table_index + 1} of Page {page_index + 1}"
                    row_count = table.GetRowCount()
                    col_count = table.GetColumnCount()
                    #--
                    #-- EXTRACT DATA FROM EACH PDF TABLE & APPEND TO TABLE_DATA LIST:
                    for row_index in range(row_count):
                        for column_index in range(col_count):
                            data = table.GetText(row_index, column_index)
                            worksheet.Range[row_index + 1, column_index + 1].Value = data.strip()
                    #-- ADJUST EXCEL COLUMNS WIDTH:
                    worksheet.Range.AutoFitColumns()
        #-- SAVE EXCEL WORKBOOK TO PATH:
        workbook.SaveToFile(xls_path, ExcelVersion.Version2016)
    #--
    except Exception as e:
        print(f"Error occurred: {str(e)}")
#-- 
#-- USE EXAMPLE:
pdf_path = "Tables.pdf"
xls_path = "table_data.xlsx"
extract_table_data_to_excel(pdf_path, xls_path)
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: