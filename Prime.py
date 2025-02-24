n = int(input("Enter a number: "))
temp = 0
for i in range(2, n):
    if ( n%i == 0):
        temp = 1
        break
if (temp == 1):
    print("Not a prime no.")
else:
    print("Is a prime no.")           
    
