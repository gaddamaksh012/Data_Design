import pandas as pd
data = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
lst1 = [1,2,3,4,5,6]

try:
    df1 = pd.DataFrame(lst1)
    # print(df1)
    df = pd.read_table("C:/Users/GAKASH/Desktop/u.user.txt",delimiter="|")
    # print(df)
except Exception as e:
  print(e)


df1 = pd.read_csv("C:/Users/GAKASH/Desktop/My_Employee.csv")
df1["town"] = "Hyderabad"
df1.drop("town",inplace=True,axis=1)

df2 = pd.read_csv("C:/Users/GAKASH/Downloads/data/datasource (1)/New folder/used_car_prices1.csv")
df3 = pd.read_csv("C:/Users/GAKASH/Downloads/data/datasource (1)/New folder/used_car_prices2.csv")
df4 = pd.read_csv("C:/Users/GAKASH/Downloads/data/datasource (1)/New folder/used_car_prices3.csv")


# Total joins

df_concat1 = pd.concat([df2,df3],ignore_index=True,axis=0)
# print(df_concat1)

df_concat2 = pd.concat([df2,df3],ignore_index=True,axis=1)
# print(df_concat2)

df_join = df.join(df2)

print(df_join)
print(df2.shape)
print(df.shape)
print(df)


