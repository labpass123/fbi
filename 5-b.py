#5-b: Write a program that demonstrates the column selection, column addition, and column deletion.
import pandas as pd  
  
info = {'one': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),  
        'two': pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}  
  
# Column Selection
d1 = pd.DataFrame(info)  
print("Column 'one':")
print(d1['one'])

# Column Addition
df = pd.DataFrame(info)  
print("Add new column by passing series")  
df['three'] = pd.Series([20, 40, 60], index=['a', 'b', 'c'])  
print(df)  
  
print("Add new column using existing DataFrame columns")  
df['four'] = df['one'] + df['three']  
print(df)

# Column Deletion 
print("The DataFrame:")  
print(df)  
  
# using del function  
print("Delete the first column:")  
del df['one']  
print(df)  

# using pop function  
print("Delete the another column:")  
df.pop('two')  
print(df)
