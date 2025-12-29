import random

target= random.randint(1, 100)

while True:
    userChoice= input("Guess the target or Quit: ")
    if(userChoice == "Quit"):
        break
    userChoice= int(userChoice)
    
    if(userChoice== target):
        print("Success: correct guess!!")
        break
    elif(userChoice< target):
        print("Your guess was too small. Try again with a bigger number")
    
    else:
        print("Your guess was too big. Try again with a smaller number")

print("---------- GAME OVER----------------")

    