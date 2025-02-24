n = int(input("Enter a number: "))
if (n%4 == 0 and n%100 != 0) or (n%400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")
    