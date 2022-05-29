import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
import pandas as pd
import os
from tokenize import String
import psycopg2
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from audioop import avg
from datetime import datetime, timedelta
import statistics

df = pd.read_excel("vehicles.xlsx")

root = tk.Tk()

root.title('CO2 Emissions Tracker Demo')

window_width = 800
window_height = 600

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)

#Store username
username = tk.StringVar()

#Store manu
manuNames = tk.StringVar()
manuNames.set("Select make...")

#Store model
modelName = tk.StringVar()
modelName.set("Select model...")

#Store year
year = tk.StringVar()

#Store dist
distName = tk.StringVar()

#Store option choice
selected = tk.StringVar()

selected2 = tk.StringVar()



def login_clicked(userFrame):
    """ callback when the login button clicked
    """

    #clear frame and go to next page
    for widget in userFrame.winfo_children():
        widget.destroy()

    userFrame.pack_forget()
    userFrame.destroy()
    option_page()

def manu_clicked(manuFrame):
    #this value should be stored
    myMake = manuNames.get()

    #clear frame and go to next page
    for widget in manuFrame.winfo_children():
        widget.destroy()

    manuFrame.pack_forget()
    manuFrame.destroy()

    model_page(myMake)

def model_clicked(modelFrame):
    #this value should be stored

    #clear frame and go to next page
    for widget in modelFrame.winfo_children():
        widget.destroy()

    modelFrame.pack_forget()
    modelFrame.destroy()

    year_page()

def year_clicked(yearFrame):
    #this value should be stored

    #clear frame and go to next page
    for widget in yearFrame.winfo_children():
        widget.destroy()

    yearFrame.pack_forget()
    yearFrame.destroy()

    dist_page()

def dist_clicked(distFrame):
    #this value should be stored
    name = (username.get())
    makeCar = (manuNames.get())
    modelCar = (modelName.get())
    yearCar = (year.get())
    disTrav = (distName.get())

    #clear frame and go to next page
    for widget in distFrame.winfo_children():
        widget.destroy()

    distFrame.pack_forget()
    distFrame.destroy()

    co2 = calculator(makeCar, modelCar, yearCar, disTrav)

    inDatabase(co2, makeCar, modelCar, yearCar, name)

    option2_page()


def option_clicked(optionFrame):

    for widget in optionFrame.winfo_children():
        widget.destroy()

    optionFrame.pack_forget()
    optionFrame.destroy()

    if(selected.get() == 'Insert'):
        manufact_page()
    else: 
        plot_page()
        root.destroy()
        root.mainloop()

    #EITHER MANU PAGE OR PLOT PAGE


def option2_clicked(option2Frame):

    for widget in option2Frame.winfo_children():
        widget.destroy()

    option2Frame.pack_forget()
    option2Frame.destroy()

    if(selected2.get() == 'Option'):
        option_page()
    else: 
        root.destroy()
        root.mainloop()

    #EITHER MANU PAGE OR PLOT PAGE

def calculator(myMake, myModel, myYear, myDist):
    # User input: Make, Model, Year, Time spent driving today.
    if myModel.isdigit():
        myModel = int(myModel)
    myYear = int(myYear)
    myDist = float(myDist) * 1.60934

    # Find comb08 (combined MPG for fuelType1).
    i = df[df["make"] == myMake]
    i = i[i["model"] == myModel]
    i = i[i["year"] == myYear]
    i = i["comb08"].mean()
    myMPG = float(i)

    # Calculate CO2 released. Assumptions: Every gallon of gasoline burned creates 8,887 grams of CO2
    myGallons = myDist / myMPG
    myCO2 = myGallons * 8887

    return  myCO2

