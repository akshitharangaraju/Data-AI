#print string
str="welcome to uber"
drive="arun"
pickup="cmr"
drop="kmply"
fare=120.43
status="completed"
summary=f"Driver {drive} picked you up from {pickup} and dropped you at {drop}. The fare is {fare} and the status is {status.upper()}."
print(summary)

#masked phn number
phone="9876543210"
masked=phone[0]+"******"+phone[-1]
print(masked)

#title case
song="shApe OF You"
artist="ed ShEErAn"
formatted=f"{song.title()} - {artist.title()}"
print(formatted)

# replace  word in string
location="chnai central"
fixed=location.replace("chnai","chennai")
print(fixed)

# extract id from string
msg="your id is:UB123456. keep it safe."
id=msg.split(":")[1].split(".")[0]
print(id)

# check promo code
promo="use ZOMATO20 to get 20% off on your next order from zomato"
if "ZOMATO20" in promo:
    print("offer applied")
else:
    print("invalid code")

# find the position of the word
feedback="driver was polite. ride was comfortable."
print(feedback.find("polite"))

# extract initials 
name="Rangaraju Akshitha"
initial="".join([word[0].upper() for word in name.split()])
print(initial)

# strip unwanted spaces
dirty="akki       "
clean=dirty.strip()
print(clean)

# word count in feedback
feedback="trip was amazing and car was clean"
count=len(feedback.split())
print(count)

# check username password validity
user=input("enter username:")
password=input("enter password:")
if user=="admin" and password=="4040":
    print("login successful")
else:
    print("invalid credentials")

# check eligibility for exam
mark=int(input("enter marks:"))
attendance=int(input("enter attendance percentage:"))
if mark>=50 and attendance>=75:
    print("eligible for exam")
else:
    print("not eligible for exam")

# check data plan bonus eligibility
recharge=int(input("enter recharge amount:"))
data=int(input("enter data plan in gb:"))
if recharge>=399 and data>=2:
    print("you are eligible for bonus 2gb data plan")
else:
    print("not eligible")

# bill percentage offer
bill=int(input("enter bill amount:"))
gold=bool(input("is customer gold member (True/False):"))
day=input("enter day of the week:")
if bill>1000 and gold==True and day.lower()==("saturday" or "sunday"):
    discount=bill*0.2
    total=bill-discount
    print(f"your bill after discount is {total}")

# atm pin check
pin="5650"
i=1
while(i<=3):
    user=input("enter your atm pin:")
    if user==pin:
        print("access granted")
        break
    else:
        print("incorrect pin")
        i+=1


