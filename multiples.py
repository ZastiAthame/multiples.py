loop = True 
while loop:
    multiple = input("Please enter a multiple of 7.")
    multiple = int(multiple)
    if multiple % 7 == 0:
        print("again")
    else:
        print("That is not a multiple of 7!")
        loop = False