def welcomePage():
    #Username frame
    userFrame = ttk.Frame(root)
    userFrame.pack(padx=275, pady=10, fill='x', expand=True)

    #Welcome label
    welcomeLabel = ttk.Label(userFrame, text="Welcome")
    welcomeLabel.config(anchor='center')
    welcomeLabel.pack(fill='x', side='top', expand=False)
    welcomeLabel.configure(font=("Times New Roman", 48, "italic"))

    #Enter username label
    userLabel = ttk.Label(userFrame, text="Enter your Username")
    userLabel.config(anchor='center')
    userLabel.pack(fill='x', pady=(100,0), side='top', expand=False)

    #Textbox entry for username
    userEntry = ttk.Entry(userFrame, textvariable=username)
    userEntry.pack(fill='x', expand=True)
    userEntry.focus()

    #Login button
    login_button = ttk.Button(userFrame, text="Login", command=lambda: login_clicked(userFrame))
    login_button.pack(fill='x', side='bottom', expand=True, pady=10)


def option_page():
    #option frame
    optionFrame = tk.Frame(root)
    optionFrame.pack(padx=275, pady=100, fill='x', expand=False)

    #Enter option label
    manuLabel = ttk.Label(optionFrame, text="Do you want to plot your stats or insert more values?")
    manuLabel.config(anchor='center')
    manuLabel.pack(fill='x', pady=10, expand=True)

    
    r1 = ttk.Radiobutton(optionFrame, text='Plot', value='Plot', variable=selected).pack(fill='x', padx=5, pady=5)
    r2 = ttk.Radiobutton(optionFrame, text='Insert', value='Insert', variable=selected).pack(fill='x', padx=5, pady=5)
    
    #Next button
    next_button = ttk.Button(optionFrame, text="Next", command=lambda: option_clicked(optionFrame))
    next_button.pack(fill='x', expand=True, pady=(10,105))

    return selected


def option2_page():
    #option frame
    option2Frame = tk.Frame(root)
    option2Frame.pack(padx=275, pady=100, fill='x', expand=False)

    #Enter option label
    manuLabel = ttk.Label(option2Frame, text="Do you want to go back to the beginning or Exit?")
    manuLabel.config(anchor='center')
    manuLabel.pack(fill='x', pady=10, expand=True)

    
    r1 = ttk.Radiobutton(option2Frame, text='Option', value='Option', variable=selected2).pack(fill='x', padx=5, pady=5)
    r2 = ttk.Radiobutton(option2Frame, text='Exit', value='Exit', variable=selected2).pack(fill='x', padx=5, pady=5)
    
    #Next button
    next_button = ttk.Button(option2Frame, text="Next", command=lambda: option2_clicked(option2Frame))
    next_button.pack(fill='x', expand=True, pady=(10,105))

    return selected2



def manufact_page():
    #manu frame
    manuFrame = tk.Frame(root)
    manuFrame.pack(padx=275, pady=(225,100), fill='x', expand=False)

    #Enter manu label
    manuLabel = ttk.Label(manuFrame, text="Enter the make of your vehicle")
    manuLabel.config(anchor='center')
    manuLabel.pack(fill='x', pady=10, expand=True)

    #Textbox entry for manu
    myMake = df["make"]
    myMake = myMake.tolist()
    myMake = sorted(list(set(myMake)), key = str.lower)

    w = ttk.Combobox(manuFrame, textvariable = manuNames, values = myMake)
    w.pack(fill='x', pady=(10,0), expand=True)

    #Next button
    next_button = ttk.Button(manuFrame, text="Next", command=lambda: manu_clicked(manuFrame))
    next_button.pack(fill='x', expand=True, pady=(10,105))
    myMake = manuNames.get()

    return myMake

def model_page(manuNames):
    #model frame
    modelFrame = tk.Frame(root)
    modelFrame.pack(padx=275, pady=(225,100), fill='x', expand=False)

    #Enter model label
    modelLabel = ttk.Label(modelFrame, text="Enter the model of your vehicle")
    modelLabel.config(anchor='center')
    modelLabel.pack(fill='x', pady=10, side='top', expand=True)

    #Textbox entry for model
    userMake = manuNames
    myModels = df["model"][df["make"] == userMake]
    myModels = myModels.tolist()
    myModels = list(set(myModels))
    myModels = list(map(str, myModels))
    myModels = sorted(myModels, key = str.lower)

    w = ttk.Combobox(modelFrame, textvariable = modelName, values = myModels)
    w.pack(fill='x', pady=(10,0), expand=True)

    #Next button
    next_button = ttk.Button(modelFrame, text="Next", command=lambda: model_clicked(modelFrame))
    next_button.pack(fill='x', expand=True, pady=(10,105))

    return modelName

