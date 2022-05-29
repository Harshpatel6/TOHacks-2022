from audioop import avg
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import statistics

# For future person's problem, you should fix directory, and input username
df = pd.read_excel(r"C:\Users\justi\Desktop\ExampleDB.xlsx")
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