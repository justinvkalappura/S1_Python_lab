# 7. Sort dictionary in ascending and descending order.

dict1={'Milan':43,'Raju':12,'Renju':90,'Biju':16,'Bibin':210,'Arjun':190}

print("Sorting of dictionary:")
print(sorted(dict1.items()))
print(sorted(dict1.items(),key=lambda x:x[1]))
print(sorted(dict1.items(),key=lambda x:x[1],reverse=True))