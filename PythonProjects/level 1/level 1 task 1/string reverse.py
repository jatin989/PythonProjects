def reverse(x):
    w = ""
    for i in x :
        w = i + w
    return w
x = input("Enter the String :")
rev = reverse(x)
print("reversed string : ",rev )