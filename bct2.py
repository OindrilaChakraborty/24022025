#update tuple by user given data

tup = (11, 22, 33)
a = list(tup)  #converting into a list
a.append(44)   #by using append function we can only add one data to the existing list
b = tuple(a)   #again converting it into a tuple
print(b)

tup2 = (10, 20, 30)
x = list(tup2)
x.extend([40, 50]) #by using extend function we can add two data to the existing list
y = tuple(x)
print(y)

#adding two tuple
tup3 = (1, 2, 3)
tup4 = (4, 5, 6)
print(tup3+tup4)