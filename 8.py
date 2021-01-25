import time

while True:
    with open("data.txt") as file:
        print(file.read())
        time.sleep(10)
