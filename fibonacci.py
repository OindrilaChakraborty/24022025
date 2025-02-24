#fibonacci

n = (int(input("Enter the number of terms: ")))
n1 = 0
n2 = 1
print("Fibonacci Series: ", n1, "\n", n2)
for i in range(2, n):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3)
    
    
