# 8. From a list of integers, create a list removing even numbers.

list_1=list()
n=int(input("Enter the number of elements in the list:"))
print("Enter the elements:")
for i in range(0,n):
     element=int(input())
     list_1.append(element)
print("The list after removing even numbers are:")
list_2 = [x for x in list_1 if x%2!=0]
print(list_2)
