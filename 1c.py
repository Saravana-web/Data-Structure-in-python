l=[]
n=int(input("Enter no  of elements:"))
for i in range(n):
    a=int(input(f"Enter element{i+1}:"))
    l.append(a)

for i  in l:
    for j in l:
        print(i,j)

e=[1,2,3,4]
f=l[1:2]
