import random
guess_taken = 5
hidden = random.randint(1,20)

guess = int(input("Enter a number between 1 and 20 :"))

while guess != hidden :
    if guess > hidden:
        print("Too high!")
    else:
        print("Too low!")

    guess_taken -= 1


        
    print(" Not correct")
    guess = int(input("Enter again : "))
    if guess_taken == 0:
        print("game over")
        break
if hidden == guess:   
    print("Correct!")