def year_page():
    #model frame
    yearFrame = tk.Frame(root)
    yearFrame.pack(padx=275, pady=(225,100), fill='x', expand=False)

    #Enter model label
    yearLabel = ttk.Label(yearFrame, text="Enter the year of your vehicle")
    yearLabel.config(anchor='center')
    yearLabel.pack(fill='x', pady=10, side='top', expand=True)

    #Textbox entry for username
    userEntry = ttk.Entry(yearFrame, textvariable=year)
    userEntry.pack(fill='x', expand=True)
    userEntry.focus()

    #Next button
    next_button = ttk.Button(yearFrame, text="Next", command=lambda: year_clicked(yearFrame))
    next_button.pack(fill='x', expand=True, pady=(10,105))

    return modelName

def dist_page():
    #dist frame
    distFrame = tk.Frame(root)
    distFrame.pack(padx=275, pady=(225,100), fill='x', expand=False)

    #Enter dist label
    distLabel = ttk.Label(distFrame, text="Enter distanced travelled today in kilometers")
    distLabel.config(anchor='center')
    distLabel.pack(fill='x', pady=10, side='top', expand=True)

    #Textbox entry for dist
    distEntry = ttk.Entry(distFrame, textvariable=distName)
    distEntry.pack(fill='x', pady=(10,0), expand=True)
    distEntry.focus()

    #Next button
    next_button = ttk.Button(distFrame, text="Next", command=lambda: dist_clicked(distFrame))
    next_button.pack(fill='x', expand=True, pady=(10,105))

    return distName

def plot_page():
    df = pd.read_excel(r"ExampleDB.xlsx")
    myUsername = "justinjyou"

    pastSevenDays = []
    userCO2 = []
    avgCO2 = []
    # For loop 7 times, get 7 days from present day, and co2 data from user and average co2 data
    for i in reversed(range(7)):
        d = datetime.today() - timedelta(days = i)
        d = str(d).split()
        d = d[0]
        pastSevenDays.append(d)
        userCO2AtI = df[df["username"] == myUsername]
        if not list(userCO2AtI[userCO2AtI["date"] == d]["co2"]):
            userCO2.append(0)
        else:
            userCO2AtI = float(userCO2AtI[userCO2AtI["date"] == d]["co2"])
            userCO2.append(userCO2AtI)
        if list(df[df["date"] == d]["co2"]):
            avgCO2AtI = float(statistics.mean(list(df[df["date"] == d]["co2"])))
            avgCO2.append(avgCO2AtI)
        else:
            avgCO2.append(0)

    print(pastSevenDays)
    print(userCO2)
    print(avgCO2)

    plt.plot(pastSevenDays, userCO2, label = "Your CO2 emission")
    plt.plot(pastSevenDays, avgCO2, label = "Average CO2 emission")
    plt.legend()
    plt.ylabel('Daily CO2 emission (g)', fontsize=14)
    plt.grid(True)
    plt.show()

def inDatabase(co2, makeCar, modelCar, yearCar, user):
    def exec_statement(conn, stmt, list1):
        try:
            with conn.cursor() as cur:
                cur.execute(stmt, list1)
                row = cur.fetchone()
                conn.commit()
                if row: print(row[0])
        except psycopg2.ProgrammingError:
            return

    def inse(list1):

        # Connect to CockroachDB
        connection = psycopg2.connect(os.environ['DATABASE_URL'])

        statements = [

            """INSERT INTO coEmissionsTable (username, make, model, modelYear, date, co2)
                VALUES (%s,%s,%s,%s,%s,%s)
            """,

            'SELECT * FROM coEmissionsTable'
        ]

        for statement in statements:
            exec_statement(connection, statement, list1)

        # Close communication with the database
        connection.close()

    date_object = datetime.date.today()

    list1 = [user, makeCar, modelCar, yearCar, date_object, co2]

    list_as_tuple = tuple(list1)
    inse(list1)

welcomePage()



























root.mainloop()



