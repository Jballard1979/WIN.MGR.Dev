#--!/usr/bin/env python
#-- -*- coding: Latin-1 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************** LAYOUT DESIGN SKILLS ******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.4.24                                                                                         :
#-- Script:   WIN-DEFAULT.LAYOUT.py                                                                             :
#-- Purpose:  A python script uses tkinter's layout management capabilities.                                    :
#-- Class:    python -m pip install customtkinter                                                               :
#-- Class:    python -m pip install tkinter                                                                     :
#-- Class:    python -m pip install asksaveasfile                                                               :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES         :
#-- ********************************************************:
import customtkinter as ctk
import tkinter as tk
from tkinter.filedialog import asksaveasfile
#--
#-- SUPPORTED MODES = LIGHT; DARK; & SYSTEM:
ctk.set_appearance_mode("System") 
#--
#-- SUPPORTED THEMES = GREEN; DARK-BLUE; & BLUE:
ctk.set_default_color_theme("blue") 
#--
#-- SET DIMENSIONS FOR APP:
appWidth, appHeight = 1400, 400
#--
#-- APP CLASS:
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
	#--
        self.title("CI Downloader")
        self.geometry(f"{appWidth}x{appHeight}")
	#--
        #-- INITIALIZE VARS:
        self.tenant_group_id = 0
        self.tenant_id = 0
        self.region_id = 0
        self.site_id = 0
        header = ["Name", "Model/Type", "Mgmt IP", "Tenant", "Site", "Region", "Serial", "Primary Device" ]
        #--
        #-- GENERATE SIDEBAR FRAM W/ WIDGETS:
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=5)
        self.sidebar_frame.grid(row=0, column=0, rowspan=9, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
	#--
        #-- GENERATE TABLE FRAME:
        self.table_frame = ctk.CTkFrame(self, width=800, corner_radius=5)
        self.table_frame.grid(row=3, column=1, columnspan=10, rowspan=20,  padx=20, pady=20, sticky="nsew")
        self.table_frame.grid_columnconfigure(0, weight=1)
        self.table_frame_switches = []
	#--
        #-- URL LABEL:
        self.url_label = ctk.CTkLabel(self, text="URL")
        self.url_label.grid(row=0, column=1, padx=5, pady=5, sticky="e")
	#--
        #-- URL ENTRY FIELD:
        self.url_entry = ctk.CTkEntry(self, placeholder_text="https://demo.netbox.dev/",)
        self.url_entry.grid(row=0, column=2, columnspan=4, padx=5, pady=5, sticky="ew")
	#--
        #-- TOKEN LABEL:
        self.token_label = ctk.CTkLabel(self, text="Token")
        self.token_label.grid(row=1, column=1, padx=5, pady=5, sticky="e")
	#--
        #-- TOKEN ENTRY FIELD:
        self.token_entry = ctk.CTkEntry(self, placeholder_text="b353f1efdc128974423ec7dbf4e75460923de9f8")
        self.token_entry.grid(row=1, column=2, columnspan=4, padx=5, pady=5, sticky="ew")
        #--
        #-- CONNECT BUTTON:
        self.connect_to_server_button = ctk.CTkButton(self.sidebar_frame, text="Connect to Server", command=self.dummy_function)
        self.connect_to_server_button.grid(row=0, column=0, columnspan=1, padx=5, pady=5, sticky="ew")
        #--
        #-- LOAD DATA BUTTON:
        self.load_data_button = ctk.CTkButton(self.sidebar_frame, text="Load Data", command=self.dummy_function)
        self.load_data_button.grid(row=7, column=0, columnspan=1, padx=5, pady=5, sticky="ew")
        self.load_data_button.configure(state="disabled")
        #--
        #-- SAVE DATA BUTTON:
        self.save_data_button = ctk.CTkButton(self.sidebar_frame, text="Save Data", command=self.dummy_function)
        self.save_data_button.grid(row=8, column=0, columnspan=1, padx=5, pady=5, sticky="ew")
        self.save_data_button.configure(state="disabled")
        #--
        #-- TENANT GROUP DROPDOWN:
        self.tenant_group_option_menu_var = ctk.StringVar(value="select")
        self.tenant_group_option_menu = ctk.CTkOptionMenu(self.sidebar_frame,values=[], command=self.dummy_function, variable=self.tenant_group_option_menu_var)
        self.tenant_group_option_menu.grid(row=3, column=0, columnspan=1, padx=5, pady=5, sticky="new")
        self.tenant_group_option_menu.configure(state="disabled")
        #--
        #-- TENANT DROPDOWN
        self.tenant_option_menu_var = ctk.StringVar(value="all")
        self.tenant_option_menu = ctk.CTkOptionMenu(self.sidebar_frame,values=[], command=self.dummy_function, variable=self.tenant_option_menu_var)
        self.tenant_option_menu.grid(row=4, column=0,  columnspan=1, padx=5, pady=5, sticky="ew")
        self.tenant_option_menu.configure(state="disabled")
        #--
        #-- REGION DROPDOWN:
        self.region_option_menu_var = ctk.StringVar(value="all")
        self.region_option_menu = ctk.CTkOptionMenu(self.sidebar_frame,values=[],  command=self.dummy_function, variable=self.region_option_menu_var)
        self.region_option_menu.grid(row=5, column=0, columnspan=1, padx=5, pady=5, sticky="ew")
        self.region_option_menu.configure(state="disabled")
        #--
        #-- SITE DROPDOWN:
        self.site_option_menu_var = ctk.StringVar(value="all")
        self.site_option_menu = ctk.CTkOptionMenu(self.sidebar_frame,values=[], command=self.dummy_function, variable=self.site_option_menu_var)
        self.site_option_menu.grid(row=6, column=0, columnspan=1, padx=5, pady=5, sticky="ew")
        self.site_option_menu.configure(state="disabled")
    #--
    #-- DUMMY FUNCTION FOR [COMMAND] REF IN WIDGETS:
    def dummy_function(self):
        pass
#--
#-- MAIN LOOP:
if __name__ == "__main__":
    app = App()
    app.mainloop()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: