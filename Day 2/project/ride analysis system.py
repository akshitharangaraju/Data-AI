import os
import shutil
import datetime

PIN = "4040"
attempt = 1
while attempt <= 3:
    user_pin = input("Enter your PIN: ")
    if user_pin == PIN:
        print("Login successful!\n")
        break
    else:
        print("Incorrect PIN")
        attempt += 1
if attempt > 3:
    print("Too many attempts. Access denied.")
    exit()

name = input("Enter name: ").strip()
email = input("Enter email: ").strip()
phone = input("Enter phone number: ")
gender = input("Enter gender: ")
if not name.isalpha():
    print("Invalid name")
    exit()
if "@" not in email and "." not in email:
    print("Invalid email")
    exit()
if len(phone) != 10 or not phone.isdigit():
    print("Invalid phone number")
    exit()

masked_phone = phone[0] + "********" + phone[-1]
initials = "".join([word[0].upper() for word in name.split()])

user_profile = {
    "Name": name.title(),
    "Initials": initials,
    "Email": email,
    "Phone": masked_phone,
    "Gender": gender
}

driver = input("Enter driver name: ")
pickup = input("Enter pickup location: ")
drop = input("Enter drop location: ")
fare = float(input("Enter base fare: "))
day = input("Enter day of ride: ").lower()
gold = input("Is Gold Member (True/False): ")

discount = 0
if fare > 500 and gold == "True" and day in ["saturday", "sunday"]:
    discount = fare * 0.2
final_fare = fare - discount

promo = input("Enter promo code (or press enter): ").upper()
if promo == "UBER20":
    final_fare -= 50
    promo_status = "Promo Applied"
else:
    promo_status = "No Promo Applied"

feedback = input("Enter feedback: ")

summary = f"""
Customer   : {user_profile['Name']} ({user_profile['Initials']})
Phone      : {user_profile['Phone']}
Driver     : {driver.title()}
Pickup     : {pickup.title()}
Drop       : {drop.title()}
Day        : {day.title()}
Fare       : Rs.{fare}
Discount   : Rs.{discount}
Final Fare : Rs.{final_fare}
Promo      : {promo_status}
Status     : COMPLETED
"""
print(summary)


if not os.path.exists("records"):
    os.mkdir("records")
file_path = "records/ride_records.txt"
with open(file_path, "a", encoding="utf-8") as file:
    file.write(summary)
if not os.path.exists("backup"):
    os.mkdir("backup")
backup_file = f"backup/ride_backup_{datetime.date.today()}.txt"
shutil.copy(file_path, backup_file)
print("Ride details saved and backed up successfully")
