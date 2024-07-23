import random
def guess() :
    num = random.randint(1,100)
    print("Im Guessing a number from 1 to 100. You will have to guess it .")
    while True :
        try:
            x = int(input("Enter the number : "))
            if x < 1 or x > 100 :
                print("Enter the Number between 1 and 100")
            elif x < num:
                print("too low ! try again ")
            elif x > num :
                print("too high ! try again ")
            else :
                print("You won!!!! you guessed it Right ")
                break
        except ValueError:
            print("Invalid input")
guess()