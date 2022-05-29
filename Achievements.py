import pandas as pd
df = pd.read_excel(r"which python3")

myUsername = input("Enter username: ")
meanCO2 = df["co2"].mean()

# Achievement "V-Card Lost"
entries = df[df["username"] == myUsername]
if not entries.empty:
    print("ACHIEVEMENT UNLOCKED: V-Card Lost")

# Achievement "For Treebeard 3"
entries = df[df["username"] == myUsername]
entries = dict(zip(entries["date"], entries["co2"]))
entries = dict((k, v) for k, v in entries.items() if v < meanCO2)
entries = list(entries.keys())
count = 1
for i in range(1, len(entries)):
    if str(entries[i] - entries[i - 1]) == "1 days 00:00:00":
        count = count + 1
        if count >= 3:
            print("ACHIEVEMENT UNLOCKED: For Treebeard 3")
            break
    else:
        count = 1

# Achievement "For Treebeard 7"
entries = df[df["username"] == myUsername]
entries = dict(zip(entries["date"], entries["co2"]))
entries = dict((k, v) for k, v in entries.items() if v < meanCO2)
entries = list(entries.keys())
count = 1
for i in range(1, len(entries)):
    if str(entries[i] - entries[i - 1]) == "1 days 00:00:00":
        count = count + 1
        if count >= 7:
            print("ACHIEVEMENT UNLOCKED: For Treebeard 7")
            break
    else:
        count = 1

# Achievement "For Treebeard 30"
entries = df[df["username"] == myUsername]
entries = dict(zip(entries["date"], entries["co2"]))
entries = dict((k, v) for k, v in entries.items() if v < meanCO2)
entries = list(entries.keys())
count = 1
for i in range(1, len(entries)):
    if str(entries[i] - entries[i - 1]) == "1 days 00:00:00":
        count = count + 1
        if count >= 30:
            print("ACHIEVEMENT UNLOCKED: For Treebeard 30")
            break
    else:
        count = 1