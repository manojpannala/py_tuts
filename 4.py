while True:
    username = input ("Say Something: ")
    if username == "/end":
        break
    #print("Correct")
    else:
        continue
    #print("Wrong")
    
    message = f"Hello {username}!!!"
    print(message)
