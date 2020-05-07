# A program that uses nested for loops to create a number pyramid.

for i in range(1 , 10):
    for j in range(i + 1):
        print (i * j, end = " ")
    print(" ")
