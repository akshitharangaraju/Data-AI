import os
import shutil
import datetime

source=r"C:\Users\akshi\OneDrive\Desktop\akanksh bharadwaj.txt"
newpath=r"C:\Users\akshi\OneDrive\Desktop\backup_1"
os.mkdir(newpath)
backup=rf"{newpath}\backup_{datetime.date.today()}.txt"
shutil.copy(source,backup)
print("file backed up successfully")