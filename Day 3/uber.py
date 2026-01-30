import os
import random
import datetime
import shutil
import time
import datetime

print("Welcome to Uber!")
uder_id=input("Enter user ID: ")
name = input("Enter name: ")
phone = input("Enter phone number: ")
masked_phone = phone[0] + "********" + phone[-1]
if len(phone) != 10 or not phone.isdigit():
    print("Invalid phone number")
    exit()

cities = ["Chennai", "Bangalore", "Pondicherry", "Hyderabad", "Mumbai", "Delhi"]
print("Available Cities:")
print(cities)
src = input("Enter pickup city: ").title()
dest = input("Enter drop city: ").title()
if src == dest:
    print("Pickup and drop locations cannot be the same.")
    exit()
if src not in cities or dest not in cities:
    print("Invalid city selection.")
    exit()
if src==dest:
    print("Pickup and drop locations cannot be the same.")
    exit()
if src not in cities or dest not in cities:
    print("Service not available in the selected city.")
    exit()

distance = {
    ("Chennai", "Bangalore"): 346,
    ("Chennai", "Pondicherry"): 151,
    ("Chennai", "Hyderabad"): 627,
    ("Chennai", "Mumbai"): 1338,
    ("Chennai", "Delhi"): 2180,

    ("Bangalore", "Pondicherry"): 312,
    ("Bangalore", "Hyderabad"): 569,
    ("Bangalore", "Mumbai"): 984,
    ("Bangalore", "Delhi"): 2150,

    ("Pondicherry", "Hyderabad"): 867,
    ("Pondicherry", "Mumbai"): 1290,
    ("Pondicherry", "Delhi"): 2210,

    ("Hyderabad", "Mumbai"): 709,
    ("Hyderabad", "Delhi"): 1560,

    ("Mumbai", "Delhi"): 1415
}
if (src, dest) in distance:
    distance = distance[(src, dest)]
elif (dest, src) in distance:
    distance = distance[(dest, src)]
else:
    print("Distance data not available.")
    exit()
print(f"Distance between {src} and {dest} is {distance} km")
time.sleep(1)

print("\nSelect Ride Type:")
print("1. Car")
print("2. Auto")
print("3. Bike")
print("4. Scooty")
choice = input("Enter your choice (1-4): ")
if choice == "1":
    vehicle = "Car"
    multiplier = 3
elif choice == "2":
    vehicle = "Auto"
    multiplier = 2
elif choice == "3":
    vehicle = "Bike"
    multiplier = 1.5
elif choice == "4":
    vehicle = "Scooty"
    multiplier = 1
else:
    print("Invalid choice. Defaulting to Scooty.")
    vehicle = "Scooty"
    multiplier = 1

base=5
fare_per_km=15
total=base + (fare_per_km * distance)
print(f"Hello {name}, your ride from {src} to {dest} covering {distance} km will cost Rs.{total}.")
time.sleep(2)

print("Finding a driver for you...")
time.sleep(4)
driver=["alice","bob","charlie","david","eva"]
print("The driver assigned for your ride is:")
assigned_driver=random.choice(driver)
print(assigned_driver)
status="Driver Assigned"
print(f"Current Status: {status}")
time.sleep(4)

print("Driver arrived at your location.")
print("your 2 min of free waiting time is started")
time.sleep(4)
print("Enter the otp to confirm your ride:")
otp=input()
if otp=="1234":
    print("OTP confirmed.")
    status="Ride Started"
    print(f"Current Status: {status}")
    time.sleep(4)
    print("Ride completed successfully.")
    status="COMPLETED"
    print(f"Current Status: {status}")
    rating=input("Please rate your ride experience (1-5):")
    print(f"Thank you for rating us {rating} stars!")
    feedback=input("Please provide your feedback for the ride:")
    print("Thank you for your feedback!")
else:
    print("Invalid OTP. Ride cancelled.")
    status="CANCELLED"
summary = f"""
Date     : {datetime.date.today()}
Time     : {datetime.datetime.now().strftime("%H:%M:%S")}
User ID : {uder_id}
Customer : {name}
Phone    : {masked_phone}
Driver   : {assigned_driver.title()}
Pickup   : {src.title()}
Drop     : {dest.title()}
Fare     : Rs.{total}
Status   : {status}
Rating   : {rating} stars
Feedback : {feedback}
"""
print(summary)

if not os.path.exists("uber_records"):
    os.mkdir("uber_records")
file_path = "uber_records/ride_records.txt"
with open(file_path, "a", encoding="utf-8") as file:
    file.write(summary)
if not os.path.exists("uber_backup"):
    os.mkdir("uber_backup")
backup_file = f"uber_backup/ride_backup_{datetime.date.today()}.txt"
shutil.copy(file_path, backup_file)
print("Ride details saved and backed up successfully")
