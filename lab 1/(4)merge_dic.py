#4. Merge two dictionaries

dic_1 = dict()
dic_2 = dict()
n=int(input("Enter the number of elements in dicitionary 1:"))
m=int(input("Enter the number of elements in dicitionary 2:"))
print('Enter (key:value) in dictionary 1:')
for i in range (0,n):
  data = input()
  temp = data.split(':')
  dic_1[temp[0]] = temp[1]
print(dic_1)
print('Enter (key:value) in dictionary 2:')
for i in range (0,m):
    data = input()
    temp = data.split(':')
    dic_2[temp[0]] = temp[1]
print(dic_2)
dic_1.update(dic_2)
print("Updated dictionary is:")
print(dic_1)