import pandas as pd
df = pd.read_excel(r"C:\Users\justi\Desktop\vehicles.xlsx")

# User input: Make, Model, Year, Time spent driving today.
myMake = input("Enter car make: ")
myModel = input("Enter car model: ")
myYear = input("Enter car year: ")
myYear = int(myYear)
myDist = input("Enter distance in km drove today: ")
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
print("You have emitted approximately", myCO2, "grams of CO2 with your irresponsible mode of transportation.")