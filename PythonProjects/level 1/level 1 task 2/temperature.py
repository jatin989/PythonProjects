def c_to_f(c) :
    return (c*9/5) + 32
def f_to_c(f) :
    return (f - 32)* 5/9
def main() :
    temp = float(input("Enter the temperature : "))
    unit = input("Enter the unit(C or F) : ").strip().upper()
    if unit == "C" :
        cf = c_to_f(temp)
        print(f"Converted Temperature : {cf:.2f}")
    elif  unit == "F" :
        fc = f_to_c(temp)
        print(f"Converted Temperature : {fc:.2f}")
    else :
        print("Enter the valid input ( C or F)")
main()