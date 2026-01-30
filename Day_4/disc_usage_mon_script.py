import shutil
total, used, free = shutil.disk_usage("/")
total_gb = total // (1024**3)
used_gb = used // (1024**3)
free_gb = free // (1024**3)
usage_percent = (used / total) * 100
print(f"Total Disk Space : {total_gb} GB")
print(f"Used Disk Space  : {used_gb} GB")
print(f"Free Disk Space  : {free_gb} GB")
print(f"Usage Percentage: {usage_percent:.2f}%")
if usage_percent > 80:
    print("WARNING: Disk usage exceeded 80%")

with open("disk_usage_report.txt", "w") as file:
    file.write(f"Total Disk Space : {total_gb} GB\n")
    file.write(f"Used Disk Space  : {used_gb} GB\n")
    file.write(f"Free Disk Space  : {free_gb} GB\n")
    file.write(f"Usage Percentage: {usage_percent:.2f}%\n")
print("Disk usage report saved successfully.")
