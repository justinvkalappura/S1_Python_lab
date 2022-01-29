# 6. Print out all colors from color-list1 not contained in color-list2.

list_1 = []
list_2 = []
n = int(input("Enter number of colours in list 1:"))
m = int(input("Enter number of colours in list 2:"))
print("Enter the colours in the first list:")
for i in range(0, n):
    element = str(input())
    list_1.append(element)
print("Colour list 1 is:")
print(list_1)
print("Enter the colours in the second list:")
for i in range(0, n):
    element = str(input())
    list_2.append(element)
print("Colour list 2 is:")
print(list_2)
print("The colours in list 1 and not in list 2 is:")
for element in list_1:
    if element not in list_2:
        print(element)
        flag=1
    else:
        flag=0
if(flag==0):
        print("Every colour in the list 1 is in the list 2!!!!")