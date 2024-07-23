import re
def valid(email : str) :
    pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        print(e , "is valid email")
    else :
        print(e, "is invalid email")
e = input("Enter the Email : ")
valid(e)

