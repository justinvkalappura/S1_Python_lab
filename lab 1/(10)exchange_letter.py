# 10. Create a string from given string where first and last characters exchanged. [eg:python - > nythop]

word=input("Enter a word:")
print("Before Swapping:",word)
print("After Swapping:",word[-1]+word[1:-1]+word[0])