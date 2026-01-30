import re
text="python is powerful"
result=re.match("python",text)
if result:
    print("match found:",result.group())

text="my num is 1234567890 and 9876543210"
number=re.findall("\d{10}",text)
print(number)

for match in re.finditer("\d{10}",text):
    print("match found at index:",match.start(),"to",match.end())

import re
text="my phone number is 1234567890"
masked=re.sub(R'\d','*',text)
print(masked)