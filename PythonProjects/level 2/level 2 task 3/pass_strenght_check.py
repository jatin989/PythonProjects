import re
def password() :
    flag = 0
    p = input("Enter the Password : ").strip()
    if len(p) >= 8 :
        flag = flag +1
    lower = re.search(r'[a-z]', p)
    if lower :
        flag = flag + 1
    upper = re.search(r"[A-Z]",p)
    if upper :
        flag = flag + 1
    digit = re.search(r"[0-9]",p)
    if digit :
        flag = flag + 1
    special =  re.search(r'\W',p)
    if special :
        flag = flag + 1
    if flag == 1 :
        print("Your password is weakest")
    if flag == 2 :
        print("Your password is weak")
    if flag == 3 :
        print("Your password is decent")
    if flag == 4 :
        print("Your password is strong")
    if flag == 5 :
        print("Your password is super strong")
password()


