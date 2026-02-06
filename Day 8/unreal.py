import pandas as pd

df = pd.read_csv("employee_unrealistic.csv")

threshold = 10000000

unrealistic_salary = df[df["Salary"] > threshold]

print("Unrealistic Salary Records:")
print(unrealistic_salary)