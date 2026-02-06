
import pandas as pd
df=pd.read_csv("coust_mis.csv")
print(df)
df['City']=df['City'].str.strip().str.lower()
print(df)