import random
def guess() :
    while True :
        try :
            lower = int(input("Enter the Lower Bound : "))
            upper = int(input("Enter the Upper Bound : "))
            if lower > upper :
                print("Lower bound should be less than Upper Bound")
            else :
                break
        except :
            print("Enter valid Number")
    num = random.randint(lower,upper)
    print(f"Im Guessing a number from {lower} to {upper} /n You will have to guess it .")
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