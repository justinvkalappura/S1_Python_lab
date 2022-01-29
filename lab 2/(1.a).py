# 1. List comprehensions:
# (a) Generate positive list of numbers from a given list of integers

lst = [10,-79,34,12,-90,56]
lstnew = [n for n in lst if n >= 0]
print("list:",lst)
print("New List Is:", lstnew)