#--
#-- ************************************************************************************************************:
#-- ********************************************* EXTRACT PDF TABLES *******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.2.18                                                                                         :
#-- Script:   EXTRACT-PDF.2.TEXT.py                                                                             :
#-- Purpose:  A python script that extracts PDF tables to TEXT.                                                 :
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
def extract_table_data(pdf_path):
    doc = PdfDocument()
    try:
        #-- LOAD PDF PATH:
        doc.LoadFromFile(pdf_path)
        #-- POPULATE LIST TO STORE PDF TABLE DATA:
        table_data = []
        extractor = PdfTableExtractor(doc)
        #--
        #-- ITERATE THROUGH PDF DOCUMENT:
        for page_index in range(doc.Pages.Count):
            #-- RETRIEVE PDF TABLES:
            tables = extractor.ExtractTable(page_index)
            if tables is not None and len(tables) > 0:
                #--
                #-- ITERATE THROUGH TABLES:
                for table_index, table in enumerate(tables):
                    row_count = table.GetRowCount()
                    col_count = table.GetColumnCount()
                    table_data.append(f"Table {table_index + 1} of Page {page_index + 1}:\n")
                    #--
                    #-- EXTRACT DATA FROM EACH PDF TABLE & APPEND TO TABLE_DATA LIST:
                    for row_index in range(row_count):
                        row_data = []
                        for column_index in range(col_count):
                            data = table.GetText(row_index, column_index)
                            row_data.append(data.strip())
                        table_data.append("  ".join(row_data))
                    table_data.append("\n")
        return table_data
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None
#--
#-- DEFINE FUNCTION TO SAVE EXTRACTED TABLE DATA TO TEXT FILE:
def save_table_data_to_text(table_data, output_path):
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write("\n".join(table_data))
        print(f"Table data saved to '{output_path}' successfully.")
    except Exception as e:
        print(f"Error occurred while saving table data: {str(e)}")
#-- 
#-- USE EXAMPLE:
pdf_path    = "Tables.pdf"
output_path = "table_data.txt"
#--
data = extract_table_data(pdf_path)
if data:
    save_table_data_to_text(data, output_path)
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: