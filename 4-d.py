#4-d: Write a program which makes use of the following Pandas methods i) describe() ii) head() iii) tail() iv) info()
import pandas as pd
import numpy as np

# Generating a random series of data
s = pd.Series(np.random.randn(4))

print("The original series is:")
print(s)
print("\n")

print("The first two rows of the data series:")
print(s.head(2))
print("\n")

print("The last two rows of the data series:")
print(s.tail(2))
print("\n")

print("Statistical summary of the data series:")
print(s.describe())
print("\n")

print("Information about the data series:")
print(s.info())
