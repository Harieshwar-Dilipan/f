import time
import os
import shutil
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = r"C:\Users\dhari\Downloads\New folder (3)"              # Add the path of you "Downloads" folder.
 #Create "Document_Files" folder in your Desktop and update the path accordingly.

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print('file created')
    def on_modified(self, event):
        print('file modified')
    def on_deleted(self, event):
        print('file deleted')
    def on_moved(self, event):
        print('file moved')
        

# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()