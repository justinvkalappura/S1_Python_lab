#1. Display future leap years from current year to a final year entered by user.

a=int(input("Enter the first year:"))
b=int(input("Enter the final year:"))
print("The leap year in this range are:")
for i in range(a,b):
    if i%400==0 or i%4==0 and i%100!=0:
        print(i)