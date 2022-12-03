import pandas as pd
import numpy as np

data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


birds_df = pd.DataFrame(data,index = [labels])


print(birds_df)
print(birds_df.info())
print(birds_df.describe())
print(birds_df.head(2))

print(birds_df.iloc[[0,1,2,6,5]])
print("************")
print(birds_df.loc[birds_df.birds == 'Maruti'])

print(birds_df[["birds","age"]])
print("######################")
print(birds_df.iloc[[2,3,7],0:2])



visits = birds_df[birds_df["visits"] > 4]

print(visits)


