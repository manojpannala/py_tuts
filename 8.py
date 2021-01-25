import time
import os
import pandas

# using pandas
while True:
    if os.path.exists("temps.csv"):
        data = pandas.read_csv("temps.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist")
    time.sleep(10)
