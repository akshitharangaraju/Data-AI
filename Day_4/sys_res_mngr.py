import psutil
import datetime

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("system_resource_log.txt", "a") as file:
    file.write(f"\n[{timestamp}]\n")
    file.write(f"CPU Usage    : {cpu}%\n")
    file.write(f"RAM Usage    : {memory.percent}%\n")
    file.write(f"Disk Usage   : {disk.percent}%\n")

    if cpu > 80:
        file.write("WARNING: High CPU usage\n")
    if memory.percent > 80:
        file.write("WARNING: High Memory usage\n")
    if disk.percent > 80:
        file.write("WARNING: High Disk usage\n")

print("System resource data stored successfully.")
