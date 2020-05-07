# A program that uses nested for loops to create a number pyramid.

for i in range(1 , 10):
    for j in range(i + 1):  # (comment for myself) for j in range(1, i + 1): this piece of code will help you remove the 0 
        print (i * j, end = " ")
    print(" ")
