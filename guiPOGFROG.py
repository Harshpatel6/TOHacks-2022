import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel(r"C:\Users\justi\Desktop\vehicles.xlsx")

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

#Store dist
distName = tk.StringVar()


def login_clicked(userFrame):
    """ callback when the login button clicked
    """
    print(username.get())#this value should be stored
    
    #clear frame and go to next page
    for widget in userFrame.winfo_children():
        widget.destroy()

    userFrame.pack_forget()
    userFrame.destroy()
    manufact_page()

def manu_clicked(manuFrame):
    #this value should be stored
    print(manuNames.get())
    myMake = manuNames.get()

    #clear frame and go to next page
    for widget in manuFrame.winfo_children():
        widget.destroy()

    manuFrame.pack_forget()
    manuFrame.destroy()

    model_page(myMake)

def model_clicked(modelFrame):
    #this value should be stored
    print(modelName.get())

    #clear frame and go to next page
    for widget in modelFrame.winfo_children():
        widget.destroy()

    modelFrame.pack_forget()
    modelFrame.destroy()

    dist_page()

def dist_clicked(distFrame):
    #this value should be stored
    print(distName.get())

    #clear frame and go to next page
    for widget in distFrame.winfo_children():
        widget.destroy()

    distFrame.pack_forget()
    distFrame.destroy()

    plot_page()







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
    d = {'Number': [5,5,5,7,8,7,5]}
    data1 = pd.DataFrame(d)
    sns.histplot(data=data1, x="Number")
    plt.show()



welcomePage()



























root.mainloop()



