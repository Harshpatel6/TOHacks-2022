#IMPORTS
import pandas as pd #data processing, CSV file I/O (e.g. pd.read_csv)
from datetime import date
import json
import os
import seaborn as sns
import matplotlib.pyplot as plt

def userIn():
    #INPUT USER NUMBER
    today = date.today()
    user = input("Enter Your Username: ")
    make = input("Enter Your Make (EX: Toyota): " )
    match make:
        case 'Toyota':
            model = input("Enter Your Model (EX: Camry, Corola): ")
        case 'Honda':
            model = input("Enter Your Model (EX: Civic, Accord): ")
        case _:
            print("You are dumb")
    year = input("Enter the year for your car: ")
    d1 = today.strftime("%d/%m/%Y")

    data1.loc[len(data1)] = user, make, model, year, d1
    print(data1)

    data1.to_csv(path, index=False)  # print csv to cwd
    return 0

cwd = os.getcwd()
path = cwd + "/test.csv"

data1 = pd.read_csv('test.csv')
print(data1.head())
loop = True
while loop == True:
    userInp = input("Option 1 to add a value, Option 2 to see the graph: ")
    if userInp == '1':
        userIn()
    elif userInp == '2':
        print("WIP")

    userInp = input("Do you want to exit? 1 for yes, 2 for no: ")
    if userInp == '1':
        loop = False

#GRAPH IT
#sns.set(rc = {'figure.figsize':(15,8)})
#sns.histplot(data=data1, x="Number")
#plt.show()