a = float(input("Enter the first Number : "))
b = float(input("Enter the Second Number : "))
c = input("Enter the operation to perform (+,-,/,*,,%)").strip()
if c == "+" :
    print(f"result = {a+b}")
elif c == "-" :
    print(f"result = {a-b}")
elif c == "*" :
    print(f"result = {a*b}")
elif c == "/" :
    print(f"result = {a/b}")
elif c == "%" :
    print(f"result = {a%b}")
else :
    print("Enter valid input")

