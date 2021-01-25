import time
import os

while True:
    if os.path.exists("data.txt"):
        with open("data.txt") as file:
            print(file.read())
    else:
        print("File does not exist")
    time.sleep(10)
