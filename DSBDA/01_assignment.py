
# Importing Pandas to create DataFrame
import pandas as pd
import numpy as np

# defining data 
data= [[10,20,30,40,50],[60,70,80,90,100],[110,120,130,140,150],[160,170,180,190,200]]

# # Creating DataFrame and Storing it in variable "df"
df = pd.DataFrame(data)
  
# # Printing Empty DataFrame
# print(df) 

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['A', 'B', 'C', 'D', 'E']
# iris_df = pd.read_csv(url, names=column_names)

# print(iris_df.isnull().sum())
print(df.isnull().sum())
# print(iris_df.describe())
print(df.describe())
# print(iris_df.shape)
print(df.shape)
    
# print(iris_df.dtypes)
print(df.dtypes)
 

# iris_df['sepal_width'] = iris_df['sepal_width'].astype(int)
# df['A'] = df['A'].astype(int)

