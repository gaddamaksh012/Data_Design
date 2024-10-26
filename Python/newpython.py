import pandas as pd
df = pd.read_csv("C:/Users/GAKASH/Downloads/u.user.csv",delimiter="|")
print(df.head())
# print(df.head())
for i in df.columns:
    if df[i].dtype == "int64":
        df.sort_values(by=i,inplace=True,index = False)

dt = df.dtypes
print(df)
