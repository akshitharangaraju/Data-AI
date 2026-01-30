# playlist=["shape of you","baby","sorry","payphone","perfect"]
# food=["pizza","burger","pasta","salad","ramen","sandwich"]
# location=["beach","mountains","desert","forest","island","lake"]
# print(playlist)
# playlist.append("blinding lights")
# print("updated playlist:",playlist)
# playlist.remove("baby")
# print(playlist)
# playlist.insert(2,"thinking out loud")
# print(playlist)
# playlist.pop()
# print(playlist)
# numbers=[5,3,45,8,104,6,2,111,7,104,4,1]
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers.count(104))
# print(numbers[1])
# numbers[1]=99
# print(numbers[1])
# print(numbers)
# numbers=[10,20,30,40,50]
# print(numbers[:])
# print(numbers[0:3])
# print(numbers[-2:])
# for num in numbers:
#     print(num)
# playlist = ["shape of you", "baby", "sorry", "payphone", "perfect"]
# if "baby" in playlist:
#     print("Found 'baby' in playlist")
# playlist[1]="hello doctor"
# print(playlist)
# order_summary=["pizza",2,500.00,True]
# print(order_summary)
# for index,item in enumerate(order_summary):
#     print(f"Index: {index}, Item: {item}")





# trip_summary=("uber","pondicherry","chennai airport","uber",750.00,"completed")
# print("Trip Summary:",trip_summary)
# # print(trip_summary[2])
# for item in trip_summary:
#     print(item)
# print(len(trip_summary))





# mydict={}
# print(type(mydict))
# mydict={"key1":"value1","key2":"value2","key3":"value3"}
# print(mydict)
# trip={
#     "Service":"Uber",
#     "Pickup":"Pondicherry",
#     "Drop":"Chennai Airport",
#     "Vehicle":"UberX",
#     "Fare":750.00,
#     "Status":"Completed"
# }
# print(trip["Service"])
# print(trip["Fare"])
# print(trip.get("Service"))
# print(trip.get(750.00))
# print(trip.keys())
# print(trip.values())
# for key,value in trip.items():
#     print(f"{key}:{value}")
# trip.update({"Driver":"John Doe"})
# print(trip)
# trip.pop("Driver")
# print(trip)
# trip["Fare"]=4000.00
# print(trip)
# for key in trip:
#     print(key,"->",trip[key])




# st={1,2,9,4,5,6,6}
# print(st)
# uber_cities={"chennai","hyderabad","bombay","goa"}
# uber_cities2={"mumbai","chennai","karnataka"}
# print(uber_cities)
# uber_cities.add("delhi")
# print(uber_cities)
# lst_cities=list(uber_cities)
# print(type(lst_cities))
# print(uber_cities.union(uber_cities2))
# print(uber_cities.intersection(uber_cities2))
# print(uber_cities.difference(uber_cities2))
# uber_cities.add("pune")
# print(uber_cities)
# uber_cities.remove("pune")
# print(uber_cities)



# add=lambda x,y:x+y
# print(add(5,10))

# def add (x,y):
#     return x+y
# print(add(3,7))

# num=[10,9,8,7,6,5,4,3,2,1]
# even=list(filter(lambda x:x%2==0,num))
# print(even)

# data=[
#     {"name":"Alice","age":30},
#     {"name":"Bob","age":25},
#     {"name":"Charlie","age":35}
# ]
# youngest=min(data,key=lambda x:x["age"]<=30)
# print(youngest)

