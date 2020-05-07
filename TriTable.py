# A program that uses nested for loops to create a number pyramid.
# ===== I struggled a bit with this task and had to so some googling to find answers. I found great examples of code but for some reason I can't get rid of the "0" in front.
# ===== I'd also like some help for resources to better explain and help with code like this.

for i in range(1 , 10):
    for j in range(i + 1):  # (comment for myself) for j in range(1, i + 1): this piece of code will help you remove the 0 
        print (i * j, end = " ")
    print(" ")