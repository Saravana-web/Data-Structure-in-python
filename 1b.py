d={}
for i in range(2):
    k=input("Enter key:")
    v=input("Enter value:")
    d[k]=v
for i in d.values():
    for j in d.values():
               print(i+j)
