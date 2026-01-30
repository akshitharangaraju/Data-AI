import shutil
import datetime
import time
import os
src = r"C:\Users\akshi\OneDrive\Desktop\primary track\Day 3"
backup_root = r"C:\Users\akshi\OneDrive\Desktop\primary track\Day_4"
os.makedirs(backup_root, exist_ok=True)
while True:
    now = datetime.datetime.now()
    if now.hour == 10 and now.minute == 47:
        dst = os.path.join(
            backup_root,
            "backup_" + now.strftime("%Y%m%d_%H%M%S")
        )
        shutil.copytree(src, dst)
        print("Backup created:", dst)
        time.sleep(60)
    time.sleep(1)