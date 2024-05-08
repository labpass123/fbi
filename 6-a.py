#6-a:Write a program which use Pandas inbuilt visualization to plot following graphs: i) Bar plots ii) Histograms  iii) Line plots  iv) Scatter plots
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data={'category':['A','B','C','D','E'],'value1':[10,20,15,25,30], 'value2':[5,15,10,20,25]}
df=pd.DataFrame(data)
df.plot(kind='bar',x='category',y=['value1','value2'],title='bar plot')
plt.show()
df['value1'].plot(kind='hist',bins=10,title='histogram')
plt.show()
df.plot(kind='line',x='category',y=['value1','value2'],marker='o',title='line plot')
plt.show()
df.plot(kind='scatter',x='value1',y='value2',title='scatter plot')
