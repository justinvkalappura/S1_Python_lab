# 1. List comprehensions:
# (b) Square of N numbers

num=int(input("Enter the limit:\t"))
sqr=[i*i for i in range(num+1)]
print("Square of numbers is:\t",sqr)