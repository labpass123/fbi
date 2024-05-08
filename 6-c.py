# 6-c: Write a program to demonstrate pandas Merging, Joining and Concatenating
import pandas as pd
 
# Define two dictionaries containing employee data 
data1 = {'Name': ['Gangotri', 'Karthik', 'Naresh', 'Pravallika'], 
         'Age': [27, 24, 22, 32], 
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']} 

data2 = {'Name': ['Manoj', 'Varma', 'Kishore', 'Ritesh'], 
         'Age': [17, 14, 12, 52], 
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']} 

# Convert the dictionaries into DataFrames  
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2) 

# Concatenating
concatenated = pd.concat([df1, df2])
print("\nConcatenated DataFrame:\n", concatenated)

# Merging
merged_inner = pd.merge(df1, df2, on='Name', how='inner')
print("\nInner merged DataFrame:\n", merged_inner)

# Joining
joined = df1.join(df2, lsuffix='_df1', rsuffix='_df2')
print("\nJoined DataFrame:\n", joined)
