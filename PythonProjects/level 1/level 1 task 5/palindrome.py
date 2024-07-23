x = input("Enter the String :").strip()
w = ""
for i in x :
    w = i + w
if x==w :
    print(f"{x} is Palindrome")
else :
    print(f"{x} is not Palindrome")
