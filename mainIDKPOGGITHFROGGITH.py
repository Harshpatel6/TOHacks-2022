#IMPORTS
import numpy as np #linear algebra
import pandas as pd #data processing, CSV file I/O (e.g. pd.read_csv)
import json
import os
import seaborn as sns
import matplotlib.pyplot as plt

#get current working directory
cwd = os.getcwd()
path = cwd + "/test.csv"

#data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}  
data1 = pd.read_csv('test.csv')
print(data1.head())

#INPUT USER NUMBER 
val = input("Enter your value: ")
val_list = [val]

#data.insert(val)#add to list
data1.loc[len(data1)] = val_list
print(data1)

#INPUT NUMBER INTO DATABASE
#db = pd.DataFrame(data)#convert list to df


data1.to_csv(path, index=False)#print csv to cwd

#GRAPH IT
sns.set(rc = {'figure.figsize':(15,8)})
sns.histplot(data=data1, x="Number")
plt.show()