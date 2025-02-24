#armstrong
n = (int(input("Enter a number: ")))

sum = 0
temp = n

while temp > 0:
    q = temp % 10
    sum = sum + (q * q * q)
    temp = temp//10

if (sum == n):
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")


