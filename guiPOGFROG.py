import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

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

#Store username
manuName = tk.StringVar()


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
    print(manuName.get())

    #clear frame and go to next page
    for widget in manuFrame.winfo_children():
        widget.destroy()

    manuFrame.pack_forget()
    manuFrame.destroy()

    #model_page()



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
    manuLabel = ttk.Label(manuFrame, text="Enter the Make of your vehicle")
    manuLabel.config(anchor='center')
    manuLabel.pack(fill='x', pady=10, side='top', expand=True)

    #Textbox entry for manu
    manuEntry = ttk.Entry(manuFrame, textvariable=manuName)
    manuEntry.pack(fill='x', pady=(10,0), expand=True)
    manuEntry.focus()

    #Next button
    next_button = ttk.Button(manuFrame, text="Next", command=lambda: manu_clicked(manuFrame))
    next_button.pack(fill='x', expand=True, pady=(10,105))

    return manuName





welcomePage()



























root.mainloop()



