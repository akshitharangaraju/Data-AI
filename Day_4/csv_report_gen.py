import csv

with open("report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Akki", 20, "Karimnagar"])
    writer.writerow(["Bunny", 22, "Medak"])
    writer.writerow(["Suzzie",20,"Hyderabad"])

print("CSV report created")