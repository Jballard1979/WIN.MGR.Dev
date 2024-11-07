#-- !/usr/bin/env python3
#-- -*- coding: utf-8 -*-
#--
#-- ************************************************************************************************************:
#-- *********************************************** RENAME FILES ***********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.1.05                                                                                         :
#-- Script:   WIN-FILE.AUTOMATION.py                                                                            :
#-- Purpose:  A python script that renames all files within the specified directory.                            :
#-- Class:    python -m pip install scandir                                                                     :
#-- Class:    python -m pip install rename                                                                      :
#-- Class:    python -m pip install splitext                                                                    :
#-- Class:    python -m pip install exists                                                                      :
#-- Class:    python -m pip install join                                                                        :
#-- Class:    python -m pip install shutil                                                                      :
#-- Class:    python -m pip install move                                                                        :
#-- Class:    python -m pip install time                                                                        :
#-- Class:    python -m pip install sleep                                                                       :
#-- Class:    python -m pip install logging                                                                     :
#-- Class:    python -m pip install Observer                                                                    :
#-- Class:    python -m pip install FileSystemEventHandler                                                      :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
#--
#-- FILL IN BELOW {"C:\USERS\JBALLARD-ADMIN\\DOWNLOADS"}
SRCDir       = "\\JBALLARD-9520\c$\0_SVN\4_PERSONAL\PY.PROC.STORE"
DSTDIRSFx    = ""
DSTDIRAudio  = ""
DSTDIRVideo  = ""
DSTDIRImages = ""
DSTDIRDocs   = ""
#--
#-- IDENTIFY IMAGE; VIDEO; AUDIO; & DOCUMENT EXTENSIONS:
IMGExt = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
VIDExt = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
AUDExt = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
DOCExt = [".doc", ".docx", ".odt",
    ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
#--
#-- FUNCTION - MAKE UNIQUE:
def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    #--
    #-- IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME:
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name
#--
#-- FUNCTION - MOVE FILES:
def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)
#--
#-- CLASS - RUNS IF A CHANGE HAS BEEN DETECTED WITHIN "SRCDir":
class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(SRCDir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
    #--
    #-- FUNCTION - CHECKS AUDIO FILES:
    def check_audio_files(self, entry, name):
        for audio_extension in AUDExt:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:
                    dest = DSTDIRSFx
                else:
                    dest = DSTDIRAudio
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")
    #--
    #-- FUNCTION - CHECKS VIDEO FILES:
    def check_video_files(self, entry, name):
        for video_extension in VIDExt:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(DSTDIRVideo, entry, name)
                logging.info(f"NOTE - MOVED VIDEO FILE: {name}")
    #--
    #-- FUNCTION - CHECKS ALL IMAGE FILES:
    def check_image_files(self, entry, name):
        for image_extension in IMGExt:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(DSTDIRImages, entry, name)
                logging.info(f"NOTE - MOVED IMAGE FILE: {name}")
    #--
    #-- FUNCTION - CHECKS ALL DOCUMENT FILES:
    def check_document_files(self, entry, name):
        for documents_extension in DOCExt:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(DSTDIRDocs, entry, name)
                logging.info(f"NOTE - MOVED DOC FILE: {name}")
#--
#--
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    path = SRCDir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: