# import pandas as pd
# my_dataset={
#     'bike':['KTM','Yamaha','Honda','Harley'],
#     'passings':[1,2,3,4]
# }

# df=pd.DataFrame(my_dataset)
# print(df)

# #pandas series

# a=[1,2,3,4,5]
# ps=pd.Series(a)
# print(ps)

# # #labels
# print(a[0])

# mv=pd.Series(a,index=['a','b','c','d','e'])
# print(mv)

# print(mv['d'])

# data = {
#     "Name": ["Asha", "Ravi", "Neha", "Kiran", "Suman"],
#     "Age": [21, 22, 20, 23, 21],
#     "City": ["Hyderabad", "Bengaluru", "Chennai", "Pune", "Delhi"]
# }

# df = pd.DataFrame(data)

# print(df)

# print(df.loc[0])
# print(df.loc[[0,1]])
# # named indexing
# df = pd.DataFrame(data,index=['n1','n2','n3','n4','n5'])

# print(df.loc['n2'])

# print(df.loc[['n2','n3']])

# # load files into panda dataframe
# df=pd.read_csv('sample.csv')
# print(df.head())

# import pandas as pd
# data={
#     "Movie":["Dhurandar","Baazigar","Devdas","Kabhi kushi kabhi gham"],
#     "genre":["Action", "Comedy", "Drama","Thriller"],
#     "ratings":[4,4,3,5]
# }
# df=pd.DataFrame(data)
# print(df)
# #Averagre rating
# print("Avg Rating:",df["ratings"].mean())
# #top rated movie
# top_movies=df[df["ratings"]>=4.5]
# print(top_movies)
# #low rated movies
# df["need_imporv"]=df["ratings"]<3.5
# print(df)

# task:

# bank tarnsaction analysis 

# track diposit and with drawals
# calculate final balance
# detect high value transactions


# import pandas as pd

# data = {
#     "Transaction_ID": [101, 102, 103, 104],
#     "Type": ["Deposit", "Withdrawal", "Deposit", "Withdrawal"],
#     "Amount": [5000, 2000, 12000, 3000]
# }

# df = pd.DataFrame(data)

# print("Transaction Dataset:")
# print(df)

# total_deposit = df[df["Type"] == "Deposit"]["Amount"].sum()
# total_withdrawal = df[df["Type"] == "Withdrawal"]["Amount"].sum()

# print("\nTotal Deposits:", total_deposit)
# print("Total Withdrawals:", total_withdrawal)

# final_balance = total_deposit - total_withdrawal
# print("\nFinal Balance:", final_balance)

# high_value_txns = df[df["Amount"] > 10000]

# print("\nHigh Value Transactions:")
# print(high_value_txns)

# import pandas as pd
# df=pd.read_csv('sales.csv')
# df['total_sales']=df['Price']*df['Quantity']

# print(df)
# best_prod=df.loc[df['total_sales'].idxmax()]
# print(best_prod)

# df['price_with_tax']=df['Price']*1.10
# print("final data :",df)

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("sales.csv")

# plt.figure()
# plt.barh(df["Product"], df["Price"])
# plt.xlabel("Price")
# plt.ylabel("Product")
# plt.title("Product Price Comparison")

# plt.show()